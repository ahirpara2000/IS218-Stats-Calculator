from Calculator.Calculator import Calculator
from Statistics.StatOperations.StatsOps import StatsOps

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = StatsOps.mean(data)
        return self.result
