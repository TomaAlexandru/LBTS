import json

class Heuristics(dict):

    def __init__(self, tasksProcessor):
        super().__init__()
        self.processors = tasksProcessor
        self.finished_tasks = []
        self.current_finished = []

    def task_reception(self, number_of_tasks, task_resources_distributions, in_pipes):
        """ TASK RECEPTION """
        for in_pipe in in_pipes:
            self.finished_tasks = self.finished_tasks + in_pipe.items
            self.current_finished = in_pipe.items
            in_pipe.items = []
            """ OPERATION FINISHED """
            if number_of_tasks == len(self.finished_tasks):
                with open("Reports/%s_%s.json" % (task_resources_distributions, self.__str__()),
                          "w") as twitter_data_file:
                    json.dump(self.finished_tasks, twitter_data_file, indent=4, sort_keys=True)
                raise Exception(task_resources_distributions, self.__str__())

    def update_processor_states(self, current_finished_tasks):
        for current_finished_task in current_finished_tasks:
            self.processors[current_finished_task['processor_index']] = current_finished_task['current_resources']

    def has_available_resources_to_process_task(self, processor, task):
        task_can_be_processed = True
        for type, value in processor.items():
            if (processor[type] - task[type] < 0):
                task_can_be_processed = False
        return task_can_be_processed


