import json, yaml
from TaskGenerator.TaskGenerator import TaskGenerator

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

    """ resources are randomly generated, for each task, by a specified distribution"""
    resources_distributions = ['uniform', 'normal']
    """ for each specified distribution we create a file in 'GeneratedTasks' directory that contains number of task specified """
    for resources_distribution in resources_distributions:
        """ instance of task generator is created for each distribution """
        taskGenerator = TaskGenerator(number_of_tasks, resources_distribution, resources_max_values)
        f = open("GeneratedTasks/%s.json" % resources_distribution, "w+")
        f.write(json.dumps(taskGenerator.get_tasks(), indent=4))
        f.close()
