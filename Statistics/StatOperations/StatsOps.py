from Calculator.Operations.operations import Operations


class StatsOps:

    def __init__(self):
        pass

    @staticmethod
    def mean(data):
        data_len = len(data)
        total = sum(data)
        return Operations.division(data_len, total)

    @staticmethod
    def median(data):
        list_len = len(data)
        list_sort = sorted(data)
        index = (list_len - 1) // 2

        if list_len % 2 == 1:
            return list_sort[index]
        else:
            return (list_sort[index] + list_sort[index + 1]) / 2
