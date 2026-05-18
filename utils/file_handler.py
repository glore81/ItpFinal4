import json
from models.task import from_dict, Task


def task_from_json(filename,task_manager):
    try:
        with open(filename,'r') as f:
            tasks = json.load(f)
        for task in tasks:
            task = from_dict(task)
            task_manager.add_task(task)
            print("Loaded!")
        return True
    except FileNotFoundError:
        print("File not found!")
        return False
    except Exception as e:
        print(e)
        return False

def task_to_json(filename,task_manager):
    try:
        task=[]
        for task in task_manager.tasks:
            task.append(task.to_dict())
        with open(filename,'w') as f:
            json.dump(task,f,indent=4)
        print("Saved!")
        return True
    except Exception as e:
        print(e)
        return False








