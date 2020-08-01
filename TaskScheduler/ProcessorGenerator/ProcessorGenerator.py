from TaskGenerator.Distribution import Distribution

class ProcessorGenerator:
    number_of_taskProcessors = None
    resources_distribution   = None
    resources_max_values     = None

    def __init__(self, number_of_taskProcessors, resources_distribution, resources_max_values):
        self.number_of_taskProcessors = number_of_taskProcessors
        self.resources_distribution   = resources_distribution
        self.resources_max_values     = resources_max_values

    def get_task_processors(self):
        taskProcessors = []
        # generate taskProcessor
        for i in range(self.number_of_taskProcessors):
            distribution = Distribution(self.resources_distribution, self.resources_max_values)
            taskProcessors.append(distribution.get_generated_values())
        return taskProcessors