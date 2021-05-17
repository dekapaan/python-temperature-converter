from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('800x600')
root.config(bg='#f7b32b')

c_f_frame = Frame(root, width=300, height=200, bg='#333')
c_f_frame.place(x=80, y=50)
f_c_frame = Frame(root, width=300, height=200, bg='#333')
f_c_frame.place(x=420, y=50)

c_f_label = Label(c_f_frame, text='Celsius to Fahrenheit', bg='#333', fg='white')
c_f_label.place(x=10, y=10)
f_c_label = Label(f_c_frame, text='Fahrenheit to Celsius', bg='#333', fg='white')
f_c_label.place(x=10,y=10)

c_f_entry = Entry(c_f_frame, state='readonly')
c_f_entry.place(x=70, y=100)
f_c_entry = Entry(f_c_frame, state='readonly')
f_c_entry.place(x=70, y=100)


def c_f_activation():
    c_f_entry.config(state='normal')
    f_c_entry.config(state='normal')
    f_c_entry.delete(0, END)
    f_c_entry.config(state='readonly')


def f_c_activation():
    f_c_entry.config(state='normal')
    c_f_entry.config(state='normal')
    c_f_entry.delete(0, END)
    c_f_entry.config(state='readonly')


c_f_activate = Button(root, text='Activate - Celsius to fahrenheit', command=c_f_activation)
c_f_activate.place(x=115, y=270)
f_c_activate = Button(root, text='Activate - Fahrenheit to Celsius', command=f_c_activation)
f_c_activate.place(x=455, y=270)


def conversion():
    # Clears result label
    calc_label.config(text='')
    # Celsius to Fahrenheit
    if c_f_entry['state'] == 'normal':
        c_temp = float(c_f_entry.get())
        f_result = round((c_temp * (9/5)) + 32, 1)
        calc_label.config(text=str(f_result))
    # Fahrenheit to Celsius
    elif f_c_entry['state'] == 'normal':
        f_temp = float(f_c_entry.get())
        c_result = round((f_temp-32)*(5/9), 1)
        calc_label.config(text=str(c_result))


calc = Button(root, text='Calculate Conversion', command=conversion)
calc.place(x=200, y=350)
calc_label = Label(root, width=20, height=2, bg='#333', fg='white')
calc_label.place(x=420, y=350)


def delete():
    c_f_entry.config(state='normal')
    f_c_entry.config(state='normal')
    calc_label.config(text='')
    c_f_entry.delete(0, END)
    f_c_entry.delete(0, END)
    f_c_entry.config(state='readonly')
    c_f_entry.config(state='readonly')


clear = Button(root, text='Clear', command=delete)
clear.place(x=550, y=500)
escape = Button(root, text='Exit', command='exit')
escape.place(x=650, y=500)
root.mainloop()
