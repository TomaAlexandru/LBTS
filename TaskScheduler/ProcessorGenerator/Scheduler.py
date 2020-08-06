from .TaskProcessor import TaskProcessor
import simpy, json

class Scheduler:
    def __init__(self, env, heuristic):
        self.env = env
        self.env.scheduler_processor_pipe = simpy.Store(self.env)
        self.taskProcessors = []
        self.out_pipes = []
        self.in_pipes = []
        self.finished_tasks = []

        self.finished_tasks = []
        self.buffer = []
        for i in range(self.env.number_of_task_processors):
            out_pipe = simpy.Store(self.env)
            in_pipe = simpy.Store(self.env)
            taskProcessor = TaskProcessor(self.env, i, out_pipe, in_pipe)
            self.taskProcessors.append(taskProcessor)
            self.out_pipes.append(out_pipe)
            self.in_pipes.append(in_pipe)
        self.heuristicInstance = heuristic(self.taskProcessors)

    """ method executed every time unit """
    def schedule_tasks(self, tasks, task_resources_distributions):
        self.buffer = tasks[::-1] + self.buffer

        """ SCHEDULE TASKS """
        self.heuristicInstance.schedule(self.buffer, self.env.now)

        """ PROCESS TASKS """
        for i in range(self.env.number_of_task_processors):
            self.taskProcessors[i].process_tasks()

        """ RECEIVE TASK PROCESSORS FINISHED TASKS """
        self.heuristicInstance.task_reception(self.env.number_of_tasks, task_resources_distributions, self.in_pipes)





    def has_processing_resources(self):
        for i in range(self.env.number_of_task_processors):
            return True
        return False