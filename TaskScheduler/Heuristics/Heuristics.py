from .Random import Random
from .RoundRobin import RoundRobin
from .ShortestProcessingTime import ShortestProcessingTime
from .CriticalRatio import CriticalRatio
from .EarliestDueDate import EarliestDueDate

class Heuristics(dict):
    @staticmethod
    def get_list():
        return [
            # Random,
            RoundRobin,
            # ShortestProcessingTime
        ]