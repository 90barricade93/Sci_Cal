# Scientific Calculator (wetenschappelijke rekenmachine)
# gebaseerd op: @rahulmallah785671 build-your-own-scientific-calculator-with-python-a-step-by-step-guide

# importeer modules
import math
import tkinter as tk

# maak calculator class
def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("312x324")

        self.total = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.total, font=("Roboto", 20))
        self.entry.grid(row=0, column=0, columnspan=5, pady=5)

        self.create_buttons()

        # maak creat button def
        def create_buttons(self):
                button_list = [
                    ['sin', 'cos', 'tan', '^2', '10^x'],
                    ['7', '8', '9', '/', 'log(x)'],
                    ['4', '5', '6', '*', '1/x'],
                    ['1', '2', '3', '-', 'x!'],
                    ['0', 'C', '=', '+', 'sqrt']
                ]

                
                
                
        # maak click def

# maak mainloop