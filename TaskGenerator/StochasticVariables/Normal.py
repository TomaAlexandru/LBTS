from .Distribution import Distribution
import numpy

class Normal(Distribution):
    max_val_to_generate = {}

    """ instance is made using distribution and max values to be generated """
    def __init__(self, max_vals):
        self.max_val_to_generate = max_vals

    """ get generated values for each type of resources """

    def get_generated_values(self):
        result = {}
        for k in self.max_val_to_generate:
            result[k] = self.get_normal_distribution_value(self.max_val_to_generate[k])
        return result

    """ normal distribution value """
    def get_normal_distribution_value(self, max_value):
        r = max_value + 1
        while r > max_value or r < 1:
            r = int(numpy.random.normal(max_value / 2, max_value / 4, 1)[0])
        return r