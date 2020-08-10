from os import listdir
from os.path import isfile, join
import json, csv
import numpy as np

with open('Reports/_overview.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['HEURISTIC', 'MAKESPAN', 'AVERAGE TIME OF JOB', 'LATENESS', 'SLA VIOLATION'])


    reportFiles = [f for f in listdir("Reports") if isfile(join("Reports", f))]

    for reportFile in reportFiles:
        if 'overview' in reportFile:
            continue
        file = open("Reports/%s" % reportFile, "r")
        tasks = json.loads(file.read())
        performance_evaluations_criterion = []

        # heuristic
        performance_evaluations_criterion.append(reportFile.split('.')[0])

        # makespan
        performance_evaluations_criterion.append(max([t['task']['finished_at'] for t in tasks]))

        # average_time_of_jobs
        performance_evaluations_criterion.append(np.mean([t['task']['waiting_time'] + t['task']['time_processing'] for t in tasks]))

        # lateness
        performance_evaluations_criterion.append(sum([t['task']['waiting_time'] for t in tasks]))

        # sla_violation
        performance_evaluations_criterion.append(sum([t['task']['sla_violation'] for t in tasks]))

        csvwriter.writerow(performance_evaluations_criterion)
        for task in tasks:
            pass
