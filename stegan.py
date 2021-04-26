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

    text_len = os.stat(text).st_size
    img_len = os.stat(start_image).st_size
    if text_len >= img_len * Globals.degree / Globals.bits - Globals.BMP_HEADER_SIZE:
        print('Too long text')
        return
    with open(text, 'r') as text, open(start_image, 'rb') as start_bmp, open(
            final_image, 'wb') as final_bmp:

        final_bmp.write(start_bmp.read(Globals.BMP_HEADER_SIZE))
        text_mask, img_mask = create_masks(Globals.degree)

        while True:
            symbol = text.read(Globals.step)
            if not symbol:
                for byte_amount in range(Globals.first_bit, Globals.last_bit,
                                         Globals.degree):
                    img_byte = int.from_bytes(start_bmp.read(Globals.step),
                                              sys.byteorder) & img_mask
                    bits = Globals.last_byte & text_mask
                    bits >>= (Globals.bits - Globals.degree)
                    img_byte |= bits
                    final_bmp.write(
                        img_byte.to_bytes(Globals.step, sys.byteorder))
                break
            symbol = ord(symbol)
            for byte_amount in range(Globals.first_bit, Globals.last_bit,
                                     Globals.degree):
                img_byte = int.from_bytes(start_bmp.read(Globals.step),
                                          sys.byteorder) & img_mask
                bits = symbol & text_mask
                bits >>= (Globals.bits - Globals.degree)
                img_byte |= bits
                final_bmp.write(img_byte.to_bytes(Globals.step, sys.byteorder))
                symbol <<= Globals.degree
        final_bmp.write(start_bmp.read())

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

    with open(output_text, 'w', encoding='utf-8') as text, open(
            start_image, 'rb') as Encryptd_bmp:

        Encryptd_bmp.seek(Globals.BMP_HEADER_SIZE)

        text_mask, img_mask = create_masks(Globals.degree)
        img_mask = ~img_mask

        read = Globals.empty_value
        while True:
            symbol = Globals.empty_value

            for bits_read in range(Globals.first_bit, Globals.last_bit,
                                   Globals.degree):
                img_byte = int.from_bytes(Encryptd_bmp.read(Globals.step),
                                          sys.byteorder) & img_mask
                symbol <<= Globals.degree
                symbol |= img_byte

            if chr(symbol) == '\n' and len(os.linesep) == Globals.degree:
                read += Globals.step

            read += Globals.step
            if symbol == Globals.last_byte:
                break
            text.write(chr(symbol))

    return True


def create_masks(degree):
    '''Функция, которая создает маски для байтов текста и изображения'''

    Globals.text_mask <<= (Globals.bits - degree)
    Globals.text_mask %= Globals.number_of_bits
    Globals.img_mask >>= degree
    Globals.img_mask <<= degree

    return Globals.text_mask, Globals.img_mask
