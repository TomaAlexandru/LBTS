from .TaskProcessor import TaskProcessor
import simpy


""" Task Scheduler """
class Scheduler:
    def __init__(self, env):
        """ assign to the current value, necessary properties """
        self.env = env
        self.taskProcessors = []
        self.out_pipes = []
        self.in_pipes = []
        self.finished_tasks = []
        self.buffer = []
        self.task_resources_distribution_name = env.task_resources_distribution_name

        """ for each task processor assign necessary properties """
        for i in range(len(self.env.taskProcessors)):

            """ out pipe is a resource used to send information from scheduler to task processor """
            out_pipe = simpy.Store(self.env)

            """ out pipe is a resource used to send information from task processor to scheduler """
            in_pipe = simpy.Store(self.env)

            """ we create task processor instance as specified in setup file """
            taskProcessor = TaskProcessor(self.env, i, out_pipe, in_pipe)

            """ append tasks processor to a list in order to operate on it from the schedule algorithm """
            self.taskProcessors.append(taskProcessor)
            self.in_pipes.append(in_pipe)
        self.algorithmInstance = env.algorithm(self.taskProcessors)

    """ method executed every time unit """
    def schedule_tasks(self, tasks):
        self.buffer = tasks[::-1] + self.buffer

        """ PROCESS TASKS """
        for i in range(len(self.env.taskProcessors)):
            self.taskProcessors[i].process_tasks()

        """ RECEIVE TASK PROCESSORS FINISHED TASKS """
        self.algorithmInstance.task_reception(self.env.number_of_tasks, self.task_resources_distribution_name, self.in_pipes)

        """ SCHEDULE TASKS """
        self.algorithmInstance.schedule(self.buffer, self.env.now)
