from Calculator.Operations.operations import Operations


class StatsOps:

    def __init__(self):
        pass

    @staticmethod
    def mean(data):
        data_len = len(data)
        total = sum(data)
        return Operations.division(total, data_len)
