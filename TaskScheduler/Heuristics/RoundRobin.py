from .Heuristics import Heuristics

class RoundRobin(Heuristics):
    def __init__(self, tasksProcessor):
        self.parent = super().__init__(tasksProcessor)
        self.current_task_iterator = 0
        self.finished_tasks = []
        self.number_of_task_processors = len(tasksProcessor)

    def schedule(self, buffer):
        currently_no_processor_available = False
        """ take task from buffer one by one """
        while len(buffer) > 0:
            """ loop with a single task in processor cluster and try to schedule """
            for processor_index in range(0, self.number_of_task_processors):
                task_scheduled = False
                """ IF WE FIND AVAILABLE PROCESSOR WE REMOVE FROM BUFFER AND MARK INNER ITERATION FOR BREAK """
                if RoundRobin.has_available_resources_to_process_task(self.processors[self.current_task_iterator], buffer[-1]):
                    self.processors[self.current_task_iterator].reserve_resources(buffer[-1])
                    del buffer[-1]
                    task_scheduled = True
                self.current_task_iterator = (self.current_task_iterator + 1) % self.number_of_task_processors
                """ IF TASK WAS SCHEDULED GO TO NEXT TASK -> THUS OUTER LOOP """
                if task_scheduled:
                    break
                """ CURRENTLY NO RESOURCE AVAILABLE - WE CHECKED ALL PROCESSORS """
                if processor_index == self.number_of_task_processors - 1:
                    currently_no_processor_available = True

            if currently_no_processor_available:
                break



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