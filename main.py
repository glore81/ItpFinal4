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
