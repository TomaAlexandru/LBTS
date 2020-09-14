from .ProcessorGenerator.Queue import Queue
from .ProcessorGenerator.Scheduler import Scheduler
from .ProcessorGenerator.SystemArchitecture import SystemArchitecture
import simpy

""" class extends simpy environment in order to use features of simulation from the parent class"""
class SimulationEnvironment(simpy.Environment):
    def __init__(self, tasks, number_of_task_processors, task_processor_resource,
                 task_resources_distribution_name, algorithm):
        """ parent class is also instantiated """
        super().__init__()
        """ assign properties for the current instance of environment """
        self.tasks = tasks
        self.number_of_tasks = len(self.tasks)
        self.taskProducer_queue_pipe = simpy.Store(self)
        self.queue = Queue(self)
        self.task_resources_distribution_name = task_resources_distribution_name
        self.algorithm = algorithm

        """ omogen / heterogeneous computing units """
        systemArchitecture = SystemArchitecture('omogen', number_of_task_processors, task_processor_resource)
        self.taskProcessors = systemArchitecture.get_task_processor_resources_list()
        self.scheduler = Scheduler(self)

        """ TaskProducer -> Queue """
        self.process(self.simulate())

    """ TASKS ARE PUSHED INTO QUEUE - to simulate arrival of task in system """
    def simulate(self):
        while True:
            tasks = [t for t in self.tasks if t['time_arrival'] == self.now]
            self.scheduler.schedule_tasks(tasks)
            yield self.timeout(1)
