import simpy

class Queue(simpy.Store):

    currentState = []

    def __init__(self, env):
        super().__init__(env)