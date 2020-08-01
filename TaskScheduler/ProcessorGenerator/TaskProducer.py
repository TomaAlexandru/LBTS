from .Task import Task

class TaskProducer:
    def __init__(self, env):
        self.env = env

    def send_tasks(self, tasks):
        while True:
            taskChunk = []
            currentTime = self.env.now
            for task in tasks:
                if task['time_arrival'] == currentTime:
                    taskChunk.append(task)
                else:
                    break
            tasks = tasks[len(taskChunk):]
            self.env.taskProducer_queue_pipe.put(taskChunk)
            yield self.env.timeout(1)


