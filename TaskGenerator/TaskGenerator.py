from .Distribution import Distribution

class TaskGenerator:
    number_of_tasks        = None
    resources_distribution = None
    resources_max_values   = None

    def __init__(self, number_of_taskProcessors, resources_distribution, resources_max_values):
        self.number_of_taskProcessors = number_of_taskProcessors
        self.resources_distribution = resources_distribution
        self.resources_max_values = resources_max_values

    def get_tasks(self):
        taskProcessors = []
        # generate taskProcessor
        previous_arrival_time = 0
        for i in range(self.number_of_taskProcessors):
            distribution = Distribution(self.resources_distribution, self.resources_max_values)
            task = distribution.get_generated_values()
            task['time_arrival'] = (task['time_arrival'] - 1) + previous_arrival_time
            previous_arrival_time = task['time_arrival']
            taskProcessors.append(task)
        for t in taskProcessors:
            t['time_arrival'] = int(t['time_arrival'] / 50)
            t['due_time'] = t['time_arrival'] + t['time_processing'] + t['due_time']
        return taskProcessors