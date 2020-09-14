"""
This module is designed to evaluate performance of algorithms by reading data from Reports directory
"""

from os import listdir
from os.path import isfile, join
import json, csv
import numpy as np

""" we open an overview.csv file """
with open('Reports/overview.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    """ we create a header of table """
    csvwriter.writerow(['RESOURCE DISTRIBUTION', 'ALGORITHM', 'MAKESPAN', 'AVERAGE TIME OF JOB', 'LATENESS', 'SLA VIOLATION'])

    reportFiles = [f for f in listdir("Reports") if isfile(join("Reports", f))]

    """ for each file from reports we compute mean of the most important metrics """
    for reportFile in reportFiles:
        if 'overview' in reportFile:
            continue
        file = open("Reports/%s" % reportFile, "r")
        tasks = json.loads(file.read())
        performance_evaluations_criterion = []

        # heuristic
        performance_evaluations_criterion.append(reportFile.split('.')[0].split("_")[0])

        performance_evaluations_criterion.append(reportFile.split('.')[0].split("_")[1])

        # makespan
        performance_evaluations_criterion.append(max([t['task']['finished_at'] for t in tasks]))

        # average_time_of_jobs
        performance_evaluations_criterion.append(int(np.mean([t['task']['waiting_time'] + t['task']['time_processing'] for t in tasks])))

        # lateness
        performance_evaluations_criterion.append(int(np.mean([t['task']['waiting_time'] for t in tasks])))

        # sla_violation
        performance_evaluations_criterion.append(int(np.mean([t['task']['sla_violation'] for t in tasks])))

        # write data
        csvwriter.writerow(performance_evaluations_criterion)

