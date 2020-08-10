class ReinforcementLearning:
    def __init__(self):
        self.current_task_iterator = 0

    def schedule(self, out_pipes, tasks, number_of_task_processors):
        for task in tasks:
            self.current_task_iterator = (self.current_task_iterator + 1) % number_of_task_processors
            out_pipes[self.current_task_iterator].put(task)

    def __str__(self):
        return 'reinforcementLearning'
