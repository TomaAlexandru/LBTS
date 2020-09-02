import simpy

""" queue implements simpy.Store in order to simulate resource with *capacity* slots for storing arbitrary objects """
class Queue(simpy.Store):

    currentState = []

    def __init__(self, env):
        super().__init__(env)