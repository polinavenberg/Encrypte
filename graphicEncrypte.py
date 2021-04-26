from globals import Globals
import tkinter
from tkinter import ttk, messagebox, filedialog
from tkinter.ttk import Combobox
import winsound
from functions import caesar_cipher, morse_code, vegenere_cipher, vernam_cipher
from functions import de_morse_code
from functions import caesar_analysys
from stegan import encrypt, decrypt

'''add1 - add6 - функции для кнопок добавления файлов'''


def add1():
    input_file = filedialog.askopenfilename()
    text_filename_1.configure(text=input_file)


def add2():
    input_file = filedialog.askopenfilename()
    text_filename_2.configure(text=input_file)


def add3():
    input_file = filedialog.askopenfilename()
    text_filename_3.configure(text=input_file)


def add4():
    input_file = filedialog.askopenfilename()
    text_filename_4.configure(text=input_file)


def add5():
    input_file = filedialog.askopenfilename()
    img_filename_5.configure(text=input_file)


def add6():
    input_file = filedialog.askopenfilename()
    text_filename_5.configure(text=input_file)


'''Функции, которые выполняется при нажатии кнопки, которая запускает
    процесс шифрования или дешифрования с использованием определенного шифра.
    Они считывают введенные данные и исходя из них запускают необходимые
    функции'''


def caesar_crypt():
    choice = choice_1.get()
    input_text = text_filename_1['text']
    output_text = output_filename_1.get()
    key = int(step_value_1.get())
    if choice == 'Crack':
        caesar_analysys(input_text, output_text)
    else:
        caesar_cipher(input_text, output_text, key, choice)

    messagebox.showinfo('Encrypte', 'Done!')


def vernam_crypt():
    choice = choice_2.get()
    input_text = text_filename_2['text']
    output_text = output_filename_2.get()
    key = key_value_2.get()
    vernam_cipher(input_text, output_text, key, choice)
    messagebox.showinfo('Encrypte', 'Done!')


def vegenere_crypt():
    choice = choice_3.get()
    input_text = text_filename_3['text']
    output_text = output_filename_3.get()
    key = key_value_3.get()
    vegenere_cipher(input_text, output_text, key, choice)
    messagebox.showinfo('Encrypte', 'Done!')


def morse_crypt():
    choice = choice_4.get()
    input_text = text_filename_4['text']
    output_text = output_filename_4.get()
    if choice == 'Encrypt':
        morse_code(input_text, output_text)
    elif choice == 'Decrypt':
        de_morse_code(input_text, output_text)
    messagebox.showinfo('Encrypte', 'Done!')


def steganography_crypt():
    choice = choice_5.get()
    input_img = img_filename_5['text']
    input_text = text_filename_5['text']
    output_name = output_filename_5.get()

    if choice == 'Encrypt':
        encrypt(input_text, input_img, output_name)
    elif choice == 'Decrypt':
        decrypt(input_img, output_name)
    messagebox.showinfo('Encrypte', 'Done!')


'''Функция, отвечающая за анимацию глаз'''


def update(ind):
    frame = frames[ind % Globals.sprite_quantity]
    ind += Globals.step
    label_1.configure(image=frame)
    label_2.configure(image=frame)
    label_3.configure(image=frame)
    label_4.configure(image=frame)
    label_5.configure(image=frame)
    tab1.after(Globals.sprite_speed, update, ind)


# создаем окно
window = tkinter.Tk()
window.title('Encrypte')
w = window.winfo_screenwidth() // Globals.divide_by_two - Globals.to_window_center_width
h = window.winfo_screenheight() // Globals.divide_by_two - Globals.to_window_center_high
window.geometry(
    '{}x{}+{}+{}'.format(Globals.window_width, Globals.window_height, w, h))
window.resizable(False, False)

frames = [tkinter.PhotoImage(file=f'eyes_sprites//e{i}.png') for i in
          range(Globals.first_image, Globals.last_image)]

# создаем вкладки
tab_control = ttk.Notebook(window)

# вкладка для шифра Цезаря
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Caesar cipher')
tab_control.pack(expand=1, fill='both')

text_about_input_1 = tkinter.Label(tab1, text='Choose the input file')
text_about_input_1.grid(column=0, row=0)
button_to_choose_input_file_1 = tkinter.Button(tab1, text='+', command=add1)
button_to_choose_input_file_1.grid(column=0, row=1)
text_filename_1 = tkinter.Label(tab1, text='')
text_filename_1.grid(column=0, row=2)

text_about_output_1 = tkinter.Label(tab1, text='Name the output file')
text_about_output_1.grid(column=1, row=0)
output_filename_1 = tkinter.Entry(tab1, width=15)
output_filename_1.grid(column=1, row=1)

choice_1 = Combobox(tab1)
choice_1['values'] = ('Encrypt', 'Decrypt', 'Crack')
choice_1.grid(column=0, row=5)

text_step_1 = tkinter.Label(tab1, text='Print step or 0 if you want to crack')
text_step_1.grid(column=1, row=4)
step_value_1 = tkinter.Entry(tab1, width=15)
step_value_1.grid(column=1, row=5)

button_to_start_1 = tkinter.Button(tab1, text='Encrypte', command=caesar_crypt)
button_to_start_1.grid(column=0, row=7, columnspan=2)

label_1 = tkinter.Label(tab1)
label_1.grid(column=0, row=10, columnspan=2)
tab1.after(0, update, 0)

# вкладка для шифра Вернама
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Vernam cipher')
tab_control.pack(expand=2, fill='both')

