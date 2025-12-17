# 📝 Python CLI To-Do List Manager

A simple **command-line to-do list application** built with Python.  
Tasks are stored locally in a JSON file and persist between runs.
X
This project demonstrates core Python concepts such as file I/O, data structures, program flow, and basic project organization.

---

## 📂 Features

- List all tasks with status (Pending / Done)
- Add new tasks
- Remove tasks
- Mark tasks as completed
- Automatically tracks:
  - Task creation time
  - Task completion time
- Color-coded status output in the terminal
- Persistent storage using JSON

---

## 📂 Project Structure

```
todo-cli/
├── todo_cli/
│   ├── main.py
│   ├── tasks.py
│   ├── storage.py
│   ├── utils.py
├── screenshots/
│   └── cli.png
├── user_tasks.json # Created automatically when tasks are added
├── README.md
├── .gitignore

```
---
## Getting Started

### Requirements
- Python 3.7+
- `colorama`

### Run the application
```
python main.py
```

When you run the app, you’ll see:
```
=== 📝 To-Do List Manager ===
1. List tasks
2. Add task
3. Remove task
4. Mark as done
5. Exit
```
Follow the prompts to manage your tasks!!

## 📂 Example Output

<img src="screenshots/cli.png" width="650">

## 📂 Possible Improvements
- Task priorities or due dates
- Edit existing tasks
- Search/filter tasks
- UI design

## 📜 License
This project is for learning and personal use.