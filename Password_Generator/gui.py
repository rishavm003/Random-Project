import tkinter as tk
from tkinter import font, messagebox
import random
import string

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("450x600")
        self.root.configure(bg="#1e1e2e")
        
        # State variables
        self.length_var = tk.IntVar(value=12)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        self.password_var = tk.StringVar(value="")
        
        # Fonts
        self.title_font = font.Font(family="Helvetica", size=22, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=12)
        self.pass_font = font.Font(family="Courier New", size=14, weight="bold")
        self.btn_font = font.Font(family="Helvetica", size=10, weight="bold")
        
        self.create_widgets()
        self.generate() # Trigger initial generation

    def create_widgets(self):
        # Header
        tk.Label(
            self.root, text="PASSWORD GEN", font=self.title_font,
            fg="#cba6f7", bg="#1e1e2e", pady=30
        ).pack()

        # Display Section
        self.display_frame = tk.Frame(self.root, bg="#313244", padx=15, pady=15)
        self.display_frame.pack(fill="x", padx=30, pady=10)

        self.pass_entry = tk.Entry(
            self.display_frame, textvariable=self.password_var,
            font=self.pass_font, fg="#cdd6f4", bg="#313244",
            borderwidth=0, justify="center"
        )
        self.pass_entry.pack(fill="x")

        # Copy Button
        tk.Button(
            self.root, text="COPY TO CLIPBOARD", command=self.copy_to_clipboard,
            font=self.btn_font, bg="#89b4fa", fg="#1e1e2e",
            activebackground="#b4befe", borderwidth=0, cursor="hand2",
            pady=8
        ).pack(fill="x", padx=30, pady=5)

        # Settings Section
        self.settings_frame = tk.Frame(self.root, bg="#1e1e2e", pady=20)
        self.settings_frame.pack(fill="both")

        # Length Slider
        tk.Label(
            self.settings_frame, text="Length:", font=self.label_font,
            fg="#bac2de", bg="#1e1e2e"
        ).pack()
        
        tk.Scale(
            self.settings_frame, from_=6, to=50, variable=self.length_var,
            orient="horizontal", bg="#1e1e2e", fg="#cba6f7",
            highlightthickness=0, troughcolor="#313244", cursor="hand2",
            command=lambda x: self.generate()
        ).pack(fill="x", padx=60, pady=5)

        # Checkboxes
        check_frame = tk.Frame(self.settings_frame, bg="#1e1e2e")
        check_frame.pack(pady=20)

        for text, var in [("Uppercase (A-Z)", self.upper_var), 
                        ("Numbers (0-9)", self.digits_var), 
                        ("Symbols (#$%@)", self.special_var)]:
            tk.Checkbutton(
                check_frame, text=text, variable=var,
                font=self.label_font, fg="#bac2de", bg="#1e1e2e",
                activebackground="#1e1e2e", activeforeground="#cba6f7",
                selectcolor="#1e1e2e", command=self.generate
            ).pack(anchor="w", pady=5)

        # Strength Indicator
        self.strength_label = tk.Label(
            self.root, text="Strength: Strong", font=self.label_font,
            bg="#1e1e2e", pady=10
        )
        self.strength_label.pack()

        # Big Generate Button
        tk.Button(
            self.root, text="GENERATE NEW", command=self.generate,
            font=self.btn_font, bg="#a6e3a1", fg="#1e1e2e",
            activebackground="#94e2d5", borderwidth=0, cursor="hand2",
            pady=12
        ).pack(fill="x", padx=30, pady=20)

    def generate(self, *args):
        length = self.length_var.get()
        characters = string.ascii_lowercase
        
        if self.upper_var.get(): characters += string.ascii_uppercase
        if self.digits_var.get(): characters += string.digits
        if self.special_var.get(): characters += string.punctuation
        
        if not characters:
            self.password_var.set("Select a type!")
            self.update_strength(0)
            return

        password = "".join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)
        
        # Calculate Strength
        score = 0
        if length >= 12: score += 1
        if self.upper_var.get(): score += 1
        if self.digits_var.get(): score += 1
        if self.special_var.get(): score += 1
        self.update_strength(score)

    def update_strength(self, score):
        if score <= 1:
            self.strength_label.config(text="Strength: WEAK", fg="#f38ba8")
        elif score <= 3:
            self.strength_label.config(text="Strength: MEDIUM", fg="#fab387")
        else:
            self.strength_label.config(text="Strength: STRONG", fg="#a6e3a1")

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password and "!" not in password: # Basic check for valid pass
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    # Centering
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    win_w, win_h = 450, 600
    x = (screen_w // 2) - (win_w // 2)
    y = (screen_h // 2) - (win_h // 2)
    root.geometry(f"{win_w}x{win_h}+{x}+{y}")
    
    app = PasswordGeneratorGUI(root)
    root.mainloop()
