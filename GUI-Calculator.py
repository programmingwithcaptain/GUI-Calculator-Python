from tkinter import *

# Window
root = Tk()
root.title("Calculator")
root.geometry("312x324")
root.resizable(0, 0)


# Click Function
def click_btn(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# Clear Function
def clear_btn():
    global expression
    expression = ""
    input_text.set("")


# Equal Function
def equal_btn():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

# Fetch Data of Input
input_text = StringVar()

# Input Frame
input_frame = Frame(root, width=312, height=50, bd=0)
input_frame.pack(side=TOP)


# Frame for Input Field
input_field = Entry(input_frame, font=("Times New Roman", 18, "bold"),
                textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


# Frame for Buttons
btns_frame = Frame(root, width=312, height=272)
btns_frame.pack()


# First Row

clear = Button(btns_frame, text = "Clear", fg = "black", width = 32, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: clear_btn()
            ).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text = "/", fg = "black", width = 10, height=3, bd=0,
            bg="#eee", cursor="hand2", command=lambda: click_btn("/")
            ).grid(row=0, column=3, padx=1, pady=1)

# Second Row 

seven = Button(btns_frame, text = "7", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("7")
            ).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text = "8", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("8")
            ).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text = "9", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("9")
            ).grid(row=1, column=2, padx=1, pady=1)

mutiply = Button(btns_frame, text = "*", fg = "black", width = 10, height=3, bd=0,
            bg="#eee", cursor="hand2", command=lambda: click_btn("*")
            ).grid(row=1, column=3, padx=1, pady=1)


# Third Row 

four = Button(btns_frame, text = "4", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("4")
            ).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text = "5", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("5")
            ).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text = "6", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("6")
            ).grid(row=2, column=2, padx=1, pady=1)

subtract = Button(btns_frame, text = "-", fg = "black", width = 10, height=3, bd=0,
            bg="#eee", cursor="hand2", command=lambda: click_btn("-")
            ).grid(row=2, column=3, padx=1, pady=1)

# fourth Row

one = Button(btns_frame, text = "1", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("1")
            ).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text = "2", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("2")
            ).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text = "3", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("3")
            ).grid(row=3, column=2, padx=1, pady=1)

addition = Button(btns_frame, text = "+", fg = "black", width = 10, height=3, bd=0,
            bg="#eee", cursor="hand2", command=lambda: click_btn("+")
            ).grid(row=3, column=3, padx=1, pady=1)


# Fifth Row
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn("0")
            ).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text = ".", fg = "black", width = 10, height=3, bd=0,
            bg="#fff", cursor="hand2", command=lambda: click_btn(".")
            ).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text = "=", fg = "black", width = 10, height=3, bd=0,
            bg="#eee", cursor="hand2", command=lambda: equal_btn()
            ).grid(row=4, column=3, padx=1, pady=1)


root.mainloop()
