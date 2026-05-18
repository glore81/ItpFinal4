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