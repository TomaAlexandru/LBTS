# pick random task and put on random task processor

from .Heuristic import Heuristic
import random

class Random(Heuristic):
    def get_evaluation(self):
        return {
            'task_order': self.get_task_order(),
            'performance_evaluation': self.get_performance_evaluation()
        }

    def get_task_order(self):
        result = []
        for arrival in range(0, self.tasks[-1]['time_arrival']):
            arrived_tasks = list(filter(lambda e : e['time_arrival'] == arrival, self.tasks))
            if len(arrived_tasks) > 1:
                random.shuffle(arrived_tasks)

        return "random" + str(len(self.tasks)) + str(self.number_of_task_processors)

    def get_performance_evaluation(self):
        return {
            'makespan': '',
            'average_time_of_jobs': '',
            'lateness': '',
            'average_name_of_jobs_pending': '',
            'utilization_of_machines': ''
        }
