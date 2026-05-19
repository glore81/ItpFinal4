import unittest
from services.task_manager import TaskManager
from models.task import Task

class TaskManagerTest(unittest.TestCase):
    def creat(self):
        self.manager = TaskManager()
        self.task = Task(1,"Test", "Description", "low", "2026-11-08", "pending")
        self.manager.add_task(self.task)
    def test_add_task(self):
        new_task=Task(2, "fresh", "Description", "medium", "2026-11-08", "in progress")
        self.manager.add_task(new_task)
        if len(self.manager.tasks)==2:
            return True
        else:
            return False
