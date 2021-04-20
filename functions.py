import collections
from globals import Globals


def caesar_cipher(input_txt, output_txt, step, choice):
    '''
    Функция, зашифровывающая и расшифровывающая текст с помощью шифра Цезаря.
    :param input_txt: название файла, в котором лежит текст, который должна
    зашифровать функция
    :param output_txt: название файла, в котором будет лежать зашифрованный
    текст
    :param choice: зашифровать или расшифровать текст
    :param step: число, являющееся шагом шифрования
    '''
    if choice == 'Encode':
        choice = 1
    elif choice == 'Decode':
        choice = -1
    with open(input_txt, 'r') as text, open(output_txt, 'w') as code:
        text_list = text.readlines()
        working_line = ''
        code_list = []

        for line in text_list:
            line = line.lower()
            for symbol in line:
                if symbol not in Globals.alphabet:
                    working_line += symbol
                else:
                    working_line += Globals.alphabet[
                        (Globals.alphabet.find(symbol) + step * choice) % len(
                            Globals.alphabet)]
            code_list.append(working_line)
            working_line = ''
        for line in code_list:
            code.write(line)
    return code


def caesar_analysys(input_txt, output_txt):
    '''
    Фуекция, которая взламывает шифр Цезар методом анализа частоты вхождений
    букв английского алфавита в зашифрованный текст. Функция не работает для
    коротких текстов.
    :param input_txt: название файла, в котором лежит зашифрованный текст
    :param output_txt: название файла, в котором будет лежать взломанный текст
    '''

    with open(input_txt, 'r') as code:

        code_list = code.readlines()

        all_letters = ''

        for line in code_list:
            line = line.lower()
            for symbol in line:
                if symbol in Globals.alphabet:
                    all_letters += symbol

        most_common_element = \
            collections.Counter(all_letters).most_common(1)[0][0]
        key = Globals.alphabet.find(
            most_common_element) - Globals.alphabet.find(
            Globals.most_common_letter)

    return caesar_cipher(input_txt, output_txt, key, 'Decode')


def vegenere_cipher(input_txt, output_txt, k):
    '''
    Функция, зашифровывающая текст с помощью шифра Виженера.
    :param input_txt: название файла, в котором лежит текст, который должна
    зашифровать функция
    :param output_txt: название файла, в котором будет лежать зашифрованный
    текст
    :param k: слово, являющееся ключом шифрования
    :return:
    '''

    with open(input_txt, 'r') as text, open(output_txt, 'w') as code:

        text_list = text.readlines()
        working_line = ''
        code_list = []
        all_str = ''

        k = k.lower()

        for i, line in enumerate(text_list):
            if i < len(text_list) - 1:
                all_str += line[:-1] + ' '
            elif i == len(text_list) - 1:
                all_str += line
        i = 0
        j = 0
        key = ''
        while i < len(all_str):
            if all_str[i] in Globals.alphabet:
                key += k[j % len(k)]
                i += 1
                j += 1
            elif all_str[i] not in Globals.alphabet:
                key += Globals.random_letter
                i += 1

        for line in text_list:
            line = line.lower()
            for i, symbol in enumerate(line):
                if symbol not in Globals.alphabet:
                    working_line += symbol
                else:
                    working_line += Globals.alphabet[
                        (Globals.alphabet.find(symbol) + Globals.alphabet.find(
                            key[i])) % len(
                            Globals.alphabet)]
            code_list.append(working_line)
            working_line = ''
        for line in code_list:
            code.write(line)
    return code


def de_vegenere_cipher(input_txt, output_txt, k):
    '''
    Функция, расшифровывающая шифр Виженера.
    :param input_txt: название файла, в котором лежит зашифрованный текст,
    который должна расшифровать функция
    :param output_txt: название файла, в котором будет лежать расшифрованный
    текст
    :param k: слово, являющееся ключом шифрования
    '''

    with open(input_txt, 'r') as code, open(output_txt, 'w') as text:

        code_list = code.readlines()
        working_line = ''
        text_list = []
        all_str = ''

        k = k.lower()

        for i, line in enumerate(code_list):
            if i < len(code_list) - 1:
                all_str += line[:-1] + ' '
            elif i == len(code_list) - 1:
                all_str += line
        i = 0
        j = 0
        key = ''
        while i < len(all_str):
            if all_str[i] in Globals.alphabet:
                key += k[j % len(k)]
                i += 1
                j += 1
            elif all_str[i] not in Globals.alphabet:
                key += Globals.random_letter
                i += 1

        for line in code_list:
            line = line.lower()
            for i, symbol in enumerate(line):
                if symbol not in Globals.alphabet:
                    working_line += symbol
                else:
                    working_line += Globals.alphabet[
                        (Globals.alphabet.find(symbol) - Globals.alphabet.find(
                            key[i])) % len(
                            Globals.alphabet)]
            text_list.append(working_line)
            working_line = ''
        for line in text_list:
            text.write(line)
    return text


