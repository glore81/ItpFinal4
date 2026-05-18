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
