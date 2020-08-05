from .ProcessorGenerator.Queue import Queue
from .ProcessorGenerator.Scheduler import Scheduler
import simpy

class SimulationEnvironment(simpy.Environment):

    def __init__(self, tasks, number_of_task_processors, task_processor_resource, number_of_tasks,
                 task_resources_distributions, heuristic):
        super().__init__()
        self.tasks = tasks
        self.number_of_task_processors = number_of_task_processors
        self.task_processor_resource = task_processor_resource
        self.number_of_tasks = number_of_tasks

        self.taskProducer_queue_pipe = simpy.Store(self)

        self.queue = Queue(self)
        self.scheduler = Scheduler(self, heuristic)


        self.task_resources_distributions = task_resources_distributions
        self.heuristic = heuristic

        """ TaskProducer -> Queue """
        self.process(self.task_reception())

    """ TASKS ARE PUSHED INTO QUEUE """
    def task_reception(self):
        while True:
            tasks = [t for t in self.tasks if t['time_arrival'] == self.now]
            self.scheduler.schedule_tasks(tasks, self.task_resources_distributions)
            yield self.timeout(1)
