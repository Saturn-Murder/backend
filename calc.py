from tkinter import *


def calculator(root: Tk):
    root.title("Calc")
    root.geometry("262x338")

    frame = Frame(root)
    frame.pack()

    label = Label(frame, text="0", font="Arial", bg="white", width=28)
    label.grid(row=0, column=0, columnspan=4)

    string_var = StringVar()
    string_var.set("0")

    def append(char):
        if string_var.get() == "0":
            string_var.set(char)
        else:
            string_var.set(string_var.get() + char)
        update_label()

    def update_label():
        label.config(text=string_var.get())

    def clear():
        string_var.set("0")
        update_label()

    def evaluate():
        try:
            res = eval(string_var.get())
            string_var.set(str(res))
        except ZeroDivisionError:
            string_var.set("Error")
        update_label()

    button_1 = Button(frame, text="1", font=("Arial", 15), command=lambda: append("1"))
    button_2 = Button(frame, text="2", font=("Arial", 15), command=lambda: append("2"))
    button_3 = Button(frame, text="3", font=("Arial", 15), command=lambda: append("3"))
    button_4 = Button(frame, text="4", font=("Arial", 15), command=lambda: append("4"))
    button_5 = Button(frame, text="5", font=("Arial", 15), command=lambda: append("5"))
    button_6 = Button(frame, text="6", font=("Arial", 15), command=lambda: append("6"))
    button_7 = Button(frame, text="7", font=("Arial", 15), command=lambda: append("7"))
    button_8 = Button(frame, text="8", font=("Arial", 15), command=lambda: append("8"))
    button_9 = Button(frame, text="9", font=("Arial", 15), command=lambda: append("9"))
    button_0 = Button(frame, text="0", font=("Arial", 15), command=lambda: append("0"))
    button_plus = Button(frame, text="+", font=("Arial", 15), command=lambda: append("+"))
    button_minus = Button(frame, text="-", font=("Arial", 15), command=lambda: append("-"))
    button_multiply = Button(frame, text="*", font=("Arial", 15), command=lambda: append("*"))
    button_divide = Button(frame, text="/", font=("Arial", 15), command=lambda: append("/"))
    button_equals = Button(frame, text="=", font=("Arial", 15), command=evaluate)
    button_point = Button(frame, text=".", font=("Arial", 15), command=lambda: append("."))
    button_clear = Button(frame, text="C", font=("Arial", 15), command=clear)

    button_1.grid(row=1, column=0)
    button_2.grid(row=1, column=1)
    button_3.grid(row=1, column=2)
    button_plus.grid(row=1, column=3)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_minus.grid(row=2, column=3)
    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)
    button_multiply.grid(row=3, column=3)
    button_point.grid(row=4, column=0)
    button_0.grid(row=4, column=1)
    button_equals.grid(row=4, column=2)
    button_divide.grid(row=4, column=3)
    button_clear.grid(row=5, column=0, columnspan=4)

    button_1.config(width=5, height=2)
    button_2.config(width=5, height=2)
    button_3.config(width=5, height=2)
    button_4.config(width=5, height=2)
    button_5.config(width=5, height=2)
    button_6.config(width=5, height=2)
    button_7.config(width=5, height=2)
    button_8.config(width=5, height=2)
    button_9.config(width=5, height=2)
    button_0.config(width=5, height=2)
    button_plus.config(width=5, height=2)
    button_minus.config(width=5, height=2)
    button_multiply.config(width=5, height=2)
    button_divide.config(width=5, height=2)
    button_equals.config(width=5, height=2)
    button_point.config(width=5, height=2)
    button_clear.config(width=23, height=2)

    root.bind("<Escape>", lambda event: root.destroy())
    root.bind("<Return>", lambda event: evaluate())
    root.bind("<BackSpace>", lambda event: clear())
    root.bind("1", lambda event: append("1"))
    root.bind("2", lambda event: append("2"))
    root.bind("3", lambda event: append("3"))
    root.bind("4", lambda event: append("4"))
    root.bind("5", lambda event: append("5"))
    root.bind("6", lambda event: append("6"))
    root.bind("7", lambda event: append("7"))
    root.bind("8", lambda event: append("8"))
    root.bind("9", lambda event: append("9"))
    root.bind("0", lambda event: append("0"))
    root.bind("+", lambda event: append("+"))
    root.bind("-", lambda event: append("-"))
    root.bind("*", lambda event: append("*"))
    root.bind("/", lambda event: append("/"))
    root.bind(".", lambda event: append("."))
    root.bind("=", lambda event: evaluate())
    root.bind("C", lambda event: clear())


if __name__ == '__main__':
    root = Tk()
    calculator(root)
    root.mainloop()
