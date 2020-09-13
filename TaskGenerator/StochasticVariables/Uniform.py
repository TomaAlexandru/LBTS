from .Distribution import Distribution
import random

class Uniform(Distribution):
    max_val_to_generate = {}

    """ instance is made using distribution and max values to be generated """
    def __init__(self,  max_vals):
        self.max_val_to_generate = max_vals

    """ get generated values for each type of resources """
    def get_generated_values(self):
        result = {}
        for k in self.max_val_to_generate:
            result[k] = random.randrange(1, self.max_val_to_generate[k] + 1)
        return result
