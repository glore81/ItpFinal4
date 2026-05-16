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
