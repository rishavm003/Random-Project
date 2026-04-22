import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Loads tasks from the tasks.txt file."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                # Read lines and strip newline characters
                tasks = [line.strip() for line in f.readlines()]
        except Exception as e:
            print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks):
    """Saves the current list of tasks to tasks.txt."""
    try:
        with open(TASKS_FILE, "w") as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def view_tasks(tasks):
    """Displays all current tasks with their indices."""
    if not tasks:
        print("\n--- Your To-Do List is empty! ---")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Prompts the user for a new task and adds it to the list."""
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def delete_task(tasks):
    """Prompts the user for a task index and deletes it if valid."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        choice = int(input("\nEnter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Removed: '{removed_task}'")
        else:
            print("Invalid number. Please choose a task from the list.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main entry point for the application."""
    tasks = load_tasks()
    
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number between 1 and 4.")

if __name__ == "__main__":
    main()
