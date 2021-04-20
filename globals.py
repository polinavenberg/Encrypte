import string


class Globals:
    alphabet = string.ascii_lowercase
    morse = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•',
             'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••',
             'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•',
             'o': '———', 'p': '•——•', 'q': '——•—',
             'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—',
             'w': '•——', 'x': '—••—', 'y': '—•——',
             'z': '——••'}
    degree = 2
    most_common_letter = 'e'
    random_letter = 'a'
    BMP_HEADER_SIZE = 54
