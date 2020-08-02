from .ProcessorGenerator.TaskProducer import TaskProducer
from .ProcessorGenerator.Queue import Queue
from .ProcessorGenerator.Scheduler import Scheduler
import simpy

class SimulationEnvironment(simpy.Environment):

    performance_evaluations_criterion = [
        'makespan', # total time to completely process all jobs
        'average_time_of_jobs',
        'lateness',
        'average_name_of_jobs_pending',
        'utilization_of_machines'
    ]

    def __init__(self, tasks, number_of_task_processors, task_processor_resource, number_of_tasks):
        super().__init__()
        self.tasks = tasks
        self.number_of_task_processors = number_of_task_processors
        self.task_processor_resource = task_processor_resource
        self.number_of_tasks = number_of_tasks

        self.taskProducer_queue_pipe = simpy.Store(self)

        self.queue = Queue(self)
        self.scheduler = Scheduler(self)

        self.taskProducer = TaskProducer(self)

        """ TaskProducer -> Queue """
        self.process(self.task_reception())
        self.process(self.taskProducer.send_tasks(tasks))
        self.process(self.scheduler.schedule_tasks())

    """ TASKS ARE PUSHED INTO QUEUE """
    def task_reception(self):
        while True:
            tasks = yield self.taskProducer_queue_pipe.get()
            self.queue.put(tasks)