def vernam_cipher(input_txt, output_txt, input_key):
    '''
    Функция, зашифровывающая текст с помощью шифра Вернама.
    :param input_txt: название файла, в котором лежит текст, который должна
    зашифровать функция
    :param output_txt: название файла, в котором будет лежать зашифрованный
    текст
    :param input_key: слово, являющееся ключом шифрования
    '''

    with open(input_txt, 'r') as text, open(output_txt, 'w') as code:

        text_list = text.readlines()
        working_line = ''
        code_list = []
        all_str = ''

        input_key = input_key.lower()

        for i, line in enumerate(text_list):
            if i < len(text_list) - 1:
                all_str += line[:-1] + ' '
            elif i == len(text_list) - 1:
                all_str += line

        i = 0
        j = 0
        key = ''
        while i < len(all_str):
            if all_str[i] in Globals.alphabet:
                key += input_key[j % len(input_key)]
                i += 1
                j += 1
            elif all_str[i] not in Globals.alphabet:
                key += Globals.random_letter
                i += 1
        for line in text_list:
            line = line.lower()
            for i, symbol in enumerate(line):
                if symbol not in Globals.alphabet:
                    working_line += symbol
                else:
                    working_line += Globals.alphabet[
                        (Globals.alphabet.find(symbol) + Globals.alphabet.find(
                            key[i])) % len(
                            Globals.alphabet)]
            code_list.append(working_line)
            working_line = ''
        for line in code_list:
            code.write(line)
    return code


def de_vernam_cipher(input_txt, output_txt, input_key):
    '''
    Функция, расшифровывающая шифр Вернама.
    :param input_txt: название файла, в котором лежит зашифрованный текст,
    который должна расшифровать функция
    :param output_txt: название файла, в котором будет лежать расшифрованный
    текст
    :param input_key: слово, являющееся ключом шифрования
    '''

    with open(input_txt, 'r') as code, open(output_txt, 'w') as text:

        code_list = code.readlines()
        working_line = ''
        text_list = []
        all_str = ''

        input_key = input_key.lower()

        for i, line in enumerate(code_list):
            if i < len(code_list) - 1:
                all_str += line[:-1] + ' '
            elif i == len(code_list) - 1:
                all_str += line

        i = 0
        j = 0
        key = ''
        while i < len(all_str):
            if all_str[i] in Globals.alphabet:
                key += input_key[j]
                i += 1
                j += 1
            elif all_str[i] not in Globals.alphabet:
                key += Globals.random_letter
                i += 1
        for line in code_list:
            line = line.lower()
            for i, symbol in enumerate(line):
                if symbol not in Globals.alphabet:
                    working_line += symbol
                else:
                    working_line += Globals.alphabet[
                        (Globals.alphabet.find(symbol) - Globals.alphabet.find(
                            key[i])) % len(
                            Globals.alphabet)]
            text_list.append(working_line)
            working_line = ''
        for line in text_list:
            text.write(line)
    return text


def morse_code(input_txt, output_txt):
    '''
    Функция, зашифровывающая текст азбукой Морзе.
    :param input_txt: название файла, в котором лежит текст, который должна
    зашифровать функция
    :param output_txt: название файла, в котором будет лежать зашифрованный
    текст
    '''

    with open(input_txt, 'r') as text, open(output_txt, 'w') as code:

        text_list = text.readlines()
        working_line = ''
        code_list = []

        for line in text_list:
            line = line.lower()
            for symbol in line:
                if symbol not in Globals.morse.keys():
                    working_line += symbol
                else:
                    working_line = working_line + Globals.morse[symbol] + ' '
            code_list.append(working_line)
            working_line = ''
        for line in code_list:
            code.write(line)
    return code


def de_morse_code(input_txt, output_txt):
    '''
    Функция, расшифровывающая текст азбукой Морзе.
    :param input_txt: название файла, в котором лежит зашифрованный текст,
    который должна расшифровать функция
    :param output_txt: название файла, в котором будет лежать расшифрованный
    текст
    '''

    reversed_morse = {}

    for key, value in Globals.morse.items():
        reversed_morse[value] = key

    with open(input_txt, 'r') as code, open(output_txt, 'w') as text:

        code_list = code.readlines()
        working_line = ''
        text_list = []

        for line in code_list:
            words = line.split('  ')
            for word in words:
                letters = word.split()
                for symbol in letters:
                    if symbol not in reversed_morse.keys():
                        working_line += symbol
                    else:
                        working_line = working_line + reversed_morse[symbol]
                working_line += ' '
            working_line += '\n'
            text_list.append(working_line)
            working_line = ''
        for line in text_list:
            text.write(line)
    return text
