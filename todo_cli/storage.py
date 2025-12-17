import json
import os

TASK_FILE = "user_tasks.json"


def load_tasks():
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("⚠️ Warning: tasks file is corrupted. Starting fresh.")
    return []


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
