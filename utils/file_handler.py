import json
from models.task import from_dict


def task_to_json(filename,task_manager):
    with open(filename,'r') as f:
        tasks = json.load(f)
    for task in tasks:
        task = from_dict(task)
        task_manager.add_task(task)
        print("Loaded!")
    return True





