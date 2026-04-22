import tkinter as tk
from tkinter import font, messagebox
import os

TASKS_FILE = "tasks.txt"

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.geometry("450x550")
        self.root.configure(bg="#1e1e2e")
        
        # File Persistence
        self.tasks = self.load_tasks()
        
        # Fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.item_font = font.Font(family="Helvetica", size=12)
        self.button_font = font.Font(family="Helvetica", size=10, weight="bold")
        
        self.create_widgets()
        self.refresh_listbox()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                return [line.strip() for line in f.readlines()]
        return []

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def create_widgets(self):
        # Header
        self.header = tk.Label(
            self.root, text="MY TASKS", 
            font=self.title_font, fg="#cba6f7", bg="#1e1e2e", pady=20
        )
        self.header.pack()

        # Task List Area (Listbox + Scrollbar)
        self.listbox_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.listbox_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.scrollbar = tk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            self.listbox_frame, font=self.item_font,
            bg="#313244", fg="#cdd6f4", selectbackground="#cba6f7",
            selectforeground="#1e1e2e", borderwidth=0,
            highlightthickness=0, yscrollcommand=self.scrollbar.set
        )
        self.listbox.pack(fill="both", expand=True)
        self.scrollbar.config(command=self.listbox.yview)

        # Input Area
        self.entry_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.entry_frame.pack(fill="x", padx=20, pady=20)

        self.task_entry = tk.Entry(
            self.entry_frame, font=self.item_font,
            bg="#45475a", fg="#cdd6f4", insertbackground="white",
            borderwidth=0, highlightthickness=2, highlightbackground="#313244",
            highlightcolor="#cba6f7"
        )
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=5)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Buttons
        self.btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.btn_frame.pack(fill="x", padx=20, pady=(0, 30))

        self.add_button = tk.Button(
            self.btn_frame, text="ADD TASK", command=self.add_task,
            font=self.button_font, bg="#a6e3a1", fg="#1e1e2e",
            activebackground="#94e2d5", cursor="hand2", borderwidth=0,
            padx=15, pady=8
        )
        self.add_button.pack(side="left", expand=True, fill="x", padx=(0, 5))

        self.delete_button = tk.Button(
            self.btn_frame, text="DELETE SELECTED", command=self.delete_task,
            font=self.button_font, bg="#f38ba8", fg="#1e1e2e",
            activebackground="#eba0ac", cursor="hand2", borderwidth=0,
            padx=15, pady=8
        )
        self.delete_button.pack(side="left", expand=True, fill="x", padx=(5, 0))

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            self.refresh_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task description.")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            removed_task = self.tasks.pop(selected_index)
            self.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, f" • {task}")

if __name__ == "__main__":
    root = tk.Tk()
    # Centering the window
    win_w, win_h = 450, 550
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = (screen_w // 2) - (win_w // 2)
    y = (screen_h // 2) - (win_h // 2)
    root.geometry(f"{win_w}x{win_h}+{x}+{y}")
    
    app = ToDoListGUI(root)
    root.mainloop()
