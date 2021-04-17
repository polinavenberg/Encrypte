import collections
from globals import Globals


def caesar_cipher(input_txt, output_txt, step):
    '''
    Функция, создающая шифр Цезаря.
    :param input_txt: название файла, в котором лежит текст, который должна
    зашифровать функция
    :param output_txt: название файла, в котором будет лежать зашифрованный
    текст
    :param step: число, являющееся шагом шифрования
    '''

    text = open(input_txt, 'r')
    code = open(output_txt, 'w')

    text_list = text.readlines()
    working_line = ''
    code_list = []

    for line in text_list:
        line = line.lower()
        for l in line:
            if l not in Globals.a:
                working_line += l
            else:
                working_line += Globals.a[
                    (Globals.a.find(l) + step) % len(Globals.a)]
        code_list.append(working_line)
        working_line = ''
    for line in code_list:
        code.write(line)
    text.close()
    code.close()
    return code


def de_caesar_cipher(input_txt, output_txt, step):
    '''
    Функция, расшифровывающая шифр Цезаря.
    :param input_txt: название файла, в котором лежит зашифрованный текст
    :param output_txt: название файла, в котором будет лежать расшифрованный
    текст
    :param step: число, являющееся шагом шифрования
    '''

    code = open(input_txt, 'r')
    text = open(output_txt, 'w')

    code_list = code.readlines()
    working_line = ''
    text_list = []

    for line in code_list:
        line = line.lower()
        for l in line:
            if l not in Globals.a:
                working_line += l
            else:
                working_line += Globals.a[
                    (Globals.a.find(l) - step) % len(Globals.a)]
        text_list.append(working_line)
        working_line = ''
    for line in text_list:
        text.write(line)
    text.close()
    code.close()
    return text


def caesar_analysys(input_txt, output_txt):
    '''
    Фуекция, которая взламывает шифр Цезар методом анализа частоты вхождений
    букв английского алфавита в зашифрованный текст. Функция не работает для
    коротких текстов.
    :param input_txt: название файла, в котором лежит зашифрованный текст
    :param output_txt: название файла, в котором будет лежать взломанный текст
    '''

    code = open(input_txt, 'r')

    code_list = code.readlines()

    all_letters = ''

    for line in code_list:
        line = line.lower()
        for l in line:
            if l in Globals.a:
                all_letters += l

    most_common_element = collections.Counter(all_letters).most_common(1)[0][0]
    key = Globals.a.find(most_common_element) - Globals.a.find(
        Globals.most_common_letter)

    code.close()
    return de_caesar_cipher(input_txt, output_txt, key)


def vegenere_cipher(input_txt, output_txt, k):
    '''
    Функция, создающая шифр Виженера.
    :param input_txt: название файла, в котором лежит текст, который должна
    зашифровать функция
    :param output_txt: название файла, в котором будет лежать зашифрованный
    текст
    :param k: слово, являющееся ключом шифрования
    :return:
    '''

    text = open(input_txt, 'r')
    code = open(output_txt, 'w')

    text_list = text.readlines()
    working_line = ''
    code_list = []
    all_str = ''

    k = k.lower()

    for i, line in enumerate(text_list):
        if i < len(text_list) - 1:
            all_str += line[:-1] + ' '
            print('')
        elif i == len(text_list) - 1:
            all_str += line
    i = 0
    j = 0
    key = ''
    while i < len(all_str):
        if all_str[i] in Globals.a:
            key += k[j % len(k)]
            i += 1
            j += 1
        elif all_str[i] not in Globals.a:
            key += Globals.random_letter
            i += 1

    for line in text_list:
        line = line.lower()
        for i, l in enumerate(line):
            if l not in Globals.a:
                working_line += l
            else:
                working_line += Globals.a[
                    (Globals.a.find(l) + Globals.a.find(key[i])) % len(
                        Globals.a)]
        code_list.append(working_line)
        working_line = ''
    for line in code_list:
        code.write(line)
    text.close()
    code.close()
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

    code = open(input_txt, 'r')
    text = open(output_txt, 'w')

    code_list = code.readlines()
    working_line = ''
    text_list = []
    all_str = ''

    k = k.lower()

    for i, line in enumerate(code_list):
        if i < len(code_list) - 1:
            all_str += line[:-1] + ' '
            print('')
        elif i == len(code_list) - 1:
            all_str += line
    i = 0
    j = 0
    key = ''
    while i < len(all_str):
        if all_str[i] in Globals.a:
            key += k[j % len(k)]
            i += 1
            j += 1
        elif all_str[i] not in Globals.a:
            key += Globals.random_letter
            i += 1

    for line in code_list:
        line = line.lower()
        for i, l in enumerate(line):
            if l not in Globals.a:
                working_line += l
            else:
                working_line += Globals.a[
                    (Globals.a.find(l) - Globals.a.find(key[i])) % len(
                        Globals.a)]
        text_list.append(working_line)
        working_line = ''
    for line in text_list:
        text.write(line)
    text.close()
    code.close()
    return text


