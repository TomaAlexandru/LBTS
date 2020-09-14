import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TaskData:

    """ plot resource distribution of tasks resources """
    def display_resources_distribution(self, distribuion):
        """ get data from generated tasks to build plot """
        file = open("GeneratedTasks/%s.json" % distribuion, "r")
        tasks = json.loads(file.read())

        """ get resources, by type, as list """
        cpus = [t['cpu'] for t in tasks]
        disk = [t['disk'] for t in tasks]
        memory = [t['memory'] for t in tasks]

        """ compute amount of each value of resource """
        cpus = {item:cpus.count(item) for item in cpus}
        disk = {item:disk.count(item) for item in disk}
        memory = {item:memory.count(item) for item in memory}

        """ build plot: in a single display we have 3 plots - for each type of resource """
        fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=False)
        axs[0].bar(list(cpus.keys()), list(cpus.values()))
        axs[0].set_title('CPU')
        axs[1].bar(list(disk.keys()), list(disk.values()))
        axs[1].set_title('DISK')
        axs[2].bar(list(memory.keys()), list(memory.values()))
        axs[2].set_title('MEMORY')
        plt.show()

    """ basic example, ex: of shortest processing time algorithm
        job names
        n jobs to process in a unit of time """
    def display_timeline(self, jobs, waittimes, runtimes):
        """ build timeline chart by above data """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.barh(jobs, waittimes, align='center', height=.25, color='#FFFFFF', label='wait time')
        ax.barh(jobs, runtimes, align='center', height=.25, left=waittimes, color='g', label='run time')
        ax.set_yticks(jobs)
        ax.set_xlabel('Time')
        ax.set_title('Run Time by P')
        ax.grid(True)
        plt.tight_layout()
        plt.show()

    """ for each distribution build barchart, in a single image, for task arrival time """
    def task_arrival_time(self):
        """ read files for tasks """
        file = open("GeneratedTasks/uniform.json", "r")
        taskUniform = json.loads(file.read())

        file = open("GeneratedTasks/normal.json", "r")
        taskNormal = json.loads(file.read())

        """ get arrival time as list """
        time_arrival_uniform = [t['time_arrival'] for t in taskUniform]
        time_arrival_normal = [t['time_arrival'] for t in taskNormal]

        """ count number of tasks for each arrival time unit """
        time_arrival_uniform = {item: time_arrival_uniform.count(item) for item in time_arrival_uniform}
        time_arrival_normal = {item: time_arrival_normal.count(item) for item in time_arrival_normal}

        """ plot. for each time distribution, barchart """
        fig, axs = plt.subplots(1, 2, figsize=(9, 3), sharey=False, gridspec_kw={'hspace': 0})
        axs[0].bar(list(time_arrival_uniform.keys()), list(time_arrival_uniform.values()))
        axs[0].set_title('Uniform')
        axs[1].bar(list(time_arrival_normal.keys()), list(time_arrival_normal.values()))
        axs[1].set_title('Normal')
        plt.show()

    def display_performance_evaluation(self):

        # This next line makes our charts show up in the notebook

        table = pd.read_csv("Reports/overview.csv")

        # Create our bar chart as before
        plt.bar(x=np.arange(1, 11), height=table['LATENESS'])

        # Give it a title
        plt.title("Performance Evaluation")

        # Give the x axis some labels across the tick marks.
        # Argument one is the position for each label
        # Argument two is the label values and the final one is to rotate our labels
        plt.xticks(np.arange(1, 11), table['ALGORITHM'], rotation=90)

        # Give the x and y axes a title
        plt.xlabel("ALGORITHM")
        plt.ylabel("LATENESS")

        # Finally, show me our new plot
        plt.show()