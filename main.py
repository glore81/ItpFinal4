from models.task import Task
from models.user import User, Admin
from services.task_manager import TaskManager
from utils.file_handler import load_tasks, save_tasks


FILE_PATH = "data/tasks.json"


def choose_user():
    print("Choose role:")
    print("1. User")
    print("2. Admin")

    choice = input("Enter choice: ")

    if choice == "2":
        return Admin()

    return User()

def add_new_task(manager):
    task_id = int(input("Enter task ID: "))
    title = input("Enter title: ")
    description = input("Enter description: ")
    priority = input("Enter priority (low/medium/high): ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    status = input("Enter status (pending/in_progress/completed): ")

    task = Task(
        task_id,
        title,
        description,
        priority,
        deadline,
        status
    )

    manager.add_task(task)


def edit_existing_task(manager):
    task_id = int(input("Enter task ID to edit: "))

    print("Leave field empty if you do not want to change it.")

    title = input("New title: ")
    description = input("New description: ")
    priority = input("New priority: ")
    deadline = input("New deadline: ")
    status = input("New status: ")

    if title == "":
        title = None

    if description == "":
        description = None

    if priority == "":
        priority = None

    if deadline == "":
        deadline = None

    if status == "":
        status = None

    result = manager.edit_task(
        task_id,
        title,
        description,
        priority,
        deadline,
        status
    )

    if result:
        print("Task updated")
    else:
        print("Task not found or invalid")


def delete_existing_task(manager):
    task_id = int(input("Enter task ID to delete: "))

    result = manager.delete_task(task_id)

    if result:
        print("Task deleted")
    else:
        print("Task not found")


def mark_task_completed(manager):
    task_id = int(input("Enter task ID: "))

    result = manager.mark_completed(task_id)

    if result:
        print("Task marked as completed")
    else:
        print("Task not found")