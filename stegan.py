import os
import sys
from globals import Globals


def encrypt(text, start_image, final_image):
    '''
    Функция, которая зашифровывает текст в картинку формата .bmp. Функция,
    после того, как зашифровывает весь текст, шифрует в конце символ NULL,
    который говорит о конце текста
    :param text: название файла, в котором лежит текст в формате 'text.txt'
    :param start_image: название изображения, в которое нужно зашифровать текст
    в формате 'start_image.bmp'
    :param final_image: имя зашифрованного изображения в формате
    'final_image.bmp'
    '''

    text_len = os.stat('text.txt').st_size
    img_len = os.stat('start.bmp').st_size
    if text_len >= img_len * Globals.degree / 8 - Globals.BMP_HEADER_SIZE:
        print('Too long text')
        return
    text = open(text, 'r')
    start_bmp = open(start_image, 'rb')
    final_bmp = open(final_image, 'wb')

    final_bmp.write(start_bmp.read(Globals.BMP_HEADER_SIZE))
    text_mask, img_mask = create_masks(Globals.degree)

    while True:
        symbol = text.read(1)
        if not symbol:
            last_byte = 0b00000000
            for byte_amount in range(0, 8, Globals.degree):
                img_byte = int.from_bytes(start_bmp.read(1),
                                          sys.byteorder) & img_mask
                bits = last_byte & text_mask
                bits >>= (8 - Globals.degree)
                img_byte |= bits
                final_bmp.write(img_byte.to_bytes(1, sys.byteorder))
            break
        symbol = ord(symbol)
        for byte_amount in range(0, 8, Globals.degree):
            img_byte = int.from_bytes(start_bmp.read(1),
                                      sys.byteorder) & img_mask
            bits = symbol & text_mask
            bits >>= (8 - Globals.degree)
            img_byte |= bits
            final_bmp.write(img_byte.to_bytes(1, sys.byteorder))
            symbol <<= Globals.degree
    final_bmp.write(start_bmp.read())

    text.close()
    start_bmp.close()
    final_bmp.close()
    return True


def decrypt(start_image, output_text):
    '''
    Функция, которая расфровывает текст из картинки формата .bmp. Функция
    перестает асшифровывать текст, когда доходит до символа NULL
    :param start_image: название изображения с зашифрованным текстом в формате
    'start_image.bmp'
    :param output_text: название файла, в который нужно записать
    расшифрованный текст в формате 'text.txt'
    '''

    text = open(output_text, 'w', encoding='utf-8')
    encoded_bmp = open(start_image, 'rb')

    encoded_bmp.seek(Globals.BMP_HEADER_SIZE)

    text_mask, img_mask = create_masks(Globals.degree)
    img_mask = ~img_mask

    read = 0
    while True:
        symbol = 0

        for bits_read in range(0, 8, Globals.degree):
            img_byte = int.from_bytes(encoded_bmp.read(1),
                                      sys.byteorder) & img_mask
            symbol <<= Globals.degree
            symbol |= img_byte

        if chr(symbol) == '\n' and len(os.linesep) == 2:
            read += 1

        read += 1
        if symbol == 0b00000000:
            break
        text.write(chr(symbol))

    text.close()
    encoded_bmp.close()
    return True


def create_masks(degree):
    '''Функция, которая создает маски для байтов текста и изображения'''
    text_mask = 0b11111111
    img_mask = 0b11111111

    text_mask <<= (8 - degree)
    text_mask %= 256
    img_mask >>= degree
    img_mask <<= degree

    return text_mask, img_mask
