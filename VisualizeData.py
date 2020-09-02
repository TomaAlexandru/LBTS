""" this module is used for generating graphs for generated data """

from DataVisualization.TaskData import TaskData

""" class contains methods that process and plot graphs for generated data """
taskData = TaskData()

""" plot resource distribution over generated task resources """
taskData.display_resources_distribution('normal')

""" plot resource distribution over generated task resources """
taskData.display_resources_distribution('uniform')

""" plot timeline of shortest processing time algorithm """
taskData.display_timeline_spt()

""" plot time of arrival bar chart """
taskData.task_arrival_time()