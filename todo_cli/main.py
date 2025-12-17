from colorama import init
from storage import load_tasks
import tasks

init(autoreset=True)


def main():
    # load tasks once and share with tasks.py
    tasks.tasks = load_tasks()

    while True:
        print("=== 📝 To-Do List Manager ===")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark as done")
        print("5. Exit")

        user_input = input("Choose an option: ").strip()
        print()

        if not user_input:
            print("User input cannot be empty!\n")
            continue

        if user_input == "1":
            tasks.list_task()
        elif user_input == "2":
            tasks.add_task()
        elif user_input == "3":
            tasks.remove_task()
        elif user_input == "4":
            tasks.mark_task_done()
        elif user_input == "5":
            print("Bye 🤘")
            break
        else:
            print("Invalid Number! Please choose from 1-5\n")


if __name__ == "__main__":
    main()
