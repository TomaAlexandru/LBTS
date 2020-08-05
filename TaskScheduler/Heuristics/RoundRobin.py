import json
from .Heuristics import Heuristics
import numpy as np

class RoundRobin(Heuristics):
    def __init__(self, tasksProcessor):
        self.parent = super().__init__(tasksProcessor)
        self.current_task_iterator = 0
        self.finished_tasks = []
        self.number_of_task_processors = len(tasksProcessor)

    def schedule(self, out_pipes, buffer):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(len(buffer))
        while len(buffer) > 0:
            last_entry = buffer[-1]
            task_scheduled = False
            for processor_index in range(0, self.number_of_task_processors):
                if len(buffer) == 0:
                    break
                print(self.current_task_iterator)
                # if RoundRobin.has_available_resources_to_process_task(self.processors[self.current_task_iterator],
                #                                                       last_entry):
                #     self.processors[self.current_task_iterator].reserve_resources(last_entry)

                del buffer[-1]
                # else:
                #     self.processors[self.current_task_iterator].has_resources = False
                self.current_task_iterator = (self.current_task_iterator + 1) % self.number_of_task_processors



            # chck = 0
            # for pin in self.processors:
            #     print(pin)
            #     if pin.has_resources == False:
            #         chck = chck +1
            # if chck == len(self.processors):
            #     break




    @staticmethod
    def has_available_resources_to_process_task(processor, task):
        task_can_be_processed = True
        for type, value in processor.items():
            if (processor[type] - task[type] < 0):
                task_can_be_processed = False
        return task_can_be_processed

    def __str__(self):
        return 'roundRobin'