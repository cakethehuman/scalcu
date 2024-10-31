import tkinter as tk
from tkinter import *
import math
class Scalc:
    def __init__(self, calc):
        self.calc = calc
        calc.title("Cool Calc")
        calc.geometry("350x450")
        calc.configure(bg='lightblue')

        self.entry = tk.Entry(calc, width=20, font=('Arial', 24))
        self.entry.place(x=0, y=50)
        canvas= Canvas(self.calc, width= 1000, height= 750, bg="SpringGreen2")
        canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))

        self.create_button("+", 200, 250)
        self.create_button("-", 200, 290)
        self.create_button("*", 200, 325)
        self.create_button("/", 200, 360)
        self.create_button("7", 0, 250)   
        self.create_button("8", 50, 250)  
        self.create_button("9", 100, 250) 
        self.create_button("4", 0, 290)   
        self.create_button("5", 50, 290)  
        self.create_button("6", 100, 290) 
        self.create_button("3", 0, 325)   
        self.create_button("2", 50, 325)  
        self.create_button("1", 100, 325)
        self.create_button("0", 0, 360)
        self.create_button("=", 250, 400)
        self.create_button("C", 0, 210)
        self.create_button("cos", 300, 360)
        self.create_button("cos", 300, 360)
        self.create_button("cos", 300, 360)

        self.current_expression = ""

    
    def create_button(self, text, x, y):
        actions = {
            "=": tk.Button(text=text, width=7, height=2, command=self.calculate),
            "cos" : tk.Button(text=text, width=7, height=2, command=self.cos),
            "sin" : tk.Button(text=text, width=7, height=2, command=self.sin),
            "tan" : tk.Button(text=text, width=7, height=2, command=self.tan),
            "C" : tk.Button(text=text, width=7, height=2, command=self.clear_text),
            "0" : tk.Button(text=text, width=13,height=2, command= lambda : self.numbers(text))
            }

        if text in actions:
            button = actions.get(text)
        else:
            button = tk.Button(text=text, width=7,height=2, command= lambda : self.numbers(text))
        button.place(x=x, y=y)

    def cos(self):
        total = int(eval(self.entry.get()))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{(math.cos(math.radians(total))):.3f}")

    def sin(self):
        total = int(eval(self.entry.get()))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{(math.sin(math.radians(total))):.3f}")

    def tan(self):
        total = int(eval(self.entry.get()))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{(math.tan(math.radians(total))):.3f}")

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