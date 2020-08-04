import json

class Heuristics(dict):
    def task_reception(self, number_of_tasks, task_resources_distributions, in_pipes):
        """ TASK RECEPTION """
        for in_pipe in in_pipes:
            self.finished_tasks = self.finished_tasks + in_pipe.items
            in_pipe.items = []
            """ OPERATION FINISHED """
            if number_of_tasks == len(self.finished_tasks):
                with open("Reports/%s_%s.json" % (task_resources_distributions, self.__str__()),
                          "w") as twitter_data_file:
                    json.dump(self.finished_tasks, twitter_data_file, indent=4, sort_keys=True)
                raise Exception(task_resources_distributions, self.__str__())



