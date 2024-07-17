from tkinter import *
def add_numbers():
    result = int(num1E.get()) + int(num2E.get())
    result_label.config(text=f"Result: {result}")
def sub_numbers():
    result = int(num1E.get()) - int(num2E.get())
    result_label.config(text=f"Result: {result}")
def multiply_numbers():
    result = int(num1E.get()) * int(num2E.get())
    result_label.config(text=f"Result: {result}")
def divide_numbers():
    result = int(num1E.get())/int(num2E.get())
    result_label.config(text=f"Result: {result}")
root = Tk()
root.title('calculator')
root.geometry("400x400")
header = Label(root, text="CALCULATOR", font=('times new roman', 15), bd=15)
header.pack()

form = Frame(root)
form.pack(side=TOP, fill=X)

num1L = Label(form, text="Enter Number 1:", font=('times new roman', 12), bd=15)
num2L = Label(form, text="Enter Number 2:", font=('times new roman', 12), bd=15)
num1L.grid(row=1, sticky=W)
num2L.grid(row=2, sticky=W)

num1E = Entry(form)
num2E = Entry(form)
num1E.grid(row=1, column=2)
num2E.grid(row=2, column=2)

add = Button(form, text="ADD", activebackground="black", activeforeground="white", command=add_numbers)
sub = Button(form, text="SUB", activebackground="black", activeforeground="white", command=sub_numbers)
multiply = Button(form, text="MULTIPLY", activebackground="black", activeforeground="white", command=multiply_numbers)
divide = Button(form, text="DIVIDE", activebackground="black", activeforeground="white", command=divide_numbers)

add.grid(row=4, column=0, padx=5, pady=10)
sub.grid(row=4, column=1, padx=5, pady=10)
multiply.grid(row=4, column=2, padx=5, pady=10)
divide.grid(row=4, column=3, padx=5, pady=10)

result_label = Label(root, text="Result: ", font=('times new roman',12), bg="lightblue", bd=15)
result_label.pack(pady=20)

root.mainloop()
