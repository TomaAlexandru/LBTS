import random

""" extendable class that creates tasks for simulation """
class TaskGenerator:

    def __init__(self, number_of_tasks):
        self.number_of_tasks = number_of_tasks

    """ returns generated tasks """
    def get_tasks(self, distribution):
        """ result - returned tasks """
        generated_tasks = []
        """ for each task we will add time of arrival, due time and require resource on them """
        number_of_tasks_generated = 0
        time = 0

        stop_generator = False
        while True:
            """ number of tasks per unit time """
            current_number_of_tasks_generated = distribution.get_generated_values()['time_arrival']
            for j in range(current_number_of_tasks_generated):
                task = distribution.get_generated_values()
                """ time of arrival should be increased by what value is generated """
                task['time_arrival'] = time
                generated_tasks.append(task)
                number_of_tasks_generated += 1
                if number_of_tasks_generated == self.number_of_tasks:
                    stop_generator = True
                    break
            if stop_generator:
                break
            time+=1
        """ make sure that due time is greater than time_arrival + time_processing """
        for t in generated_tasks:
            t['due_time'] = t['time_arrival'] + t['time_processing'] + t['due_time']
        return generated_tasks