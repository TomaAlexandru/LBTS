import numpy as np
import simpy, json, copy

class TaskProcessor(dict):
    def __init__(self, env, index, in_pipe, out_pipe):
        super().__init__()
        self.env = env
        self.index = index
        self.in_pipe = in_pipe
        self.out_pipe = out_pipe
        self.set_current_resources()
        self.in_processing_tasks = []
        self.pending_tasks = []
        self.env.process(self.process_tasks())
        self.buffer = []
    def set_current_resources(self):
        for type, value in self.env.task_processor_resource.items():
            self[type] = value

    def run(self):
        while True:
            self.now = self.env.now
            while len(self.in_pipe.items) > 0:
                """ TASK RECEPTION """
                task = yield self.in_pipe.get()
                self.buffer = [task] + self.buffer

            """ CHECK LAST ENTRIES TO SEE IF ANY TASK CAN BE PROCESSED """
            if len(self.buffer) > 0:
                last_entry_time = self.buffer[-1]['time_arrival']
                last_entries = [e for e in self.buffer if e['time_arrival'] == last_entry_time]
                for i, last_entry in enumerate(last_entries):
                    if self.has_available_resources_to_process_task(last_entry):
                        self.reserve_resources(last_entry)
                        del self.buffer[-(len(last_entries) - i)]
            # print(self.index, "--",len(self.buffer), "||", + len(self.in_processing_tasks))
            yield self.env.timeout(1)

    def has_available_resources_to_process_task(self, task):
        task_can_be_processed = True
        for type, value in self.items():
            if (self[type] - task[type] < 0):
                task_can_be_processed = False
        return task_can_be_processed

    """ after processing time release task and processor resources """
    def process_tasks(self):
        while True:
            current_finished_tasks = []
            for i, task in enumerate(self.in_processing_tasks):
                if task['time_arrival'] + task['time_processing'] <= self.env.now:
                    """ release resources """
                    self.release_resources(task)
                    current_finished_tasks.append(i)
            self.in_processing_tasks = list(np.delete(self.in_processing_tasks, current_finished_tasks))
            yield self.env.timeout(1)

    """ reserve resource from current task processor """
    def reserve_resources(self, task):
        for type, value in self.items():
            self[type] = self[type] - task[type]
        self.in_processing_tasks.append(task)

    """ release resource from current task processor """
    def release_resources(self, task):
        for type, value in self.items():
            self[type] = self[type] + task[type]
        task['waiting_time'] = self.env.now - task['time_arrival'] - task['time_processing']
        task['finished_at'] = self.env.now
        task['processor_index'] = self.index
        self.out_pipe.put({'task': task, 'current_resources': self.copy()})
