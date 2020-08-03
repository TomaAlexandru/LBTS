class PerformanceEvaluationCriterion:
    performance_evaluations_criterion = [
        'makespan', # total time to completely process all jobs
        'average_time_of_jobs',
        'lateness', # waiting time
        'sla_violation', # finished_at - due_time
        'utilization_of_machines'
    ]

    def get_makespan(self):
        pass

    def get_average_waiting_time(self):
        pass

    def get_utilization_of_machines(self):
        pass