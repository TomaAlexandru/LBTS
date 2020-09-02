from .Distribution import Distribution


""" extendable class that creates tasks for simulation """
class TaskGenerator:
    number_of_tasks        = None
    resources_distribution = None
    resources_max_values   = None

    def __init__(self, number_of_tasks, resources_distribution, resources_max_values):
        self.number_of_tasks = number_of_tasks
        self.resources_distribution = resources_distribution
        self.resources_max_values = resources_max_values

    """ returns generated tasks """
    def get_tasks(self):
        """ result - returned tasks """
        generated_tasks = []
        """ start time for generated tasks """
        previous_arrival_time = 0
        """ Distribution instance is used for generate random values for tasks """
        distribution = Distribution(self.resources_distribution, self.resources_max_values)
        """ for each task we will add time of arrival, due time and require resource on them """
        for i in range(self.number_of_tasks):
            task = distribution.get_generated_values()
            """ time of arrival should be increased by what value is generated """
            task['time_arrival'] = (task['time_arrival'] - 1) + previous_arrival_time
            previous_arrival_time = task['time_arrival']
            generated_tasks.append(task)
        """ in order to highlight better difference of performance between algorithms we put generated tasks in 
            batches just for testing purposes, and we also add due date for each task """
        for t in generated_tasks:
            t['time_arrival'] = int(t['time_arrival'] / 50)
            t['due_time'] = t['time_arrival'] + t['time_processing'] + t['due_time']
        return generated_tasks