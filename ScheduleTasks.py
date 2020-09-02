import json, yaml
from TaskScheduler.SimulationEnvironment import SimulationEnvironment
from os import listdir
from os.path import isfile, join
from TaskScheduler.Heuristics.RoundRobin import RoundRobin
from TaskScheduler.Heuristics.Random import Random
from TaskScheduler.Heuristics.ShortestProcessingTime import ShortestProcessingTime
from TaskScheduler.Heuristics.EarliestDueTime import EarliestDueTime
from TaskScheduler.Heuristics.CriticalRatio import CriticalRatio

""" scheduling algorithms """
scheduling_algorithms = [
        Random,
        RoundRobin,
        ShortestProcessingTime,
        EarliestDueTime,
        CriticalRatio
    ]

""" read setup file for environment data """
with open(r'setup_file.yaml') as file:
    setup_data = yaml.load(file, Loader=yaml.FullLoader)
    """ get only data regarding process system """
    process_data  = setup_data['process']

    """ PROCESSING TASKS """
    number_of_tasks = setup_data["generate"]["number_of_tasks"]
    number_of_task_processors = process_data['number_of_task_processors']
    task_processor_resources = process_data['max_values_for_task_processor_parameters']

    """ get all generated task file """
    taskFiles = [f for f in listdir("GeneratedTasks") if isfile(join("GeneratedTasks", f))]

    """ scheduler environment is created for every generated tasks file """
    for taskFile in taskFiles:
        task_resources_distributions = taskFile.split(".")[0]

        for heuristic in scheduling_algorithms:
            file = open("GeneratedTasks/%s.json" % task_resources_distributions, "r")
            tasks = json.loads(file.read())
            try:
                """ create simulation environment """
                scheduler = SimulationEnvironment(
                    tasks,
                    number_of_task_processors,
                    task_processor_resources,
                    number_of_tasks,
                    task_resources_distributions,
                    heuristic)
                scheduler.run()
            except Exception as e:
                print(e)
