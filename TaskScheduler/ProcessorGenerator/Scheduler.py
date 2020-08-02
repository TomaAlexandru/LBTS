from .TaskProcessor import TaskProcessor
from ..Heuristics import *
import simpy, time, json
from ..Heuristics.RoundRobin import RoundRobin
from ..Heuristics.Random import Random
from ..Heuristics.ShortestProcessingTime import ShortestProcessingTime
from simpy.core import StopSimulation

class Scheduler:
    def __init__(self, env):
        self.env = env
        self.round_robin = RoundRobin()
        self.random = Random()
        self.shortest_processing_time = ShortestProcessingTime()

    def schedule_tasks(self, task_resources_distributions):
        self.env.scheduler_processor_pipe = simpy.Store(self.env)
        tasksProcessor = []
        self.out_pipes = []
        self.in_pipes = []
        self.finished_tasks = []
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
            self.shortest_processing_time.schedule(self.out_pipes, tasks, self.env.number_of_task_processors)

            """ TASK RECEPTION """
            for in_pipe in self.in_pipes:
                while in_pipe.items:
                    finished_task = yield in_pipe.get()
                    self.finished_tasks.append(finished_task)

                    """ OPERATION FINISHED """
                    if self.env.number_of_tasks == len(self.finished_tasks):
                        with open("Reports/%s.json" % task_resources_distributions, "w") as twitter_data_file:
                            json.dump(self.finished_tasks, twitter_data_file, indent=4, sort_keys=True)
                        raise Exception('spam', 'eggs')



    def has_processing_resources(self):
        for i in range(self.env.number_of_task_processors):
            return True
        return False