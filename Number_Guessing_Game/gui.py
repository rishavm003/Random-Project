import tkinter as tk
from tkinter import font
import random
import json
import os

class NumberGuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game Pro")
        self.root.geometry("450x650")
        self.root.configure(bg="#1e1e2e")  # Dark mode background
        
        # Difficulty Settings
        self.difficulties = {
            "Easy": 50,
            "Medium": 100,
            "Hard": 500
        }
        self.current_difficulty = "Medium"
        self.max_range = self.difficulties[self.current_difficulty]
        
        # Game State
        self.target_number = random.randint(1, self.max_range)
        self.attempts = 0
        self.high_scores = self.load_high_scores()
        
        # Custom Fonts
        self.title_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=12)
        self.feedback_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=11, weight="bold")
        self.hint_font = font.Font(family="Helvetica", size=10, slant="italic")
        
        self.create_widgets()

    def load_high_scores(self):
        score_file = "high_scores.json"
        if os.path.exists(score_file):
            with open(score_file, "r") as f:
                return json.load(f)
        return {"Easy": None, "Medium": None, "Hard": None}

    def save_high_score(self):
        score_file = "high_scores.json"
        current_record = self.high_scores.get(self.current_difficulty)
        if current_record is None or self.attempts < current_record:
            self.high_scores[self.current_difficulty] = self.attempts
            with open(score_file, "w") as f:
                json.dump(self.high_scores, f)
            return True
        return False

    def create_widgets(self):
        # Header
        self.header = tk.Label(
            self.root, text="GUESS THE NUMBER", 
            font=self.title_font, fg="#cba6f7", bg="#1e1e2e", pady=30
        )
        self.header.pack()

        # Difficulty Buttons
        self.btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.btn_frame.pack(pady=5)
        
        self.diff_btns = {}
        for diff in self.difficulties:
            btn = tk.Button(
                self.btn_frame, text=diff, 
                command=lambda d=diff: self.change_difficulty(d),
                bg="#313244", fg="#bac2de", font=self.button_font,
                relief="flat", padx=10, cursor="hand2"
            )
            btn.pack(side="left", padx=5)
            self.diff_btns[diff] = btn
        
        self.update_diff_buttons()

        self.instruction = tk.Label(
            self.root, text=f"I'm thinking of a number between 1 and {self.max_range}",
            font=self.label_font, fg="#bac2de", bg="#1e1e2e"
        )
        self.instruction.pack(pady=10)

        # High Score Label
        self.high_score_label = tk.Label(
            self.root, text=self.get_high_score_text(),
            font=self.label_font, fg="#fab387", bg="#1e1e2e"
        )
        self.high_score_label.pack(pady=5)

        # Input Area
        self.entry = tk.Entry(
            self.root, font=self.title_font, justify='center',
            width=5, bg="#313244", fg="#cdd6f4", insertbackground="white",
            borderwidth=0, highlightthickness=2, highlightbackground="#45475a",
            highlightcolor="#cba6f7"
        )
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", lambda event: self.check_guess())  # Allow Enter key
        self.entry.focus_set()

        # Submit Button
        self.guess_button = tk.Button(
            self.root, text="GUESS", command=self.check_guess,
            font=self.button_font, bg="#cba6f7", fg="#1e1e2e",
            activebackground="#b4befe", activeforeground="#1e1e2e",
            width=15, pady=8, cursor="hand2", borderwidth=0
        )
        self.guess_button.pack(pady=10)

        # Hint Button
        self.hint_button = tk.Button(
            self.root, text="GET HINT (Penalty: +2 tries)", command=self.give_hint,
            font=self.hint_font, bg="#1e1e2e", fg="#94e2d5",
            activebackground="#1e1e2e", activeforeground="#a6e3a1",
            relief="flat", cursor="hand2"
        )
        self.hint_button.pack(pady=5)

        # Feedback Label
        self.feedback_label = tk.Label(
            self.root, text="Type your guess and hit Enter",
            font=self.feedback_font, fg="#bac2de", bg="#1e1e2e", wraplength=350
        )
        self.feedback_label.pack(pady=30)

        # Attempt Counter
        self.counter_label = tk.Label(
            self.root, text="Attempts: 0",
            font=self.label_font, fg="#6c7086", bg="#1e1e2e"
        )
        self.counter_label.pack(side="bottom", pady=20)

        # Restart Button (Hidden initially)
        self.restart_button = tk.Button(
            self.root, text="PLAY AGAIN", command=self.reset_game,
            font=self.button_font, bg="#a6e3a1", fg="#1e1e2e",
            activebackground="#94e2d5", activeforeground="#1e1e2e",
            width=15, pady=8, cursor="hand2", borderwidth=0
        )

    def change_difficulty(self, diff):
        self.current_difficulty = diff
        self.max_range = self.difficulties[diff]
        self.update_diff_buttons()
        self.reset_game()

    def update_diff_buttons(self):
        for diff, btn in self.diff_btns.items():
            if diff == self.current_difficulty:
                btn.config(bg="#cba6f7", fg="#1e1e2e")
            else:
                btn.config(bg="#313244", fg="#bac2de")

    def get_high_score_text(self):
        score = self.high_scores.get(self.current_difficulty)
        if score:
            return f"Best: {score} tries"
        return "Best: --"

    def give_hint(self):
        self.attempts += 2
        self.counter_label.config(text=f"Attempts: {self.attempts}")
        
        # Decide which hint to give
        hints = []
        if self.target_number % 2 == 0:
            hints.append("It's an EVEN number.")
        else:
            hints.append("It's an ODD number.")
            
        if self.target_number % 5 == 0:
            hints.append("It's a multiple of 5.")
            
        if self.target_number > (self.max_range // 2):
            hints.append(f"It's in the top half ( >{self.max_range // 2}).")
        else:
            hints.append(f"It's in the bottom half ( <={self.max_range // 2}).")
            
        hint = random.choice(hints)
        self.feedback_label.config(text=f"HINT: {hint}", fg="#94e2d5")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            self.counter_label.config(text=f"Attempts: {self.attempts}")
            
            diff = abs(self.target_number - guess)
            self.update_heat(diff)

            if guess < self.target_number:
                self.feedback_label.config(text="TOO LOW! ↑", fg="#89b4fa") # Blue for low
            elif guess > self.target_number:
                self.feedback_label.config(text="TOO HIGH! ↓", fg="#f38ba8") # Red for high
            else:
                self.feedback_label.config(text=f"CORRECT! \nIt was {self.target_number}", fg="#a6e3a1") # Green for correct
                self.game_over()
            
            self.entry.delete(0, tk.END)
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!", fg="#fab387")

    def update_heat(self, diff):
        # Color shifting based on distance
        # Easy: 50, Medium: 100, Hard: 500
        # Scale the difference to a 0-255 range for red intensity
        intensity = min(255, max(0, 255 - (diff * (255 / (self.max_range / 2)))))
        color = f'#{int(intensity):02x}{int(40):02x}{int(80):02x}'
        self.root.configure(bg=color)
        self.header.config(bg=color)
        self.instruction.config(bg=color)
        self.high_score_label.config(bg=color)
        self.feedback_label.config(bg=color)
        self.counter_label.config(bg=color)
        self.btn_frame.config(bg=color)
        self.hint_button.config(bg=color, activebackground=color)

    def game_over(self):
        self.entry.config(state="disabled")
        self.guess_button.pack_forget()
        self.hint_button.pack_forget()
        self.restart_button.pack(pady=10)
        
        is_new_record = self.save_high_score()
        if is_new_record:
            self.feedback_label.config(text="NEW RECORD! 🎉", fg="#fab387")
            self.high_score_label.config(text=self.get_high_score_text())

    def reset_game(self):
        self.target_number = random.randint(1, self.max_range)
        self.attempts = 0
        self.root.configure(bg="#1e1e2e")
        self.counter_label.config(text="Attempts: 0", bg="#1e1e2e")
        self.feedback_label.config(text="New game! Guess a number.", fg="#bac2de", bg="#1e1e2e")
        self.header.config(bg="#1e1e2e")
        self.instruction.config(text=f"I'm thinking of a number between 1 and {self.max_range}", bg="#1e1e2e")
        self.high_score_label.config(text=self.get_high_score_text(), bg="#1e1e2e")
        self.btn_frame.config(bg="#1e1e2e")
        self.hint_button.config(bg="#1e1e2e")
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.restart_button.pack_forget()
        self.guess_button.pack(pady=10)
        self.hint_button.pack(pady=5)
        self.entry.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    # Centering the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    win_w, win_h = 450, 650
    x = (screen_width // 2) - (win_w // 2)
    y = (screen_height // 2) - (win_h // 2)
    root.geometry(f"{win_w}x{win_h}+{x}+{y}")
    
    app = NumberGuessingGameGUI(root)
    root.mainloop()
