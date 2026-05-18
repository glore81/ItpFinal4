# Task Management System

Final project for Introduction to Programming 2 (Python).  
A simple console app to manage your tasks.

---

## How to run

```bash
python main.py
```

No extra libraries needed.

---

## What it does

- Choose your role: **Admin** or **User**
- Admin can add, edit, delete, and complete tasks
- User can only view tasks and statistics
- Tasks are saved to `data/tasks.json` automatically on exit

---

## Project structure

```
main.py                    - main menu and program logic
models/task.py             - Task class
models/user.py             - User and Admin classes
services/task_manager.py   - add, edit, delete, sort tasks
utils/validator.py         - checks priority, status, deadline
utils/file_handler.py      - load and save JSON
data/tasks.json            - task storage
```

---

## Authors

- Aldiyar Temkeshev
- Daniyar Baikanov
- Aziza Kenzhegali
- Mansur Nursultanov

Group SE-2527
