import collections


def caesar_cipher(input_txt, output_txt, step):
    """Функция, создающая шифр Цезаря. На вход функции подается название файла, в котором лежит текст,
    который должна зашифровать функция; название файла, в котором будет лежать зашифрованный текст и число,
    являющееся шагом шифрования"""

    text = open(input_txt, 'r')
    code = open(output_txt, 'w')

    text_list = text.readlines()
    working_line = ''
    code_list = []

    a = 'abcdefghijklmnopqrstuvwxyz'

    for line in text_list:
        line = line.lower()
        for l in line:
            if l not in a:
                working_line += l
            else:
                working_line += a[(a.find(l) + step) % len(a)]
        code_list.append(working_line)
        working_line = ''
    for line in code_list:
        code.write(line)
    text.close()
    code.close()
    return code


def de_caesar_cipher(input_txt, output_txt, step):
    """Функция, расшифровывающая шифр Цезаря. На вход функции подается название файла, в котором лежит зашифрованный текст,
    который должна расшифровать функция; название файла, в котором будет лежать расшифрованный текст и число,
    являющееся шагом шифрования """

    code = open(input_txt, 'r')
    text = open(output_txt, 'w')

    code_list = code.readlines()
    working_line = ''
    text_list = []

    a = 'abcdefghijklmnopqrstuvwxyz'

    for line in code_list:
        line = line.lower()
        for l in line:
            if l not in a:
                working_line += l
            else:
                working_line += a[(a.find(l) - step) % len(a)]
        text_list.append(working_line)
        working_line = ''
    for line in text_list:
        text.write(line)
    text.close()
    code.close()
    return text


def caesar_analysys(input_txt, output_txt):
    """Фуекция, которая взламывает шифр Цезар методом анализа частоты вхождений букв англиского алфавита
    в зашифрованный текст. На вход программе подается название файла, в котором лежит зашифрованный текст и
    название файла, в котором будет лежать взломанный текст. Функция не работает для коротких текстов."""

    code = open(input_txt, 'r')

    code_list = code.readlines()

    all_letters = ''

    a = 'abcdefghijklmnopqrstuvwxyz'

    for line in code_list:
        line = line.lower()
        for l in line:
            if l in a:
                all_letters += l

    most_common_element = collections.Counter(all_letters).most_common(1)[0][0]
    # e - буква английского алфавита, которая встречается в тексте чаще всех остальных
    key = a.find(most_common_element) - a.find('e')

    code.close()
    return de_caesar_cipher(input_txt, output_txt, key)


def vegenere_cipher(input_txt, output_txt, k):
    """Функция, создающая шифр Виженера. На вход функции подается название файла, в котором лежит текст,
    который должна зашифровать функция; название файла, в котором будет лежать зашифрованный текст и слово,
    являющееся ключом шифрования"""

    text = open(input_txt, 'r')
    code = open(output_txt, 'w')

    text_list = text.readlines()
    working_line = ''
    code_list = []
    all_str = ''

    a = 'abcdefghijklmnopqrstuvwxyz'

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
        if all_str[i] in a:
            key += k[j % len(k)]
            i += 1
            j += 1
        elif all_str[i] not in a:
            key += 'a'
            i += 1

    for line in text_list:
        line = line.lower()
        for i, l in enumerate(line):
            if l not in a:
                working_line += l
            else:
                working_line += a[(a.find(l) + a.find(key[i])) % len(a)]
        code_list.append(working_line)
        working_line = ''
    for line in code_list:
        code.write(line)
    text.close()
    code.close()
    return code


