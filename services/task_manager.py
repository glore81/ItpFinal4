from datetime import datetime
from utils.validator import validate_task
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        if validate_task(task):
            self.tasks.append(task)
        else:
            print("Invalid task")
    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks")
            return
        for task in self.tasks:
            print(task.title , "-" , task.status)
    def find_task(self , task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    def delete_task(self , task_id):
        task = self.find_task(task_id)
        if task is not None:
            self.tasks.remove(task)
            return True
        return False
    def edit_task(self , task_id , title = None , description = None , priority = None , deadline = None , status = None):
        task = self.find_task(task_id)
        if task is not None:
            old_title = task.title
            old_description = task.description
            old_priority = task.priority
            old_deadline = task.deadline
            old_status = task.status
            task.update(title , description , priority , deadline , status )

            if not validate_task(task):
                task.title = old_title
                task.description = old_description
                task.priority = old_priority
                task.deadline = old_deadline
                task.status = old_status

                print("Invalid task")
                return False
            return True
        return False
    def mark_completed(self , task_id):
        task = self.find_task(task_id)
        if task is not None:
            task.mark_completed()
            return True
        return False
    def sort_tasks(self):
        priority_order = {
            "high" : 1 ,
            "medium" : 2 ,
            "low" : 3
        }
        self.tasks.sort(key = lambda task :( priority_order[task.priority] , task.deadline))
        return self.tasks
    def overdue_tasks(self):
        today = datetime.today().date()
        overdue = []
        for task in self.tasks:
            task_deadline = datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            ).date()
            if task_deadline < today and task.status != "completed":
                overdue.append(task)
        return overdue
    def statistics(self):
        total = len(self.tasks)
        completed = 0
        for task in self.tasks:
            if task.status == "completed":
                completed += 1
        if total == 0:
            percent = 0
        else:
            percent = completed / total * 100

        print("Tasks:" , total)
        print("Completed:" , completed)
        print("Completion:" , round(percent , 2) , "%")