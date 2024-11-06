import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
import math
from scipy.special import cbrt
import cmath
import ast

class Scalc():
    def __init__(self, calc):
        self.calc = calc
        calc.title("Cool Calc")
        calc.geometry("300x450")
        calc.configure(bg='#28282B')
        calc.resizable(False, False)
        img = PhotoImage(file='assets\school.png')
        calc.iconphoto(False, img)

        Roboto = font.Font(family="Roboto",size=20)

        #container = calc.Frame(self)  
        #container.pack(side = "top", fill = "both", expand = FALSE) 

        self.entry = tk.Entry(calc, width=20, font=(Roboto))
        self.entry.place(x=0, y=55)

        canvas = Canvas(self.calc, width= 100, height= 1500, bg="SpringGreen2")
        canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=(Roboto))
        
        #container.grid_rowconfigure(0, weight = 1)
        #container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        #self.frames = {}  
  
        #switch pages
        self.page1 = Page1(calc, self.entry)



class Page1(tk.Frame):
    def __init__(self, calc,entry):
        super().__init__(calc)
        self.calc = calc
        self.entry = entry

        #numbers
        self.create_button("7", 50, 170)
        self.create_button("8", 100, 170)
        self.create_button("9", 150, 170)

        self.create_button("4", 50, 210)
        self.create_button("5", 100, 210)
        self.create_button("6", 150, 210)

        self.create_button("1", 50, 250)
        self.create_button("2", 100, 250)
        self.create_button("3", 150, 250)

        # Zero and decimal point buttons
        self.create_button("0", 50, 290)
        self.create_button(".", 150, 290)
        # Operator buttons on the right
        self.create_button("+", 200, 250)
        self.create_button("-", 200, 210)
        self.create_button("*", 200, 170)
        self.create_button("/", 200, 130)
        # Additional functional buttons
        self.create_button("=", 200, 290)
        self.create_button("C", 50, 130)
        self.create_button("3.1415", 0, 290)
        # Trigonometric function buttons (cos, sin, tan)
        self.create_button("sin", 50, 90)
        self.create_button("cos", 100, 90)
        self.create_button("tan", 150, 90)
        #exponents
        self.create_button("log", 200, 130)
        self.create_button("**2", 0, 210)
        self.create_button("**0.5", 0, 170)
        self.create_button("∛", 0, 130)

        self.create_button("!", 0, 250)

        #page control
        #self.create_button("Switch to Page 2", 200, 190)
        self.current_expression = ""

    def create_button(self, text, x, y):
        actions = {
            "=": tk.Button(text=text, width=7, height=2, command=self.calculate, bg='#F28C28', activebackground='#ffa500'),
            "cos" : tk.Button(text=text, width=7, height=2, command=self.cos , bg='#F28C28'),
            "sin" : tk.Button(text=text, width=7, height=2, command=self.sin, bg='#F28C28'),
            "tan" : tk.Button(text=text, width=7, height=2, command=self.tan, bg='#F28C28'),
            "C" : tk.Button(text=text, width=7, height=2, command=self.clear_text, bg = "#D70040"),
            "0" : tk.Button(text=text,width=13,height=2, command= lambda : self.numbers(text)),
            "3.1415" : tk.Button(text="π", width=6,height=2, command= lambda : self.numbers(text)),
            "log" : tk.Button(text=text, width=7,height=2, command= self.logs),
            "**2" : tk.Button(text="x²", width=6,height=2, command= lambda : self.numbers(text)),
            "**0.5": tk.Button(text="√", width=6,height=2, command= self.rot),
            "+":tk.Button(text=text,width=7,height=2,bg='#F28C28', command= lambda : self.numbers(text)),
            "!" : tk.Button(text=text, width=6, height=2, command=self.factorial, bg='#F28C28'),
            "∛" : tk.Button(text=text, width=6,height=2, command= self.root3)
            }

        if text in actions:
            button = actions.get(text)
        else:
            button = tk.Button(text=text, width=7,height=2, bg ='#FFFFFF',command= lambda : self.numbers(text))
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
    
    def rot(self):
        rot_input = int(eval(self.entry.get()))
        self.entry.delete(0, tk.END)
        the_root = cbrt(rot_input)
        self.entry.insert(0, f"{(the_root):.3f}") #fix later for imajanary countring
        #if rot_input > 0:
            #self.entry.insert(0, f"{(the_root):.1f}")
        #else:
            #self.entry.insert(0, f"{(the_root.imag):.1f}")

    def root3(self):
        rot_input = int(eval(self.entry.get()))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{cbrt(rot_input):.3f}")
            
    def factorial(self):
        n = int(eval(self.entry.get()))
        self.entry.delete(0, tk.END)
        factorail_num = math.factorial(n)
        self.entry.insert(0,factorail_num)
            

    #normal eq
    def numbers(self,text):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current_text + text)

    def calculate(self):
        try:
            total = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(0,total)#fix
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            

    def clear_text(self):
        self.entry.delete(0, tk.END)

class Page2(tk.Frame):
    def __init__(self, calc, entry):
        super().__init__(calc)
        self.entry = entry
        self.calc = calc

        label = tk.Label(self, text="Page 2", font=("Roboto", 20))
        label.pack(pady=20)

        # Button to go back to Page 1
        switch_button = tk.Button(self, text="Back to Page 1", command=lambda: calc.show_page(calc.page1))
        switch_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = Scalc(root)
    root.mainloop()