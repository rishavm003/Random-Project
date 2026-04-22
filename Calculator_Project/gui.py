import tkinter as tk
from tkinter import font
import math

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Premium Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#1e1e2e")
        
        self.expression = ""
        self.display_var = tk.StringVar(value="0")
        
        # Custom Fonts
        self.display_font = font.Font(family="Helvetica", size=32, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=14, weight="bold")
        
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        # Display Area
        self.display_frame = tk.Frame(self.root, bg="#1e1e2e", pady=20)
        self.display_frame.pack(fill="both")

        self.display_label = tk.Label(
            self.display_frame, textvariable=self.display_var,
            font=self.display_font, fg="#cdd6f4", bg="#1e1e2e",
            anchor="e", padx=20
        )
        self.display_label.pack(fill="both", expand=True)

        # Buttons Grid Area
        self.buttons_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Button Layout
        buttons = [
            ('C', 1, 0, "#f38ba8"), ('/', 1, 3, "#fab387"),
            ('7', 2, 0, "#313244"), ('8', 2, 1, "#313244"), ('9', 2, 2, "#313244"), ('*', 2, 3, "#fab387"),
            ('4', 3, 0, "#313244"), ('5', 3, 1, "#313244"), ('6', 3, 2, "#313244"), ('-', 3, 3, "#fab387"),
            ('1', 4, 0, "#313244"), ('2', 4, 1, "#313244"), ('3', 4, 2, "#313244"), ('+', 4, 3, "#fab387"),
            ('0', 5, 0, "#313244"), ('.', 5, 1, "#313244"), ('=', 5, 2, "#a6e3a1")
        ]

        # Configure weights for grid
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.buttons_frame.rowconfigure(i, weight=1)

        for (text, row, col, color) in buttons:
            colspan = 1
            if text == '0': colspan = 1 # Keeping it simple first
            if text == '=': colspan = 2 # Make equals bigger

            btn = tk.Button(
                self.buttons_frame, text=text, font=self.button_font,
                bg=color, fg="#1e1e2e" if color != "#313244" else "#cdd6f4",
                activebackground="#45475a", borderwidth=0, cursor="hand2",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("0")
        elif char == '=':
            self.calculate()
        else:
            if self.display_var.get() == "0" and char.isdigit():
                self.expression = char
            else:
                self.expression += str(char)
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            # Replace visual symbols with python operators
            exp = self.expression.replace('*', '*').replace('/', '/')
            result = eval(exp)
            # Handle float display
            if result == int(result):
                result = int(result)
            self.display_var.set(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            self.display_var.set("Error: Div/0")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

    def bind_keys(self):
        self.root.bind("<Key>", self.handle_keypress)

    def handle_keypress(self, event):
        key = event.char
        if key.isdigit() or key in ['+', '-', '*', '/', '.']:
            self.on_button_click(key)
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == "Escape" or event.keysym == "BackSpace":
            self.on_button_click('C')

if __name__ == "__main__":
    root = tk.Tk()
    # Centering
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    win_w, win_h = 400, 600
    x = (screen_w // 2) - (win_w // 2)
    y = (screen_h // 2) - (win_h // 2)
    root.geometry(f"{win_w}x{win_h}+{x}+{y}")
    
    app = CalculatorGUI(root)
    root.mainloop()
