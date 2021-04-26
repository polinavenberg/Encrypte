from functions import caesar_cipher, morse_code, vegenere_cipher, vernam_cipher
from functions import de_morse_code
from functions import caesar_analysys


def caesar_cipher_work():
    choice = input(
        'en - Encrypt, de - Decrypt, cr - cracking a caesar cipher\n')
    input_text = input('print the name of the file with your text\n')
    output_text = input('print the name of the output file\n')
    if choice == 'crack':
        return caesar_analysys(input_text, output_text)
    key = int(input('print the key(shift) for coding\n'))
    if choice == 'en':
        return caesar_cipher(input_text, output_text, key, 'Encrypt')
    elif choice == 'de':
        return caesar_cipher(input_text, output_text, key, 'Decrypt')


def vegenere_cipher_work():
    choice = input('en - Encrypt, de - Decrypt\n')
    input_text = input('print the name of the file with your text\n')
    output_text = input('print the name of the output file\n')
    key = input('print the key word for coding\n')
    if choice == 'en':
        return vegenere_cipher(input_text, output_text, key, 'Encrypt')
    elif choice == 'de':
        return vegenere_cipher(input_text, output_text, key, 'Decrypt')


def vernam_cipher_work():
    choice = input('en - Encrypt, de - Decrypt\n')
    input_text = input('print the name of the file with your text\n')
    output_text = input('print the name of the output file \n')
    key = input(
        'print the key word for coding, it length must be the \
        same as the length of the text\n')
    if choice == 'en':
        return vernam_cipher(input_text, output_text, key, 'Encrypt')
    elif choice == 'de':
        return vernam_cipher(input_text, output_text, key, 'Decrypt')


def morse_code_work():
    choice = input('en - Encrypt, de - Decrypt\n')
    input_text = input('print the name of the file with your text\n')
    output_text = input('print the name of the output file \n')
    if choice == 'en':
        return morse_code(input_text, output_text)
    elif choice == 'de':
        return de_morse_code(input_text, output_text)


choice_dict = {'caesar': caesar_cipher_work,
               'vegenere': vegenere_cipher_work,
               'vernam': vernam_cipher_work, 'morse': morse_code_work}


def start():
    '''Функция запускает консольную версию программы и ожидает ввод всех
    необходимых параметров'''
    while True:
        choice = input('caesar, vegenere, vernam, morse cipher or quit\n')
        if choice == 'quit':
            break
        global choice_dict
        choice_dict[choice]()
