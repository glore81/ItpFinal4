import unittest
from services.task_manager import TaskManager
from models.task import Task

class TaskManagerTest(unittest.TestCase):
    def creat(self):
        self.manager = TaskManager()
        self.task = Task(1,"Test", "Description", "low", "2026-11-08", "parsing")
        self.manager.add_task(self.task)
