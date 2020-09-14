class SystemArchitecture:
    """ omogen / eterogen """
    def __init__(self, type, number_of_task_processors, task_processor_resource):
        self.type = type
        self.number_of_task_processors = number_of_task_processors
        self.task_processor_resource = task_processor_resource

    def get_task_processor_resources_list(self):
        if self.type == 'omogen':
            task_processors = []
            for i in range(self.number_of_task_processors):
                task_processors.append(self.task_processor_resource)
            return task_processors