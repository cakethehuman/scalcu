import tkinter as tk
from tkinter import *
import math
import ast
class Scalc:
    def __init__(self, calc):
        self.calc = calc
        calc.title("Cool Calc")
        calc.geometry("300x450")
        calc.configure(bg='#202020')

        self.entry = tk.Entry(calc, width=20, font=('Arial', 24))
        self.entry.place(x=0, y=50)
        canvas= Canvas(self.calc, width= 1000, height= 750, bg="SpringGreen2")
        canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))

        self.create_button("7", 0, 150)
        self.create_button("8", 50, 150)
        self.create_button("9", 100, 150)

        self.create_button("4", 0, 190)
        self.create_button("5", 50, 190)
        self.create_button("6", 100, 190)

        self.create_button("1", 0, 230)
        self.create_button("2", 50, 230)
        self.create_button("3", 100, 230)

        # Zero and decimal point buttons
        self.create_button("0", 0, 270)
        self.create_button(".", 100, 270)
        # Operator buttons on the right
        self.create_button("+", 150, 110)
        self.create_button("-", 150, 150)
        self.create_button("*", 150, 190)
        self.create_button("/", 150, 230)
        # Additional functional buttons
        self.create_button("=", 150, 270)
        self.create_button("C", 10, 380)
        self.create_button("3.1415", 80, 380)
        # Trigonometric function buttons (cos, sin, tan)
        self.create_button("sin", 0, 110)
        self.create_button("cos", 50, 110)
        self.create_button("tan", 100, 110)
        #exponents
        self.create_button("log2", 200, 110)

        self.current_expression = ""

    def create_button(self, text, x, y):
        actions = {
            "=": tk.Button(text=text, width=7, height=2, command=self.calculate, bg='#ffa500', activebackground='#ffa500'),
            "cos" : tk.Button(text=text, width=7, height=2, command=self.cos),
            "sin" : tk.Button(text=text, width=7, height=2, command=self.sin),
            "tan" : tk.Button(text=text, width=7, height=2, command=self.tan),
            "C" : tk.Button(text=text, width=7, height=2, command=self.clear_text),
            "0" : tk.Button(text=text, width=13,height=2, command= lambda : self.numbers(text)),
            "3.1415" : tk.Button(text="π", width=7,height=2, command= lambda : self.numbers(text)),
            "log2" : tk.Button(text=text, width=7,height=2, command= self.logs)
            }

        if text in actions:
            button = actions.get(text)
        else:
            button = tk.Button(text=text, width=7,height=2, command= lambda : self.numbers(text))
        button.place(x=x, y=y)
    
    #trigeo
    def cos(self):
        total = self.entry.get()
        angle = float(ast.literal_eval(total))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{(math.cos(math.radians(angle))):.3f}")

    def sin(self):
        total = int(eval(self.entry.get()))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{(math.sin(math.radians(total))):.3f}")

    def tan(self):
        total = int(eval(self.entry.get()))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{(math.tan(math.radians(total))):.3f}")
    #exponents
    def logs(self):
        log_input = int(eval(self.entry.get()))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{(math.log(log_input)):.3f}")

    #normal eq
    def numbers(self,text):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current_text + text)

    def calculate(self):
        try:
            total = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, total)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            

    def clear_text(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Scalc(root)
    root.mainloop()