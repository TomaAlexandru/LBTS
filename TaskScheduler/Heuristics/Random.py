# pick random task and put on random task processor
import random

class Random:
    def __init__(self):
        self.current_task_iterator = 0

    def schedule(self, out_pipes, tasks, number_of_task_processors):
        while len(tasks) > 0:
            task_index = random.choice([*range(len(tasks))])
            task = tasks[task_index]
            list_of_task_processors = [*range(number_of_task_processors)]
            random_processor = random.choice(list_of_task_processors)
            out_pipes[random_processor].put(task)
            del tasks[task_index]

    def __str__(self):
        return 'random'
