import numpy as np

class TaskProcessor(dict):
    def __init__(self, index, in_pipe, out_pipe, task_processor_resource):
        super().__init__()
        self.index = index
        self.in_pipe = in_pipe
        self.out_pipe = out_pipe
        self.has_resources = True

        for type, value in task_processor_resource.items():
            self[type] = value

        self.in_processing_tasks = []
        self.pending_tasks = []
        self.now = None


    """ after processing time release task and processor resources """
    def process_tasks(self):
        current_finished_tasks = []
        for i, task in enumerate(self.in_processing_tasks):
            if task['time_arrival'] + task['waiting_time'] + task['time_processing'] <= self.now:
                """ release resources """
                self.release_resources(task)
                current_finished_tasks.append(i)
        self.in_processing_tasks = list(np.delete(self.in_processing_tasks, current_finished_tasks))

    """ reserve resource from current task processor """
    def reserve_resources(self, task):
        task['waiting_time'] = self.now - task['time_arrival']
        for type, value in self.items():
            self[type] = self[type] - task[type]
        task['current_resources_after_reserve'] = self.copy()
        self.in_processing_tasks.append(task)

    """ release resource from current task processor """
    def release_resources(self, task):
        for type, value in self.items():
            self[type] = self[type] + task[type]
        task['finished_at'] = task['time_arrival'] + task['waiting_time'] + task['time_processing']
        self.out_pipe.put(
            {
                'processor_index': self.index,
                'task': task,
                'current_resources_after_finished': self.copy()
            }
        )
