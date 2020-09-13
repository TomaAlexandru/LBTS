import json
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

    """ to be disregard """
    """ basic example, with hardcoded values, of shortest processing time algorithm """
    def display_timeline_spt(self):
        """ job names """
        jobs = ['T1', 'T2', 'T3', 'T4', 'T5']

        """ 5 jobs to process in a unit of time """
        waittimes = [1, 4, 12, 16, 10]
        runtimes = [4, 7, 5, 6, 3]

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