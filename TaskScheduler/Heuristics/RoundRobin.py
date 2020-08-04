import json
from .Heuristics import Heuristics

class RoundRobin(Heuristics):
    def __init__(self):
        super().__init__()
        self.current_task_iterator = 0
        self.finished_tasks = []

    def schedule(self, out_pipes, tasks, number_of_task_processors):
        for task in tasks:
            self.current_task_iterator = (self.current_task_iterator + 1) % number_of_task_processors
            out_pipes[self.current_task_iterator].put(task)

    def __str__(self):
        return 'roundRobin'