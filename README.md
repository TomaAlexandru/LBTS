# Load Balancing and Task Scheduling

There is a lot of research in the field of task scheduling but there are not many cases in which they focus around simulations or concrete examples. Scheduling in the distributed environment remains an unresolved issue due to its extremely varied characteristics: the nature of the tasks, the system architecture, the requirements of the tasks in business terms, variation in defining a good scheduler. By definition task scheduling is a NP-complete problem.
  In this paper we will focus on  creating a simulation environment for the entry of certain sets of tasks in a system in which it is desired to execute them in the most efficient way, efficient way in the current case means that we want to find which is the best order for tasks to be executed in order to reduce makespan, average time of a job spent in system, lateness and sla_violation.
  Another aspects of these aplication among scheduling task environment are the other three modules used for generation of tasks, data visualization and performance evaluation.

## Objectives
The current application is writen in four open source modules that are easy to configurate, modify and extend.
This paper presents the application that simulates the execution environment of tasks. The focus is on the scheduler (or dispatcher) who sends tasks to be executed to the task processors. It presents the results obtained by the scheduler using several classic heuristic algorithms. Also we prezent some of the extension techniques.
Bellow, each module are taken one by one and presentend in terms of functionality.

## Modules
Modules that are executed individually from the command line:
  - TaskGenerator (This module is designed to generate tasks that will later enter the simulation system.)
  - DataVisualization (Visualize generated data)
  - TaskScheduler (This module is designed to simulate a distributed system in which the incoming tasks initially end up in a dispatcher, which has the role of sending, to be processed, the tasks to the task scheduler.)
  - PerformanceEvaluation (In this module the resulting data are taken in the resulting files inside the reports directory, ie the tasks processed together with the data used to evaluate the performances:  makespan, average time of job, lateness, sla_violation)

One of the main considerations for chosing such a modular structure is because once generated the task files, we need to be able to keep the same tasks (persist the state) for future analysis. The only reason these four modules are together is so that the whole system can be versioned more easily, thus, we can use any of the four modules independly.

## Instalation
In order to run the app, first, you need to clone or download the app from the current repository and install requirements

```bash
git clone https://github.com/TomaAlexandru/LBTS.git
cd LBTS
pip install -r requirements.txt
```

## Application operation

#### TaskGenerator
Generates task based on configuration file and defined distributions.
```bash
python GenerateTasks.py
```

It reads the file ‘setup_file.yaml’ from the root directory of the project and based on the parameters mentioned below it starts generating tasks in 'GeneratedTasks' directory

Maximum task resources are defined in ‘setup_file.yaml’ as follows.

```yaml
"generate":
  "number_of_tasks": 5000
  "max_values_for_task_parameters":
    "cpu": 20
    "memory": 1000
    "disk": 2000
    "time_arrival": 3
    "due_time": 5
    "time_processing": 4

"process":
  "number_of_task_processors": 4
  "max_values_for_task_processor_parameters":
    "cpu": 20
    "memory": 1000
    "disk": 2000
```
There are not any strict rules regarding names of task resources, but the names of "max_values_for_task_parameters" should be sale as "max_values_for_task_processor_parameters" from "process" section.

"max_values_for_task_parameters" are used by distributions classes from TaskGenerator/StochasticVariables directory. You can easily extend module with other distributions by just writing subclasses of Distribution in the folder just mentioned.

Generated tasks have the following structure:
```json
{
    "cpu": 8,
    "memory": 434,
    "disk": 1492,
    "time_arrival": 2,
    "due_time": 6,
    "time_processing": 2
}
```
Note that due_date parameter, which is used to complete service-level agreement is: random_generated_value + time_arrival + time_processing.

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
By runing the above command we have created an environment for each generated task file and algorithm defined in TaskScheduler/Algorithms. App can be extended by simply put subclasses og Algorithm in TaskScheduler/Algorithms

Creation of simulation environment

```python
 """ scheduler environment is created for every generated tasks file """
    for taskFile in taskFiles:
        task_resources_distributions = taskFile.split(".")[0]
        file = open("GeneratedTasks/%s.json" % task_resources_distributions, "r")
        tasks = json.loads(file.read())

        """ a file is created for each combination of distribution / algorithm """
        for algorithm in Algorithm.__subclasses__():
            """ create simulation environment """
            scheduler = SimulationEnvironment(
                tasks,
                number_of_task_processors,
                task_processor_resources,
                task_resources_distributions,
                algorithm)
                scheduler.run()
```

##### PerformanceEvaluation
```bash
python PerformanceEvaluation.py
```
In this module the resulting data are taken in the resulting files inside the reports directory, ie the tasks processed together with the data used to evaluate the performances:  makespan, average time of job, lateness, sla_violation.

Files are created in 'Reports/Evaluation' directory. The file contains result comparision for each algorithm.

<img src="https://raw.githubusercontent.com/TomaAlexandru/LBTS/master/Resources/performance_evaluation_result.jpg" />

##### DataVisualization
Module is used to visualize generated data, and is left behind because it also can visualize also data from performance evaluation model output

For example after generation we will have two type of distribution:

###### Normal Distribution

```bash
python VisualizeData.py distribution normal
```

<img src="https://raw.githubusercontent.com/TomaAlexandru/LBTS/master/Resources/normal_dist.jpg" />

###### Uniform Distribution

```bash
python VisualizeData.py distribution uniform
```

<img src="https://raw.githubusercontent.com/TomaAlexandru/LBTS/master/Resources/uniform_dist.jpg" />

###### Performance Evaluation

```bash
python VisualizeData.py evaluate normal 'SLA VIOLATION'
```
<img src="https://raw.githubusercontent.com/TomaAlexandru/LBTS/master/Resources/scheduler.png" />