def vernam_cipher(input_txt, output_txt, k):
    '''
    Функция, создающая шифр Вернама.
    :param input_txt: название файла, в котором лежит текст, который должна
    зашифровать функция
    :param output_txt: название файла, в котором будет лежать зашифрованный
    текст
    :param k: слово, являющееся ключом шифрования
    '''

    text = open(input_txt, 'r')
    code = open(output_txt, 'w')

    text_list = text.readlines()
    working_line = ''
    code_list = []
    all_str = ''

    k = k.lower()

    for i, line in enumerate(text_list):
        if i < len(text_list) - 1:
            all_str += line[:-1] + ' '
            print('')
        elif i == len(text_list) - 1:
            all_str += line

    i = 0
    j = 0
    key = ''
    while i < len(all_str):
        if all_str[i] in Globals.a:
            key += k[j % len(k)]
            i += 1
            j += 1
        elif all_str[i] not in Globals.a:
            key += Globals.random_letter
            i += 1
    for line in text_list:
        line = line.lower()
        for i, l in enumerate(line):
            if l not in Globals.a:
                working_line += l
            else:
                working_line += Globals.a[
                    (Globals.a.find(l) + Globals.a.find(key[i])) % len(
                        Globals.a)]
        code_list.append(working_line)
        working_line = ''
    for line in code_list:
        code.write(line)
    text.close()
    code.close()
    return code


def de_vernam_cipher(input_txt, output_txt, k):
    '''
    Функция, расшифровывающая шифр Вернама.
    :param input_txt: название файла, в котором лежит зашифрованный текст,
    который должна расшифровать функция
    :param output_txt: название файла, в котором будет лежать расшифрованный
    текст
    :param k: слово, являющееся ключом шифрования
    '''

    code = open(input_txt, 'r')
    text = open(output_txt, 'w')

    code_list = code.readlines()
    working_line = ''
    text_list = []
    all_str = ''

    k = k.lower()

    for i, line in enumerate(code_list):
        if i < len(code_list) - 1:
            all_str += line[:-1] + ' '
            print('')
        elif i == len(code_list) - 1:
            all_str += line

    i = 0
    j = 0
    key = ''
    while i < len(all_str):
        if all_str[i] in Globals.a:
            key += k[j]
            i += 1
            j += 1
        elif all_str[i] not in Globals.a:
            key += Globals.random_letter
            i += 1
    for line in code_list:
        line = line.lower()
        for i, l in enumerate(line):
            if l not in Globals.a:
                working_line += l
            else:
                working_line += Globals.a[
                    (Globals.a.find(l) - Globals.a.find(key[i])) % len(
                        Globals.a)]
        text_list.append(working_line)
        working_line = ''
    for line in text_list:
        text.write(line)
    text.close()
    code.close()
    return text


def morse_code(input_txt, output_txt):
    '''
    Функция, зашифровывающая текст азбукой Морзе.
    :param input_txt: название файла, в котором лежит текст, который должна
    зашифровать функция
    :param output_txt: название файла, в котором будет лежать зашифрованный
    текст
    '''

    text = open(input_txt, 'r')
    code = open(output_txt, 'w')

    text_list = text.readlines()
    working_line = ''
    code_list = []

    for line in text_list:
        line = line.lower()
        for l in line:
            if l not in Globals.morse.keys():
                working_line += l
            else:
                working_line = working_line + Globals.morse[l] + ' '
        code_list.append(working_line)
        working_line = ''
    for line in code_list:
        code.write(line)
    text.close()
    code.close()
    return code


def de_morse_code(input_txt, output_txt):
    '''
    Функция, расфровывающая текст азбукой Морзе.
    :param input_txt: название файла, в котором лежит зашифрованный текст,
    который должна расшифровать функция
    :param output_txt: название файла, в котором будет лежать расшифрованный
    текст
    '''

    reversed_morse = {}

    for key, value in Globals.morse.items():
        reversed_morse[value] = key

    code = open(input_txt, 'r')
    text = open(output_txt, 'w')

    code_list = code.readlines()
    working_line = ''
    text_list = []

    for line in code_list:
        words = line.split('  ')
        for word in words:
            letters = word.split()
            for l in letters:
                if l not in reversed_morse.keys():
                    working_line += l
                else:
                    working_line = working_line + reversed_morse[l]
            working_line += ' '
        working_line += '\n'
        text_list.append(working_line)
        working_line = ''
    for line in text_list:
        text.write(line)
    text.close()
    code.close()
    return text
