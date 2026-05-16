class Task:
    def __init__(self,task_id,title,description,priority,deadline,status):
        self.task_id = task_id;
        self.title = title;
        self.description = description;
        self.priority = priority;
        self.deadline = deadline;
        self.status = status;

    def __str__(self):
        return (str("Task Id: " + str(self.task_id) + "\nTitle: "+self.title)+"\nDescription: "+self.description +
                "\nPriority: " + self.priority + "\nDeadline: " + self.deadline + "\nStatus: " + self.status);
