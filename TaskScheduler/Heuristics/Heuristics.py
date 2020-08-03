from .Random import Random
from .RoundRobin import RoundRobin
from .ShortestProcessingTime import ShortestProcessingTime

class Heuristics(dict):
    @staticmethod
    def get_list():
        return [
            Random,
            RoundRobin,
            ShortestProcessingTime
        ]