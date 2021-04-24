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
    forward_step = 1
    back_step = -1
    random_letter = 'a'
    BMP_HEADER_SIZE = 54

    divide_by_two = 2
    to_window_center_width = 340
    to_window_center_high = 260

    bits = 8
    last_byte = 0b00000000
    text_mask = 0b11111111
    img_mask = 0b11111111
    step = 1
    first_bit = 0
    last_bit = 8
    empty_value = 0
    number_of_bits = 256