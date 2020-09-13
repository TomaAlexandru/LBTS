import json, yaml
from TaskGenerator.TaskGenerator import TaskGenerator
from TaskGenerator.StochasticVariables.Distribution import Distribution

def get_all_subclasses(cls):
    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses

""" setup file is read for task and timeline information regarding maximum value that can be generated """
with open(r'setup_file.yaml') as file:
    setup_data = yaml.load(file, Loader=yaml.FullLoader)
    """ setup file contains also information regarding task processors, thus we will get only the information
        by referencing 'generate' key from file"""
    generate_data = setup_data['generate']

    """GENERATING TASKS"""

    """ number of tasks to generate for simulation """
    number_of_tasks = generate_data['number_of_tasks']
    """ maximum value of resources for each task """
    resources_max_values = generate_data['max_values_for_task_parameters']

    """ instance of task generator is created for each distribution """
    taskGenerator = TaskGenerator(number_of_tasks)

    """ for each specified distribution we create a file in 'GeneratedTasks' directory that contains number of task specified """
    for distribution in Distribution.__subclasses__():
        f = open("GeneratedTasks/%s.json" % distribution.__name__.lower(), "w+")
        f.write(json.dumps(taskGenerator.get_tasks(distribution(resources_max_values)), indent=4))
        f.close()
