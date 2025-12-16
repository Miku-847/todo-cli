import uuid
from datetime import datetime
from colorama import Fore, Style
from storage import save_tasks
from utils import get_input

# this will be set from main.py
tasks = []


def list_task():
    if not tasks:
        print("📂 No task yet!\n")
        return

    print("📋 Current Tasks:")
    for i, task in enumerate(tasks, 1):
        status_text = "✅Done" if task["done"] else "❌Pending"
        status_color = Fore.GREEN if task["done"] else Fore.RED

        created = task.get("created_at", "Unknown")
        completed = task.get("completed_at")

        line = f"{i}. {task['title']} [{status_color}{status_text}{Style.RESET_ALL}] (created: {created})"
        if completed:
            line += f" (Completed: {Fore.GREEN}{completed}{Style.RESET_ALL})"
        print(line)
    print()


def add_task():
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
    save_tasks(tasks)
    print(f"Task '{new_task}' added!\n")


def remove_task():
    list_task()
    if not tasks:
        return

    choice = get_input("Enter task number to remove: ")
    if not choice:
        return

    try:
        index = int(choice) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed task '{removed['title']}'\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")


def mark_task_done():
    list_task()
    if not tasks:
        return

    choice = get_input("Enter task number to mark as done: ")
    if not choice:
        return

    try:
        index = int(choice) - 1
        task = tasks[index]

        if task["done"]:
            print("Task is already done!\n")
            return

        task["done"] = True
        task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_tasks(tasks)
        print(f"Marked task '{task['title']}' as done!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")
