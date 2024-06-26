from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("425x435+500+100")

exp = StringVar()
res = StringVar()
expression = ""

def num_click(n):
    global expression
    expression += str(n)
    exp.set(expression)

def clear():
    global expression
    expression = ""
    exp.set("")
    res.set("")

def calculate():
    try:
        global expression
        total = str(eval(expression))
        res.set(total)
        expression = total
    except Exception as e:
        res.set("Error")
        expression = ""

# Create the main window
entry_frame = Frame(root)
entry_frame.pack(pady=10)

entry = Entry(entry_frame, textvariable=exp, font=('Arial', 18), bd=5, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0)

result_entry = Entry(entry_frame, textvariable=res, font=('Arial', 18), bd=5, insertwidth=2, width=14, borderwidth=4, state='readonly')
result_entry.grid(row=1, column=0)

button_frame = Frame(root)
button_frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = Button(button_frame, text=text, padx=20, pady=20, command=calculate)
    else:
        button = Button(button_frame, text=text, padx=20, pady=20, command=lambda t=text: num_click(t))
    button.grid(row=row, column=col)

clear_button = Button(button_frame, text='C', padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

root.mainloop()