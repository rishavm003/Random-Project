import tkinter as tk
from tkinter import font, messagebox

class CountdownTimerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("420x520")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        # Timer State
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.is_running = False
        self.after_id = None

        # Fonts
        self.display_font = font.Font(family="Courier New", size=60, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=11)
        self.input_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.btn_font = font.Font(family="Helvetica", size=11, weight="bold")

        self.create_widgets()

    def create_widgets(self):
        # Header
        tk.Label(
            self.root, text="⏱  COUNTDOWN TIMER",
            font=font.Font(family="Helvetica", size=16, weight="bold"),
            fg="#cba6f7", bg="#1e1e2e", pady=20
        ).pack()

        # Digital Display
        self.display_frame = tk.Frame(self.root, bg="#181825", pady=25)
        self.display_frame.pack(fill="x", padx=30)

        self.display_label = tk.Label(
            self.display_frame, text="00:00:00",
            font=self.display_font, fg="#cdd6f4", bg="#181825"
        )
        self.display_label.pack()

        # Progress hint
        self.hint_label = tk.Label(
            self.root, text="Set your time below and press Start",
            font=self.label_font, fg="#6c7086", bg="#1e1e2e"
        )
        self.hint_label.pack(pady=8)

        # Time Input Row
        self.input_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.input_frame.pack(pady=15)

        for label_text, attr in [("HH", "hours_var"), ("MM", "minutes_var"), ("SS", "seconds_var")]:
            col = tk.Frame(self.input_frame, bg="#1e1e2e")
            col.pack(side="left", padx=8)

            tk.Label(col, text=label_text, font=self.label_font,
                     fg="#6c7086", bg="#1e1e2e").pack()

            var = tk.StringVar(value="00")
            setattr(self, attr, var)

            entry = tk.Entry(
                col, textvariable=var, font=self.input_font,
                bg="#313244", fg="#cdd6f4", insertbackground="white",
                width=4, justify="center", borderwidth=0,
                highlightthickness=2, highlightbackground="#45475a",
                highlightcolor="#cba6f7"
            )
            entry.pack()

        # Preset Buttons
        tk.Label(
            self.root, text="Quick Presets:",
            font=self.label_font, fg="#6c7086", bg="#1e1e2e"
        ).pack(pady=(15, 5))

        preset_frame = tk.Frame(self.root, bg="#1e1e2e")
        preset_frame.pack()

        for label, seconds in [("1 min", 60), ("5 min", 300), ("25 min 🍅", 1500), ("1 hr", 3600)]:
            tk.Button(
                preset_frame, text=label,
                command=lambda s=seconds: self.apply_preset(s),
                font=self.label_font, bg="#313244", fg="#bac2de",
                activebackground="#45475a", borderwidth=0, cursor="hand2",
                padx=10, pady=5
            ).pack(side="left", padx=4)

        # Control Buttons
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(fill="x", padx=30, pady=25)

        self.start_btn = tk.Button(
            btn_frame, text="▶  START", command=self.start_timer,
            font=self.btn_font, bg="#a6e3a1", fg="#1e1e2e",
            activebackground="#94e2d5", borderwidth=0, cursor="hand2",
            pady=10
        )
        self.start_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        self.pause_btn = tk.Button(
            btn_frame, text="⏸  PAUSE", command=self.pause_timer,
            font=self.btn_font, bg="#fab387", fg="#1e1e2e",
            activebackground="#f38ba8", borderwidth=0, cursor="hand2",
            pady=10, state="disabled"
        )
        self.pause_btn.pack(side="left", expand=True, fill="x", padx=5)

        self.reset_btn = tk.Button(
            btn_frame, text="↺  RESET", command=self.reset_timer,
            font=self.btn_font, bg="#f38ba8", fg="#1e1e2e",
            activebackground="#eba0ac", borderwidth=0, cursor="hand2",
            pady=10
        )
        self.reset_btn.pack(side="left", expand=True, fill="x", padx=(5, 0))

    def apply_preset(self, seconds):
        self.reset_timer()
        self.hours_var.set(f"{seconds // 3600:02d}")
        self.minutes_var.set(f"{(seconds % 3600) // 60:02d}")
        self.seconds_var.set(f"{seconds % 60:02d}")
        self.update_display(seconds)

    def get_input_seconds(self):
        try:
            h = int(self.hours_var.get() or 0)
            m = int(self.minutes_var.get() or 0)
            s = int(self.seconds_var.get() or 0)
            return h * 3600 + m * 60 + s
        except ValueError:
            return None

    def update_display(self, seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        self.display_label.config(text=f"{h:02d}:{m:02d}:{s:02d}")

        # Color feedback based on remaining time
        if seconds == 0:
            self.display_label.config(fg="#f38ba8")  # Red when done
            self.root.configure(bg="#1e1e2e")
        elif self.total_seconds > 0 and seconds <= self.total_seconds * 0.2:
            self.display_label.config(fg="#fab387")  # Orange for last 20%
        else:
            self.display_label.config(fg="#cdd6f4")  # Default

    def start_timer(self):
        if not self.is_running:
            # Fresh start: read from input
            if self.remaining_seconds == 0:
                total = self.get_input_seconds()
                if not total or total <= 0:
                    messagebox.showwarning("Invalid Time", "Please enter a valid time greater than 0.")
                    return
                self.total_seconds = total
                self.remaining_seconds = total

            self.is_running = True
            self.start_btn.config(state="disabled")
            self.pause_btn.config(state="normal")
            self.hint_label.config(text="Timer is running...")
            self.tick()

    def tick(self):
        if self.is_running and self.remaining_seconds > 0:
            self.update_display(self.remaining_seconds)
            self.remaining_seconds -= 1
            self.after_id = self.root.after(1000, self.tick)
        elif self.remaining_seconds == 0 and self.is_running:
            self.update_display(0)
            self.is_running = False
            self.start_btn.config(state="normal")
            self.pause_btn.config(state="disabled")
            self.hint_label.config(text="🔔 Time is Up!", fg="#f38ba8")
            messagebox.showinfo("Time's Up!", "🔔 Your countdown has finished!")

    def pause_timer(self):
        if self.is_running:
            self.is_running = False
            if self.after_id:
                self.root.after_cancel(self.after_id)
            self.start_btn.config(state="normal", text="▶  RESUME")
            self.pause_btn.config(state="disabled")
            self.hint_label.config(text="Timer is paused.")

    def reset_timer(self):
        self.is_running = False
        if self.after_id:
            self.root.after_cancel(self.after_id)
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.display_label.config(text="00:00:00", fg="#cdd6f4")
        self.hours_var.set("00")
        self.minutes_var.set("00")
        self.seconds_var.set("00")
        self.start_btn.config(state="normal", text="▶  START")
        self.pause_btn.config(state="disabled")
        self.hint_label.config(text="Set your time below and press Start", fg="#6c7086")

if __name__ == "__main__":
    root = tk.Tk()
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    win_w, win_h = 420, 520
    x = (screen_w // 2) - (win_w // 2)
    y = (screen_h // 2) - (win_h // 2)
    root.geometry(f"{win_w}x{win_h}+{x}+{y}")
    app = CountdownTimerGUI(root)
    root.mainloop()
