from .Random import Random
from .RoundRobin import RoundRobin
from .ShortestProcessingTime import ShortestProcessingTime

class Heuristics(dict):
    random = Random
    round_robin = RoundRobin
    shortest_processing_time = ShortestProcessingTime