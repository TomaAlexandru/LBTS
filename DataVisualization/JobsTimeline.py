from datetime import datetime
import matplotlib.pyplot as plt

jobs = ['P1','P2','P3','P4','P5']




waittimes = [0,3,11,15,9]
runtimes = [3,6,4,5,2]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.barh(jobs, waittimes, align='center', height=.25, color='#FFFFFF',label='wait time')
ax.barh(jobs, runtimes, align='center', height=.25, left=waittimes, color='g',label='run time')
ax.set_yticks(jobs)
ax.set_xlabel('Time')
ax.set_title('Run Time by P')
ax.grid(True)
# ax.legend()
plt.tight_layout()
# plt.savefig('C:\\Data\\stackedbar.png')
plt.show()