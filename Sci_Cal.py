# Scientific Calculator (wetenschappelijke rekenmachine)
# gebaseerd op: @rahulmallah785671 build-your-own-scientific-calculator-with-python-a-step-by-step-guide

# importeer modules
import math
import tkinter as tk

# maak calculator class
class Calculator:
    """
    Class for a scientific calculator using tkinter
    atributen:
        master: tk.Tk
        total: tk.StringVar
        entry: tk.Entry
        buttons: list

    methoden:
        __init__(self, master: tk.Tk)
        create_buttons(self)
        click(self, button_text: str)
        


    author: Raymond de Vries
    """


    def __init__(self, master: tk.Tk) -> None:
        """
        Initializes the calculator class
        
        returns:
            None
        """
        self.master = master
        master.title("SCI_CAL - Scientific Calculator")
        master.geometry("400x600")

        self.total = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.total, font=("Roboto", 20))
        self.entry.grid(row=0, column=0, columnspan=5, pady=5)

        self.create_buttons()

        # knoppenstijl
        for button in self.master.grid_slaves():
            if button['text'] in ['=', 'sin', 'cos', 'tan', '^2', '10^x', 'log(x)', '1/x', 'x!', 'sqrt']:
                button.configure(bg="orange")
            elif button['text'] in ['C']:
                button.configure(bg="red")    
            else:
                button.configure(bg="white")


    def create_buttons(self) -> None:
        """
        Creates and arranges buttons on the calculator's GUI.
        Buttons include numbers, basic arithmetic operators, and scientific functions.
        
        returns:
            None     
        
        """
        button_list = [
            ['sin', 'cos', 'tan', '^2', '10^x'],  # Scientific functions
            ['7', '8', '9', '/', 'log(x)'],       # Numbers and operators
            ['4', '5', '6', '*', '1/x'],          # Numbers and operators
            ['1', '2', '3', '-', 'x!'],           # Numbers and operators
            ['0', 'C', '=', '+', 'sqrt']          # Numbers and operators
        ]

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                # Create a button and assign it a command to handle clicks
                button = tk.Button(
                    self.master, text=button_text, width=5, height=3, font=("Helvetica", 20),
                    command=lambda text=button_text: self.click(text)
                )
                button.grid(row=i + 1, column=j, sticky="nsew")  # Arrange the button in the grid

                # Configure rows and columns to be expandable
                for j in range(len(button_list[0])):
                    self.master.columnconfigure(j, weight=1)
                    self.master.rowconfigure(i + 1, weight=1)  # Make rows expandable
                    self.master.columnconfigure(0, weight=1)  # Make columns expandable
                    self.master.columnconfigure(1, weight=1)
                    self.master.columnconfigure(2, weight=1)
                    self.master.columnconfigure(3, weight=1)
                    self.master.columnconfigure(4, weight=1)


    def click(self, button_text: str) -> None:
        """
        Click function for the calculator buttons
        
        returns:
            None
        """
        if button_text == '=': 
            try: #
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
            self.total.set(self.entry.get() + button_text) # Append the button text to the current input


if __name__ == '__main__':
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()
