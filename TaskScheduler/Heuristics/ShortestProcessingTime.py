# arrange tasks by shortest processing time and put it round robin

from .Heuristic import Heuristic
import random

class ShortestProcessingTime(Heuristic):
    def get_evaluation(self):
        return {
            'task_order': self.get_task_order(),
            'performance_evaluation': self.get_performance_evaluation()
        }

    def get_task_order(self):
        return random.shuffle(self.tasks[0:10])

    def get_performance_evaluation(self):
        return {
            'makespan': '',
            'average_time_of_jobs': '',
            'lateness': '',
            'average_name_of_jobs_pending': '',
            'utilization_of_machines': ''
        }
