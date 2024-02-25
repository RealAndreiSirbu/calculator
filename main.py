import tkinter as tk
from math import pi, sin, cos, tan, asin, acos, atan, sqrt

window = tk.Tk()
window.title("Calculator")

font = ('Segoe UI', 16)

menubar = tk.Menu()

mode_menu = tk.Menu(menubar, tearoff=False)

equation = tk.StringVar()
equation_entry = tk.Entry(window, textvariable=equation, width=20, font=font)
equation_entry.place(x=0, y=0)

button_clear = tk.Button(window, text=' clear ', font=font, command=lambda: equation_entry.delete(0, len(equation.get())))
button_clear.place(x=0, y=int(equation_entry.place_info()['y']) + equation_entry.winfo_reqheight())

button_backspace = tk.Button(window, text=' ⇐ ', font=font, command=lambda: equation_entry.delete(len(equation.get()) - 1))
button_backspace.place(x=int(button_clear.place_info()['x']) + button_clear.winfo_reqwidth(), y=int(equation_entry.place_info()['y']) + equation_entry.winfo_reqheight())

button_square_root = tk.Button(window, text=' √ ', font=font, command=lambda: button_insert('sqrt('))
button_square_root.place(x=int(button_backspace.place_info()['x']) + button_backspace.winfo_reqwidth(), y=int(equation_entry.place_info()['y']) + equation_entry.winfo_reqheight())

# Appends the provided insertion to the equation.
def button_insert(insertion):
    equation_entry.insert(len(equation.get()), insertion)

button_7 = tk.Button(window, text='  7  ', font=font, command=lambda: button_insert('7'))
button_7.place(x=0, y=int(button_clear.place_info()['y']) + button_clear.winfo_reqheight())

button_8 = tk.Button(window, text='  8  ', font=font, command=lambda: button_insert('8'))
button_8.place(x=int(button_7.place_info()['x']) + button_7.winfo_reqwidth(), y=int(button_clear.place_info()['y']) + button_clear.winfo_reqheight())

button_9 = tk.Button(window, text='  9  ', font=font, command=lambda: button_insert('9'))
button_9.place(x=int(button_8.place_info()['x']) + button_8.winfo_reqwidth(), y=int(button_clear.place_info()['y']) + button_clear.winfo_reqheight())

button_4 = tk.Button(window, text='  4  ', font=font, command=lambda: button_insert('4'))
button_4.place(x=0, y=int(button_7.place_info()['y']) + button_7.winfo_reqheight())

button_5 = tk.Button(window, text='  5  ', font=font, command=lambda: button_insert('5'))
button_5.place(x=int(button_4.place_info()['x']) + button_4.winfo_reqwidth(), y=int(button_8.place_info()['y']) + button_8.winfo_reqheight())

button_6 = tk.Button(window, text='  6  ', font=font, command=lambda: button_insert('6'))
button_6.place(x=int(button_5.place_info()['x']) + button_5.winfo_reqwidth(), y=int(button_9.place_info()['y']) + button_9.winfo_reqheight())

button_1 = tk.Button(window, text='  1  ', font=font, command=lambda: button_insert('1'))
button_1.place(x=0, y=int(button_4.place_info()['y']) + button_4.winfo_reqheight())

button_2 = tk.Button(window, text='  2  ', font=font, command=lambda: button_insert('2'))
button_2.place(x=int(button_1.place_info()['x']) + button_1.winfo_reqwidth(), y=int(button_5.place_info()['y']) + button_5.winfo_reqheight())

button_3 = tk.Button(window, text='  3  ', font=font, command=lambda: button_insert('3'))
button_3.place(x=int(button_2.place_info()['x']) + button_2.winfo_reqwidth(), y=int(button_6.place_info()['y']) + button_6.winfo_reqheight())

button_0 = tk.Button(window, text='  0  ', font=font, command=lambda: button_insert('0'))
button_0.place(x=0, y=int(button_1.place_info()['y']) + button_1.winfo_reqheight())

button_decimal_point = tk.Button(window, text=' . ', font=font, command=lambda: button_insert('.'))
button_decimal_point.place(x=int(button_0.place_info()['x']) + button_0.winfo_reqwidth(), y=int(button_2.place_info()['y']) + button_2.winfo_reqheight())

def evaluate():
    temp = equation.get()
    equation_entry.delete(0, len(equation.get()))
    equation_entry.insert(0, str(eval(temp)))

button_equals = tk.Button(window, text=' = ', font=font, command=evaluate)
button_equals.place(x=int(button_decimal_point.place_info()['x']) + button_decimal_point.winfo_reqwidth(), y=int(button_3.place_info()['y']) + button_3.winfo_reqheight())

button_left_bracket = tk.Button(window, text=' ( ', font=font, command=lambda: button_insert('('))
button_left_bracket.place(x=int(button_equals.place_info()['x']) + button_equals.winfo_reqwidth(), y=int(button_3.place_info()['y']) + button_3.winfo_reqheight())

button_right_bracket = tk.Button(window, text=' ) ', font=font, command=lambda: button_insert(')'))
button_right_bracket.place(x=int(button_left_bracket.place_info()['x']) + button_left_bracket.winfo_reqwidth(), y=int(button_3.place_info()['y']) + button_3.winfo_reqheight())

button_plus = tk.Button(window, text=' + ', font=font, command=lambda: button_insert('+'))
button_plus.place(x=int(button_square_root.place_info()['x']) + button_square_root.winfo_reqwidth(), y=int(equation_entry.place_info()['y']) + equation_entry.winfo_reqheight())

button_minus = tk.Button(window, text=' - ', font=font, command=lambda: button_insert('-'))
button_minus.place(x=int(button_9.place_info()['x']) + button_9.winfo_reqwidth(), y=int(button_plus.place_info()['y']) + button_plus.winfo_reqheight())

button_multiply = tk.Button(window, text=' * ', font=font, command=lambda: button_insert('*'))
button_multiply.place(x=int(button_6.place_info()['x']) + button_6.winfo_reqwidth(), y=int(button_minus.place_info()['y']) + button_minus.winfo_reqheight())

button_divide = tk.Button(window, text=' / ', font=font, command=lambda: button_insert('/'))
button_divide.place(x=int(button_3.place_info()['x']) + button_3.winfo_reqwidth(), y=int(button_multiply.place_info()['y']) + button_multiply.winfo_reqheight())

width = int(equation_entry.place_info()['x']) + equation_entry.winfo_reqwidth()
height = int(button_equals.place_info()['y']) + button_equals.winfo_reqheight()

def scientific_mode():
    # TODO: Increase the window's size and add more buttons.
    print('Scientific mode enabled.')

mode_menu.add_command(label='Basic')
mode_menu.add_command(label='Scientific', command=lambda: scientific_mode())

window.geometry(f'{width}x{height}')

menubar.add_cascade(menu=mode_menu, label='Mode')
window.config(menu=menubar)

window.mainloop()
