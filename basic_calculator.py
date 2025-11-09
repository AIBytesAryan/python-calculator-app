import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Create display frame
        display_frame = tk.Frame(self.root)
        display_frame.pack(pady=20)
        
        # Create display entry
        self.display = tk.Entry(display_frame, font=('Arial', 18), justify='right', 
                               bd=10, relief=tk.RIDGE, width=15)
        self.display.pack(padx=10, pady=10)
        self.display.focus()
        
        # Create buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()
        
        # Button layout
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '⌫']
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text == '=':
                    btn = tk.Button(buttons_frame, text=text, font=('Arial', 14), 
                                  width=5, height=2, bg='orange', fg='white',
                                  command=self.calculate)
                elif text == 'C':
                    btn = tk.Button(buttons_frame, text=text, font=('Arial', 14), 
                                  width=5, height=2, bg='red', fg='white',
                                  command=self.clear)
                elif text == '⌫':
                    btn = tk.Button(buttons_frame, text=text, font=('Arial', 14), 
                                  width=5, height=2, bg='lightgray',
                                  command=self.backspace)
                else:
                    btn = tk.Button(buttons_frame, text=text, font=('Arial', 14), 
                                  width=5, height=2, bg='lightblue',
                                  command=lambda t=text: self.add_to_display(t))
                
                btn.grid(row=i, column=j, padx=2, pady=2)
        
        # Bind keyboard events
        self.root.bind('<Key>', self.key_press)
        self.root.bind('<Return>', lambda event: self.calculate())
        self.root.bind('<BackSpace>', lambda event: self.backspace())
        self.root.bind('<Escape>', lambda event: self.clear())
    
    def add_to_display(self, char):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + str(char))
    
    def clear(self):
        self.display.delete(0, tk.END)
    
    def backspace(self):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current[:-1])
    
    def calculate(self):
        try:
            expression = self.display.get()
            if expression:
                # Security check - only allow safe characters
                allowed_chars = set('0123456789+-*/.() ')
                if all(char in allowed_chars for char in expression):
                    result = eval(expression)
                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                else:
                    messagebox.showerror("Error", "Invalid characters in expression")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression!")
    
    def key_press(self, event):
        key = event.char
        if key in '0123456789+-*/.()':
            self.add_to_display(key)
        elif key == '\r':  # Enter key
            self.calculate()
        elif key == '\x08':  # Backspace key
            self.backspace()

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()