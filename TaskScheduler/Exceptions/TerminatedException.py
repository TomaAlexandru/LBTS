class TerminatedException(Exception):
    def __init__(self, distribution, algorithm):
        self.distribution = distribution
        self.algorithm = algorithm

    def get_message(self):
        return "Tasks with %s data has been scheduled using %s algorithm" % (self.distribution, self.algorithm)