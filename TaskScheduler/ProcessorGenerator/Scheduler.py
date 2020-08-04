from .TaskProcessor import TaskProcessor
import simpy, json

class Scheduler:
    def __init__(self, env, heuristic):
        self.env = env
        self.env.scheduler_processor_pipe = simpy.Store(self.env)
        self.tasksProcessor = []
        self.out_pipes = []
        self.in_pipes = []
        self.finished_tasks = []
        self.heuristicInstance = heuristic()
        self.finished_tasks = []
        for i in range(self.env.number_of_task_processors):
            out_pipe = simpy.Store(self.env)
            in_pipe = simpy.Store(self.env)
            taskProcessor = TaskProcessor(self.env, i, out_pipe, in_pipe)
            self.tasksProcessor.append(taskProcessor)
            self.out_pipes.append(out_pipe)
            self.in_pipes.append(in_pipe)

    def schedule_tasks(self, tasks, task_resources_distributions, current_time):
        for taskProc in self.tasksProcessor:
            taskProc.now = current_time

        """ schedulling tasks this unit time """
        self.heuristicInstance.schedule(self.out_pipes, tasks, self.env.number_of_task_processors)

        for i in range(self.env.number_of_task_processors):
            self.tasksProcessor[i].run()

        """ TASK RECEPTION """
        for in_pipe in self.in_pipes:
            self.finished_tasks = self.finished_tasks+in_pipe.items
            in_pipe.items=[]
            """ OPERATION FINISHED """
            if self.env.number_of_tasks == len(self.finished_tasks):
                with open("Reports/%s_%s.json" % (task_resources_distributions, self.heuristicInstance.__str__()), "w") as twitter_data_file:
                    json.dump(self.finished_tasks, twitter_data_file, indent=4, sort_keys=True)
                raise Exception(task_resources_distributions, self.heuristicInstance.__str__())

    def has_processing_resources(self):
        for i in range(self.env.number_of_task_processors):
            return True
        return False