import random
import numpy

""" class is used as a generator for task values """
class Distribution:
    distribution    = None
    max_val_to_generate = {}

    """ instance is made using distribution and max values to be generated """
    def __init__(self, distribution, max_vals = {}):
        self.distribution    = distribution
        self.max_val_to_generate = max_vals

    """ get generated values for each type of resources """
    def get_generated_values(self):
        result = {}
        for k in self.max_val_to_generate:
            result[k] = self.get_stochastic_value(self.max_val_to_generate[k])
        return result

    """ get value for each resource """
    def get_stochastic_value(self, max_value):
        if self.distribution == "uniform":
            return self.get_uniform_distribution_value(max_value)
        if self.distribution == "normal":
            return self.get_normal_distribution_value(max_value)

    """ uniform distribution value """
    def get_uniform_distribution_value(self, max_value):
        return random.randrange(1, max_value+1)

    """ normal distribution value """
    def get_normal_distribution_value(self, max_value):
        r = max_value + 1
        while r > max_value or r < 1:
            r = int(numpy.random.normal(max_value/2, max_value/4, 1)[0])
        return r
