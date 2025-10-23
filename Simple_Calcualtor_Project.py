import tkinter
from tkinter import *

# Window Setup 
root = Tk()
root.title("Simple Calculator")
root.geometry("570x700+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

# Functions 
def show(value):
    global equation
    equation += value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def delete():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)
    
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

# Display Frame
display_frame = Frame(root, bg="#222831", bd=4, relief="ridge")
display_frame.pack(pady=15)

label_result = Label(display_frame, width=25, height=2, text="", font=("arial", 30), bg="#393E46", fg="#00FFDD", anchor="e", padx=10)
label_result.pack(padx=10, pady=10)

# Buttons 
Button(root, text="C", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#d7156d", command=clear).place(x=10, y=160)
Button(root, text="/", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=150, y=160)
Button(root, text="%", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=290, y=160)
Button(root, text="⌫", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#f57c00", command=delete).place(x=430, y=160)

Button(root, text="7", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=260)
Button(root, text="8", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=260)
Button(root, text="9", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=260)
Button(root, text="-", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=260)

Button(root, text="4", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=360)
Button(root, text="5", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=360)
Button(root, text="6", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=360)
Button(root, text="+", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=360)

Button(root, text="1", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=460)
Button(root, text="2", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=460)
Button(root, text="3", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=460)
Button(root, text="*", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")) .place(x=430, y=460)

Button(root, text="0", width=11, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=560)
Button(root, text=".", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=560)
Button(root, text="=", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#9d09c2", command=calculate).place(x=430, y=560)

# Run the App
root.mainloop()