text_about_input_2 = tkinter.Label(tab2, text='Choose the input file')
text_about_input_2.grid(column=0, row=0)
button_to_choose_input_file_2 = tkinter.Button(tab2, text='+', command=add2)
button_to_choose_input_file_2.grid(column=0, row=1)
text_filename_2 = tkinter.Label(tab2, text='')
text_filename_2.grid(column=0, row=2)

text_about_output_2 = tkinter.Label(tab2, text='Name the output file')
text_about_output_2.grid(column=1, row=0)
output_filename_2 = tkinter.Entry(tab2, width=15)
output_filename_2.grid(column=1, row=1)

choice_2 = Combobox(tab2)
choice_2['values'] = ('Encrypt', 'Decrypt')
choice_2.grid(column=0, row=5)

text_step_2 = tkinter.Label(tab2, text='Print the key word')
text_step_2.grid(column=1, row=4)
key_value_2 = tkinter.Entry(tab2, width=15)
key_value_2.grid(column=1, row=5)

button_to_start_2 = tkinter.Button(tab2, text='Encrypte', command=vernam_crypt)
button_to_start_2.grid(column=0, row=7, columnspan=2)

# Гифка
label_2 = tkinter.Label(tab2)
label_2.grid(column=0, row=10, columnspan=2)
tab2.after(0, update, 0)

# вкладка для шифра Вижнера
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Vigenere cipher')
tab_control.pack(expand=3, fill='both')

text_about_input_3 = tkinter.Label(tab3, text='Choose the input file')
text_about_input_3.grid(column=0, row=0)
button_to_choose_input_file_3 = tkinter.Button(tab3, text='+', command=add3)
button_to_choose_input_file_3.grid(column=0, row=1)
text_filename_3 = tkinter.Label(tab3, text='')
text_filename_3.grid(column=0, row=2)

text_about_output_3 = tkinter.Label(tab3, text='Name the output file')
text_about_output_3.grid(column=1, row=0)
output_filename_3 = tkinter.Entry(tab3, width=15)
output_filename_3.grid(column=1, row=1)

choice_3 = Combobox(tab3)
choice_3['values'] = ('Encrypt', 'Decrypt')
choice_3.grid(column=0, row=5)

text_step_3 = tkinter.Label(tab3, text='Print the key word')
text_step_3.grid(column=1, row=4)
key_value_3 = tkinter.Entry(tab3, width=15)
key_value_3.grid(column=1, row=5)

button_to_start_3 = tkinter.Button(tab3, text='Encrypte',
                                   command=vegenere_crypt)
button_to_start_3.grid(column=0, row=7, columnspan=2)

label_3 = tkinter.Label(tab3)
label_3.grid(column=0, row=10, columnspan=2)
tab3.after(0, update, 0)

# вкладка для кода Морзе
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='Morse code')
tab_control.pack(expand=4, fill='both')

text_about_input_4 = tkinter.Label(tab4, text='Choose the input file')
text_about_input_4.grid(column=0, row=0)
button_to_choose_input_file_4 = tkinter.Button(tab4, text='+', command=add4)
button_to_choose_input_file_4.grid(column=0, row=1)
text_filename_4 = tkinter.Label(tab4, text='')
text_filename_4.grid(column=0, row=2)

text_about_output_4 = tkinter.Label(tab4, text='Name the output file')
text_about_output_4.grid(column=1, row=0)
output_filename_4 = tkinter.Entry(tab4, width=15)
output_filename_4.grid(column=1, row=1)

choice_4 = Combobox(tab4)
choice_4['values'] = ('Encrypt', 'Decrypt')
choice_4.grid(column=0, row=5)

button_to_start_4 = tkinter.Button(tab4, text='Encrypte', command=morse_crypt)
button_to_start_4.grid(column=0, row=7, columnspan=2)

label_4 = tkinter.Label(tab4)
label_4.grid(column=0, row=10, columnspan=2)
tab4.after(0, update, 0)

# вкладка для стеганографии
tab5 = ttk.Frame(tab_control)
tab_control.add(tab5, text='Steganography')
tab_control.pack(expand=3, fill='both')

img_about_input_5 = tkinter.Label(tab5, text='Choose the input file')
img_about_input_5.grid(column=0, row=0)
button_to_choose_input_file_5 = tkinter.Button(tab5, text='+', command=add5)
button_to_choose_input_file_5.grid(column=0, row=1)
img_filename_5 = tkinter.Label(tab5, text='')
img_filename_5.grid(column=0, row=2)

text_about_output_5 = tkinter.Label(tab5, text='Name the output file')
text_about_output_5.grid(column=1, row=0)
output_filename_5 = tkinter.Entry(tab5, width=15)
output_filename_5.grid(column=1, row=1)

choice_5 = Combobox(tab5)
choice_5['values'] = ('Encrypt', 'Decrypt')
choice_5.grid(column=0, row=5)

text_step_5 = tkinter.Label(tab5, text='Choose the text file')
text_step_5.grid(column=1, row=4)
button_to_choose_input_file_5 = tkinter.Button(tab5, text='+', command=add6)
button_to_choose_input_file_5.grid(column=1, row=5)
text_filename_5 = tkinter.Label(tab5, text='')
text_filename_5.grid(column=1, row=6)

button_to_start_5 = tkinter.Button(tab5, text='Encrypte',
                                   command=steganography_crypt)
button_to_start_5.grid(column=0, row=7, columnspan=2)

label_5 = tkinter.Label(tab5)
label_5.grid(column=0, row=10, columnspan=2)
tab5.after(0, update, 0)

winsound.PlaySound('sound_file//posmertiye.wav',
                   winsound.SND_FILENAME |
                   winsound.SND_ASYNC | winsound.SND_LOOP)

window.mainloop()
