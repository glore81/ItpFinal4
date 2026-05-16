class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
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
            task.update(title , description , priority , deadline , status )
            return True
        return False
    def mark_completed(self , task_id):
        task = self.find_task(task_id)
        if task is not None:
            task.mark_completed()
            return True
        return False

