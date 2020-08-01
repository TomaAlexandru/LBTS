from .TaskProcessor import TaskProcessor
from ..Heuristics import *
import simpy, time, json


class Scheduler:
    def __init__(self, env):
        self.env = env

    def schedule_tasks(self):
        self.env.scheduler_processor_pipe = simpy.Store(self.env)
        tasksProcessor = []
        self.out_pipes = []
        self.in_pipes = []
        self.finished_tasks = []
        current_task_iterator = 0
        for i in range(self.env.number_of_task_processors):
            out_pipe = simpy.Store(self.env)
            in_pipe = simpy.Store(self.env)
            taskProcessor = TaskProcessor(self.env, i, out_pipe, in_pipe)
            tasksProcessor.append(taskProcessor)
            self.out_pipes.append(out_pipe)
            self.in_pipes.append(in_pipe)
            self.env.process(taskProcessor.run())
        while True:
            tasks = yield self.env.queue.get()
            for taskProc in tasksProcessor:
                taskProc.now = self.env.now -1

            """ schedulling tasks this unit time """
            """ ROUND ROBIN """
            for task in tasks:
                current_task_iterator = (current_task_iterator + 1) % self.env.number_of_task_processors
                self.out_pipes[current_task_iterator].put(task)

            """ TASK RECEPTION """
            for in_pipe in self.in_pipes:
                while in_pipe.items:
                    finished_task = yield in_pipe.get()
                    print(finished_task)
                    self.finished_tasks.append(finished_task)

                    """ OPERATION FINISHED """
                    if self.env.number_of_tasks == len(self.finished_tasks):
                        with open("finished_tasks.json", "w") as twitter_data_file:
                            json.dump(self.finished_tasks, twitter_data_file, indent=4, sort_keys=True)
                        exit()



    def has_processing_resources(self):
        for i in range(self.env.number_of_task_processors):
            return True
        return False