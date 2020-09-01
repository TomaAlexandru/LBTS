# Load Balancing and Task Scheduling

There is a lot of research in the field of task scheduling but there are not many cases in which they focus around simulations or concrete examples. Scheduling in the distributed environment remains an unresolved issue due to its extremely varied characteristics: the nature of the tasks, the system architecture, the requirements of the tasks in business terms, what defines a good scheduler.
In this paper we will focus exclusively on creating a simulation environment for the entry of certain sets of tasks in a system in which it is desired to execute them in the most efficient way, efficient way in the current case means that we want to find which is the best order for tasks to be executed in order to reduce makespan, average time of a job spent in system, lateness and sla_violation.

## Objectives
This paper presents the application that simulates the execution environment of tasks. The focus is on the scheduler (or dispatcher) who sends tasks to be executed to the task processors. It presents the results obtained by the scheduler using several classic heuristic algorithms and try tries to crowdsource new ideas for algorithmis in order to improve the current result.

## Aplication
The application is structured in four modules that are executed individually from the command line:
  - TaskGenerator (This module is designed to generate tasks that will later enter the simulation system.)
  - DataVisualization (Visualize generated data)
  - TaskScheduler (This module is designed to simulate a distributed system in which the incoming tasks initially end up in a dispatcher, which has the role of sending, to be processed, the tasks to the task scheduler.)
  - PerformanceEvaluation (In this module the resulting data are taken in the resulting files inside the reports directory, ie the tasks processed together with the data used to evaluate the performances:  makespan, average time of job, lateness, sla_violation)

One of the main considerations for chosing such a modular structure is because once generated the task files, we need to be able to keep the same tasks (persist the state) for future analysis. The only reason these four modules are together is so that the whole system can be versioned more easily, thus, we can use any of the four modules independly.

In order to run the app, first, you need to install requirements (we have some dependencies such as matplotlib, simpy ... etc):

```bash
pip install -r requirements.txt
```

### Application operation

##### TaskGenerator
```bash
python GenerateTasks.py
```
It reads the file ‘setup_file.yaml’ from the root directory of the project and based on the parameters mentioned below it starts generating tasks in 'GeneratedTasks' directory
##### DataVisualization
Module is used to visualize generated data.

For example after generation we will have two type of distribution:

###### Normal Distribution

<img src="https://raw.githubusercontent.com/TomaAlexandru/LBTS/master/Resources/normal_dist.jpg" />

###### Uniform Distribution

<img src="https://raw.githubusercontent.com/TomaAlexandru/LBTS/master/Resources/uniform_dist.jpg" />

##### TaskScheduler
```bash
python ScheduleTasks.py
```
Files with resulted tasks are generated in 'Reports' directory.
This module is designed to simulate a distributed system in which the incoming tasks initially end up in a scheduler, which has the role of sending, to be processed, the tasks to the task processors.

Reports file are named: <resourceDistribution>_<algorithm>.json
  
Each file contains tasks and data regarding service level agreement, waiting time, finished time.

```json
{
    "current_resources_after_finished": {
        "cpu": 20,
        "disk": 2000,
        "memory": 1000
    },
    "processor_index": 13,
    "task": {
        "cpu": 11,
        "current_resources_after_reserve": {
            "cpu": 9,
            "disk": 771,
            "memory": 787
        },
        "disk": 1229,
        "due_time": 11,
        "finished_at": 848,
        "memory": 213,
        "sla_violation": 837,
        "time_arrival": 8,
        "time_processing": 1,
        "waiting_time": 839
    }
}
```

##### PerformanceEvaluation
```bash
python PerformanceEvaluation.py
```
In this module the resulting data are taken in the resulting files inside the reports directory, ie the tasks processed together with the data used to evaluate the performances:  makespan, average time of job, lateness, sla_violation.

An overview.csv file is created in 'Reports' directory. The file contains result comparision for each algorithm.

<img src="https://raw.githubusercontent.com/TomaAlexandru/LBTS/master/Resources/performance_evaluation_result.jpg" />
