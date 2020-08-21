import json, math, random
import matplotlib.pyplot as plt

file = open("../GeneratedTasks/uniform.json", "r")
tasks = json.loads(file.read())

cpus = [t['cpu'] for t in tasks]
disk = [t['disk'] for t in tasks]
memory = [t['memory'] for t in tasks]


cpus = {item:cpus.count(item) for item in cpus}
disk = {item:disk.count(item) for item in disk}
memory = {item:memory.count(item) for item in memory}


fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=False)
axs[0].bar(list(cpus.keys()), list(cpus.values()))
axs[0].set_title('CPU')
axs[1].bar(list(disk.keys()), list(disk.values()))
axs[1].set_title('DISK')
axs[2].bar(list(memory.keys()), list(memory.values()))
axs[2].set_title('MEMORY')
# fig.suptitle('Resources - Normal Distribution\n\n')
fig.savefig('ResourcesNormalDistribution.png')
# plt.savefig('test.png')
plt.show()