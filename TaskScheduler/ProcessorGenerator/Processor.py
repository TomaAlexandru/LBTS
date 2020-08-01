class Processor:
    resources_names = ["cpu", "memory", "disk", "time_arrival", "time_processing"]
    cpu    = None
    memory = None
    disk   = None

    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk