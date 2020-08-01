import random
from abc import abstractmethod

class Heuristic:
    performance_evaluations_criterion = [
        'makespan',
        'average_time_of_jobs',
        'lateness',
        'average_name_of_jobs_pending',
        'utilization_of_machines'
    ]

    def set_tasks(self, tasks, number_of_task_processors, task_processor_resource):
        self.tasks = tasks
        self.number_of_task_processors = number_of_task_processors
        self.task_processor_resource = task_processor_resource

    @abstractmethod
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
