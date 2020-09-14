""" this module is used for generating graphs for generated data """

from DataVisualization.TaskData import TaskData
import sys

args = sys.argv

""" class contains methods that process and plot graphs for generated data """
taskData = TaskData()

""" plot resource distribution over generated task resources """
if args[1] == 'distribution':
    taskData.display_resources_distribution(args[2])

elif args[1] == 'timeline':
    """ plot timeline, ex: of shortest processing time algorithm """
    taskData.display_timeline(
        ['T1', 'T2', 'T3', 'T4', 'T5'],
        [1, 4, 12, 16, 10],
        [4, 7, 5, 6, 3]
    )



elif args[1] == 'performance':
    """ plot time of arrival bar chart """
    taskData.display_performance_evaluation()

elif args[2] == 'arrival_time':
    """ plot time of arrival bar chart """
    taskData.task_arrival_time()

else:
    print('Command not found')