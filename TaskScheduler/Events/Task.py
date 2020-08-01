import simpy

class Task(simpy.events.Event):
    def __init__(self, env, cpu, memory, disk, time_arrival, time_processing):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk
        self.time_arrival = time_arrival
        self.time_processing = time_processing