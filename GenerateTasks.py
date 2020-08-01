import json, yaml
from TaskGenerator.TaskGenerator import TaskGenerator

with open(r'setup_file.yaml') as file:
    setup_data = yaml.load(file, Loader=yaml.FullLoader)
    generate_data = setup_data['generate']

    """GENERATING TASKS"""
    number_of_tasks = generate_data['number_of_tasks']
    resources_max_values = generate_data['max_values_for_task_parameters']

    resources_distributions = ['uniform', 'normal']
    for resources_distribution in resources_distributions:
        taskGenerator = TaskGenerator(number_of_tasks, resources_distribution, resources_max_values)
        f = open("GeneratedTasks/%s.json" % resources_distribution, "w+")
        f.write(json.dumps(taskGenerator.get_tasks(), indent=4))
        f.close()
