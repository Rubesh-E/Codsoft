import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
# creating functions for the operations
def generate_password():
    password_entry.delete(0,END)
    length = var_1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*_"
    password_output = ""
    if var.get() == 1:
        for i in range(0, length):
            password_output = password_output + random.choice(lower)
        return password_output

    elif var.get() == 0:
        for i in range(0, length):
            password_output = password_output + random.choice(upper)
        return password_output

    elif var.get() == 3:
        for i in range(0, length):
            password_output = password_output + random.choice(digits)
        return password_output

    else:
        print("select valid option!!!")


def generate():
    password1 = generate_password()
    password_entry.insert(10, password1)


def copy():
    copy_password = password_entry.get()
    pyperclip.copy(copy_password)


# making GUI of the generator
root = Tk()
var = IntVar()
var_1 = IntVar()

root.title("Password Generator")
password = Label(root, text="Password")
password.grid(row=0)
password_entry = Entry(root)
password_entry.grid(row=0, column=1)
pass_length = Label(root, text="Length")
pass_length.grid(row=1)

copy_button = Button(root, text="Copy", command=copy)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

radio_low = Radiobutton(root, text="low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky="E")
radio_medium = Radiobutton(root, text="medium", variable=var, value=0)
radio_medium.grid(row=1, column=3, sticky="E")
radio_high = Radiobutton(root, text="high", variable=var, value=3)
radio_high.grid(row=1, column=4, sticky="E")

combo = Combobox(root, textvariable=var_1)
combo['values'] = (5, 6, 7, 8, 9, 10, 11, "Length")
combo.current(0)
combo.grid(row=1, column=1)

root.mainloop()
