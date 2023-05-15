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

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                button = tk.Button(
                    self.master, text=button_text, width=5, height=3, font=("Helvetica", 20),
                    command=lambda text=button_text: self.click(text)
                )
                button.grid(row=i + 1, column=j, sticky="nsew")
            self.master.rowconfigure(i + 1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=1)
                
        # maak click def

        def click(self, button_text):
            if button_text == '=':
                try:
                    result = str(eval(self.total.get()))
                    self.total.set(result)
                except:
                    self.total.set("ERROR")

            elif button_text == 'C':
                self.total.set("")
            elif button_text == 'sin':
                try:
                    result = str(math.sin(float(self.total.get())))
                    self.total.set(result)
                except:
                    self.total.set("ERROR")

            elif button_text == 'cos':
                try:
                    result = str(math.cos(float(self.total.get())))
                    self.total.set(result)
                except:
                    self.total.set("ERROR")

            elif button_text == 'tan':
                try:
                    result = str(math.tan(float(self.total.get())))
                    self.total.set(result)
                except: 
                    self.total.set("ERROR")
            
            elif button_text == '^2':
                try:
                    result = str(float(self.total.get())**2)
                    self.total.set(result)
                except:
                    self.total.set("ERROR")

            elif button_text == 'log(x)':
                try:
                    result = math.log(float(self.entry.get()))
                    self.total.set(result)
                except:
                    self.total.set("ERROR")

            elif button_text == '1/x':
                try:
                    result = 1 / float(self.entry.get())
                    self.total.set(result)
                except:
                    self.total.set("ERROR")

            elif button_text == 'x!':
                try:
                    result = math.factorial(int(self.entry.get()))
                    self.total.set(result)
                except:
                    self.total.set("ERROR")

            elif button_text == '10^x':
                try:
                    result = 10 ** float(self.entry.get())
                    self.total.set(result)
                except:
                    self.total.set("ERROR")

            elif button_text == 'sqrt':
                try:
                    result = math.sqrt(float(self.entry.get()))
                    self.total.set(result)
                except:
                    self.total.set("ERROR")

            else:
                self.total.set(self.entry.get() + button_text)

# maak mainloop