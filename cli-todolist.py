import os
import json
import uuid
from datetime import datetime
from colorama import Fore, Style, init

# resets color after each print
init(autoreset=True)

TASK_FILE = "user_tasks.json"

# loads existing tasks
if os.path.exists(TASK_FILE):
    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print("⚠️ Warning: tasks file is corrupted. Starting with an empty task list.")
        tasks = []
else:
    tasks = []


def save_task():
    """Saves task list to the JSON file"""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def get_input(prompt):
    """For empty user input"""
    value = input(prompt).strip()
    if not value:
        print("Input cannot be empty!\n")
        return None
    return value


def list_task():
    """Displays all tasks with their status and timestamsp"""

    if not tasks:
        print("📂 No task yet!\n")
        return

    print("📋 Current Tasks:")
    for i, task in enumerate(tasks, 1):

        status_text = "✅Done" if task["done"] else "❌Pending"
        status_color = Fore.GREEN if task["done"] else Fore.RED

        created = task.get("created_at", "Unknown")
        completed = task.get("completed_at", "")

        line = f"{i}. {task['title']} [{status_color}{status_text}{Style.RESET_ALL}] (created: {created})"
        if completed:
            line += f" (Completed: {Fore.GREEN}{completed}{Style.RESET_ALL})"
        print(line)
    print()


def add_task():
    """Add new task"""

    new_task = get_input("Enter task title: ")
    if not new_task:
        return

    task = {
        "id": str(uuid.uuid4()),
        "title": new_task,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "completed_at": None
    }
    tasks.append(task)
    save_task()
    print(f"Task '{new_task}' added!\n")


def remove_task():
    """Remove a task by its number"""

    list_task()
    if not tasks:
        return

    removed_task = get_input("Enter task number to remove: ")
    if not removed_task:
        return

    try:
        removed_task = int(removed_task)
        if 1 <= removed_task <= len(tasks):
            removed = tasks.pop(removed_task-1)
            save_task()
            print(f"Removed task '{removed['title']}'\n")
        else:
            print("Invalid Task Number!\n")
    except ValueError:
        print("Please Enter A Valid Number!\n")


def mark_task_done():
    """Mark a selected task as completed"""

    list_task()
    if not tasks:
        return

    done_task = get_input("Enter task number to mark as done: ")
    if not done_task:
        return

    try:
        done_task = int(done_task)

        if 1 <= done_task <= len(tasks):
            task = tasks[done_task-1]
            if task["done"]:
                print("Task is already marked as done!\n")
                return
            task["done"] = True
            task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_task()
            print(f"Marked task '{tasks[done_task-1]['title']}' as done\n")
        else:
            print("Invalid Task Number!\n")
    except ValueError:
        print("Please Enter A Valid Number!\n")


def main():
    """Main function"""

    while True:
        print("=== 📝 To-Do List Manager ===")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark as done")
        print("5. Exit")

        user_input = input("Choose an option: ").strip()
        print()
        if user_input:
            if user_input == "1":
                list_task()
            elif user_input == "2":
                add_task()
            elif user_input == "3":
                remove_task()
            elif user_input == "4":
                mark_task_done()
            elif user_input == "5":
                print("Bye 🤘")
                break
            else:
                print("Invalid Number! Please choose from 1-5 \n")
        else:
            print("User input cannot be Empty!\n")


if __name__ == "__main__":
    main()
