class Task(dict):
    def __init__(self, task_resources):
        super().__init__()
        self['cpu'] = task_resources['cpu']
        self['memory'] = task_resources['memory']
        self['disk'] = task_resources['disk']
        self['time_arrival'] = task_resources['time_arrival']
        self['time_processing'] = task_resources['time_processing']

        self.waiting_time = None
        self.finished_at = None