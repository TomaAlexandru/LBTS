import json, yaml, sys
from TaskScheduler.SimulationEnvironment import SimulationEnvironment
from os import listdir
from os.path import isfile, join

with open(r'setup_file.yaml') as file:
    setup_data = yaml.load(file, Loader=yaml.FullLoader)
    process_data  = setup_data['process']

    """ PROCESSING TASKS """
    number_of_tasks = setup_data["generate"]["number_of_tasks"]
    number_of_task_processors = process_data['number_of_task_processors']
    task_processor_resources = process_data['max_values_for_task_processor_parameters']

    taskFiles = [f for f in listdir("GeneratedTasks") if isfile(join("GeneratedTasks", f))]
    # scheduler is created for every generated tasks file
    # intermittent arrival
    schedulers = {}
    for taskFile in taskFiles:
        task_resources_distributions = taskFile.split(".")[0]
        file = open("GeneratedTasks/%s.json" % task_resources_distributions, "r")
        tasks = json.loads(file.read())

        scheduler = SimulationEnvironment(tasks, number_of_task_processors, task_processor_resources, number_of_tasks)
        scheduler.run()

