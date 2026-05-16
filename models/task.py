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

    def mark_completed(self):
        self.status = "completed";

    def update(self, title = None, description = None, priority = None, deadline = None, status = None):

        if title != None:
            self.title = title;

        if description != None:
            self.description = description;

        if priority != None:
            self.priority = priority;

        if deadline != None:
            self.deadline = deadline;

        if status != None:
            self.status = status;

    def to_dict(self):
        return {"id" : self.task_id,
                "title" : self.title,
                "description" : self.description,
                "priority" : self.priority,
                "deadline" : self.deadline,
                "status" : self.status}

def from_dict(data):
    return Task(data["id"], data["title"], data["description"], data["priority"],data["deadline"], data["status"])