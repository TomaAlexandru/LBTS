import json, yaml
from TaskScheduler.SimulationEnvironment import SimulationEnvironment
from os import listdir
from os.path import isfile, join
from TaskScheduler.Algorithms.Algorithm import Algorithm
from TaskScheduler.Exceptions.TerminatedException import TerminatedException

""" read setup file for environment data """
with open(r'setup_file.yaml') as file:
    setup_data = yaml.load(file, Loader=yaml.FullLoader)
    """ get only data regarding process system """
    process_data = setup_data['process']

    """ PROCESSING TASKS """
    number_of_task_processors = process_data['number_of_task_processors']
    task_processor_resources = process_data['max_values_for_task_processor_parameters']

    """ get all generated task file """
    taskFiles = [f for f in listdir("GeneratedTasks") if isfile(join("GeneratedTasks", f))]

    """ scheduler environment is created for every generated tasks file """
    for taskFile in taskFiles:
        task_resources_distributions = taskFile.split(".")[0]
        file = open("GeneratedTasks/%s.json" % task_resources_distributions, "r")
        tasks = json.loads(file.read())

        """ a file is created for each combination of distribution / algorithm """
        for algorithm in Algorithm.__subclasses__():
            """ create simulation environment """
            scheduler = SimulationEnvironment(
                tasks,
                number_of_task_processors,
                task_processor_resources,
                task_resources_distributions,
                algorithm)

            try:
                scheduler.run()
            except TerminatedException as e:
                print(e.get_message())
            except Exception as e:
                print(e)
