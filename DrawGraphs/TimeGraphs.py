import json, math, random
import matplotlib.pyplot as plt

file = open("../GeneratedTasks/uniform.json", "r")
taskUniform = json.loads(file.read())

file = open("../GeneratedTasks/normal.json", "r")
taskNormal = json.loads(file.read())

time_arrival_uniform = [t['time_arrival'] for t in taskUniform]
time_arrival_normal = [t['time_arrival'] for t in taskNormal]


time_arrival_uniform = {item:time_arrival_uniform.count(item) for item in time_arrival_uniform}
time_arrival_normal = {item:time_arrival_normal.count(item) for item in time_arrival_normal}


fig, axs = plt.subplots(1, 2, figsize=(9, 3), sharey=False, gridspec_kw={'hspace': 0})
axs[0].bar(list(time_arrival_uniform.keys()), list(time_arrival_uniform.values()))
axs[0].set_title('Uniform')
axs[1].bar(list(time_arrival_normal.keys()), list(time_arrival_normal.values()))
axs[1].set_title('Normal')

# fig.suptitle('Resources - Normal Distribution\n\n')
fig.savefig('TimeGraphs.png')
# plt.savefig('test.png')
plt.show()