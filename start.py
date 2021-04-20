from functions import caesar_cipher, morse_code, vegenere_cipher, vernam_cipher
from functions import de_caesar_cipher, de_morse_code, de_vegenere_cipher, \
    de_vernam_cipher
from functions import caesar_analysys


def start():
    """Функция запускает консольную версию программы и ожидает ввод всех
    необходимых параметров"""
    while True:
        choice = input(
            "en - encode, de - decode, br - breaking a caesar cipher, \
            q - quit\n")
        if choice == "q":
            break
        elif choice == "br":
            input_text = input("print the name of the file with your text\n")
            output_text = input(
                "print the name of the output file\n")
            caesar_analysys(input_text, output_text)
        else:
            cipher = input("caesar, vegenere, vernam or morse cipher\n")
            input_text = input("print the name of the file with your text\n")
            output_text = input(
                "print the name of the output file \n")

            if cipher == "caesar":
                key = int(input("print the key(shift) for coding\n"))
                if choice == "en":
                    caesar_cipher(input_text, output_text, key)
                elif choice == "de":
                    de_caesar_cipher(input_text, output_text, key)

            elif cipher == "vegenere":
                key = input("print the key word for coding\n")
                if choice == "en":
                    vegenere_cipher(input_text, output_text, key)
                elif choice == "de":
                    de_vegenere_cipher(input_text, output_text, key)

            elif cipher == "vernam":
                key = input(
                    "print the key word for coding, it length must be the \
                    same as the length of the text\n")
                if choice == "en":
                    vernam_cipher(input_text, output_text, key)
                elif choice == "de":
                    de_vernam_cipher(input_text, output_text, key)

            elif cipher == "morse":
                if choice == "en":
                    morse_code(input_text, output_text)
                elif choice == "de":
                    de_morse_code(input_text, output_text)
            else:
                print("Unknown command")