def de_vegenere_cipher(input_txt, output_txt, k):
    """Функция, расшифровывающая шифр Виженера. На вход функции подается название файла, в котором лежит зашифрованный
        текст, который должна расшифровать функция; название файла, в котором будет лежать расшифрованный текст и слово,
        являющееся ключом шифрования """

    code = open(input_txt, 'r')
    text = open(output_txt, 'w')

    code_list = code.readlines()
    working_line = ''
    text_list = []
    all_str = ''

    a = 'abcdefghijklmnopqrstuvwxyz'

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
        if all_str[i] in a:
            key += k[j % len(k)]
            i += 1
            j += 1
        elif all_str[i] not in a:
            key += 'a'
            i += 1

    for line in code_list:
        line = line.lower()
        for i, l in enumerate(line):
            if l not in a:
                working_line += l
            else:
                working_line += a[(a.find(l) - a.find(key[i])) % len(a)]
        text_list.append(working_line)
        working_line = ''
    for line in text_list:
        text.write(line)
    text.close()
    code.close()
    return text


def vernam_cipher(input_txt, output_txt, k):
    """Функция, создающая шифр Вернама. На вход функции подается название файла, в котором лежит текст,
        который должна зашифровать функция; название файла, в котором будет лежать зашифрованный текст и слово,
        являющееся ключом шифрования"""

    text = open(input_txt, 'r')
    code = open(output_txt, 'w')

    text_list = text.readlines()
    working_line = ''
    code_list = []
    all_str = ''

    a = 'abcdefghijklmnopqrstuvwxyz'

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
        if all_str[i] in a:
            key += k[j]
            i += 1
            j += 1
        elif all_str[i] not in a:
            key += 'a'
            i += 1
    for line in text_list:
        line = line.lower()
        for i, l in enumerate(line):
            if l not in a:
                working_line += l
            else:
                working_line += a[(a.find(l) + a.find(key[i])) % len(a)]
        code_list.append(working_line)
        working_line = ''
    for line in code_list:
        code.write(line)
    text.close()
    code.close()
    return code


def de_vernam_cipher(input_txt, output_txt, k):
    """Функция, расшифровывающая шифр Вернама. На вход функции подается название файла, в котором лежит зашифрованный
        текст, который должна расшифровать функция; название файла, в котором будет лежать расшифрованный текст и
        слово, являющееся ключом шифрования """

    code = open(input_txt, 'r')
    text = open(output_txt, 'w')

    code_list = code.readlines()
    working_line = ''
    text_list = []
    all_str = ''

    a = 'abcdefghijklmnopqrstuvwxyz'

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
        if all_str[i] in a:
            key += k[j]
            i += 1
            j += 1
        elif all_str[i] not in a:
            key += 'a'
            i += 1
    for line in code_list:
        line = line.lower()
        for i, l in enumerate(line):
            if l not in a:
                working_line += l
            else:
                working_line += a[(a.find(l) - a.find(key[i])) % len(a)]
        text_list.append(working_line)
        working_line = ''
    for line in text_list:
        text.write(line)
    text.close()
    code.close()
    return text


def morse_code(input_txt, output_txt):
    """Функция, зашифровывающая текст азбукой Морзе. На вход функции подается название файла, в котором лежит текст,
        который должна зашифровать функция и название файла, в котором будет лежать зашифрованный текст"""

    morse = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••',
             'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—',
             'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——',
             'z': '——••'}

    text = open(input_txt, 'r')
    code = open(output_txt, 'w')

    text_list = text.readlines()
    working_line = ''
    code_list = []

    for line in text_list:
        line = line.lower()
        for l in line:
            if l not in morse.keys():
                working_line += l
            else:
                working_line = working_line + morse[l] + ' '
        code_list.append(working_line)
        working_line = ''
    for line in code_list:
        code.write(line)
    text.close()
    code.close()
    return code


def de_morse_code(input_txt, output_txt):
    """Функция, расфровывающая текст азбукой Морзе. На вход функции подается название файла, в котором лежит
        зашифрованный текст, который должна расшифровать функция и название файла, в котором будет лежать
        расшифрованный текст"""

    morse = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••',
             'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—',
             'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——',
             'z': '——••'}
    reversed_morse = {}

    for key, value in morse.items():
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
