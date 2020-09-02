import json


""" The current class is the parent method for all algorithms and contains the common method for all algorithm class """
class Heuristics(dict):

    """ constructor receives all task processor as parameters in order to operate them """
    def __init__(self, taskProcessors):
        """ we call parent constructor in order to use class as a dict structure when necessary """
        super().__init__()
        """ we assign properties for the current instance """
        self.processors = taskProcessors
        self.finished_tasks = []
        self.current_finished = []

    """ task reception is a method used in order to receive task queue by the algorithm """
    def task_reception(self, number_of_tasks, task_resources_distributions, in_pipes):
        """ TASK RECEPTION """
        for in_pipe in in_pipes:
            """ we collect finished tasks from all task processors in order to write them in reports files """
            self.finished_tasks = self.finished_tasks + in_pipe.items
            self.current_finished = in_pipe.items
            in_pipe.items = []
            """ OPERATION FINISHED """
            if number_of_tasks == len(self.finished_tasks):
                with open("Reports/%s_%s.json" % (task_resources_distributions, self.__str__()),
                          "w") as data_file:
                    json.dump(self.finished_tasks, data_file, indent=4, sort_keys=True)
                """ we raise an exception when finished task number reach initial task number in order to signal
                    the scheduler that we have finished the current iteration """
                raise Exception(task_resources_distributions, self.__str__())

    """ we continuously have data regarding task processors loading """
    def update_processor_states(self, current_finished_tasks):
        for current_finished_task in current_finished_tasks:
            self.processors[current_finished_task['processor_index']] = current_finished_task['current_resources']

    """ check if a specific processor has enough resources in order to process a given task """
    def has_available_resources_to_process_task(self, processor, task):
        task_can_be_processed = True
        for type, value in processor.items():
            if (processor[type] - task[type] < 0):
                task_can_be_processed = False
        return task_can_be_processed
