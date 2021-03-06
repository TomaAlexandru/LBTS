from .Algorithm import Algorithm


""" This algorithm is designed to calculate urgency of a task and process them in specific order 
the less is critical ration, the bigger the urgency"""
class CriticalRatio(Algorithm):
    def __init__(self, tasksProcessor):
        self.parent = super().__init__(tasksProcessor)
        self.current_task_iterator = 0
        self.finished_tasks = []
        self.number_of_task_processors = len(tasksProcessor)

    def schedule(self, buffer, now):
        currently_no_processor_available = False

        if len(buffer) > 0:
            """ take task from buffer one by one """
            self.compute_critical_ratio(buffer, now)
            """ sort by critical ratio descending """
            buffer.sort(key=lambda e: e["critical_ratio"], reverse=True)

        while len(buffer) > 0:
            """ loop with a single task in processor cluster and try to schedule """
            for processor_index in range(0, self.number_of_task_processors):
                task_scheduled = False
                """ IF WE FIND AVAILABLE PROCESSOR WE REMOVE FROM BUFFER AND MARK INNER ITERATION FOR BREAK """
                if self.has_available_resources_to_process_task(self.processors[self.current_task_iterator],
                                                                buffer[-1]):
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

    """ compute critical ration for each task """
    def compute_critical_ratio(self, buffer, now):
        for task in buffer:
            task['critical_ratio'] = (task['due_time'] - now) / task['time_processing']

    def __str__(self):
        return 'criticalRatio'