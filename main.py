from models.task import Task
from models.user import User, Admin
from services.task_manager import TaskManager
from utils.file_handler import task_from_json, task_to_json

DATA_FILE = "data/tasks.json"


def choose_role():
    print("Welcome to Task Manager!")
    print("1. Login as Admin")
    print("2. Login as User")
    choice = input("Choose role: ")

    if choice == "1":
        return Admin()
    else:
        return User()


def show_menu(role):
    print("\n--- MENU ---")
    print("1. View all tasks")
    print("2. View statistics")

    # Admin has extra options
    if role.can_add_task():
        print("3. Add task")
    if role.can_edit_task():
        print("4. Edit task")
    if role.can_delete_task():
        print("5. Delete task")
    if role.can_mark_completed():
        print("6. Mark task as completed")

    print("7. Show overdue tasks")
    print("8. Sort tasks by priority")
    print("0. Exit")


def view_tasks(manager):
    print("\n--- ALL TASKS ---")
    manager.show_tasks()


def view_statistics(manager):
    print("\n--- STATISTICS ---")
    manager.statistics()


def view_overdue(manager):
    print("\n--- OVERDUE TASKS ---")
    overdue = manager.overdue_tasks()
    if len(overdue) == 0:
        print("No overdue tasks!")
    else:
        for task in overdue:
            print(task)


def sort_and_show(manager):
    print("\n--- SORTED TASKS (by priority) ---")
    sorted_tasks = manager.sort_tasks()
    for task in sorted_tasks:
        print(task.title, "-", task.priority, "-", task.deadline)


def add_task(manager):
    print("\n--- ADD TASK ---")

    # Generate new ID automatically
    if len(manager.tasks) == 0:
        new_id = 1
    else:
        new_id = manager.tasks[-1].task_id + 1

    title = input("Title: ")
    description = input("Description: ")
    priority = input("Priority (low / medium / high): ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    status = input("Status (pending / in_progress / completed): ")

    task = Task(new_id, title, description, priority, deadline, status)
    manager.add_task(task)
    print("Task added!")


def edit_task(manager):
    print("\n--- EDIT TASK ---")
    task_id = int(input("Enter task ID to edit: "))

    print("Leave field empty to keep old value")
    title = input("New title: ") or None
    description = input("New description: ") or None
    priority = input("New priority (low / medium / high): ") or None
    deadline = input("New deadline (YYYY-MM-DD): ") or None
    status = input("New status (pending / in_progress / completed): ") or None

    result = manager.edit_task(task_id, title, description, priority, deadline, status)
    if result:
        print("Task updated!")
    else:
        print("Task not found or invalid data!")


def delete_task(manager):
    print("\n--- DELETE TASK ---")
    task_id = int(input("Enter task ID to delete: "))

    result = manager.delete_task(task_id)
    if result:
        print("Task deleted!")
    else:
        print("Task not found!")


def complete_task(manager):
    print("\n--- MARK AS COMPLETED ---")
    task_id = int(input("Enter task ID: "))

    result = manager.mark_completed(task_id)
    if result:
        print("Task marked as completed!")
    else:
        print("Task not found!")


