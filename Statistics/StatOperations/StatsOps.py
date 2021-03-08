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

    @staticmethod
    def mode(data):
        counter = 0
        num = data[0]

        for i in data:
            curr_frequency = data.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                num = i

        return num

    @staticmethod
    def variance(data):
        data_mean = StatsOps.mean(data)
        x = 0

        for num in data:
            x = x + Operations.square(num - data_mean)

        return Operations.division(len(data), x)

    @staticmethod
    def std_deviation(data):
        data_variance = StatsOps.variance(data)
        return Operations.square_root(data_variance)

    @staticmethod
    def z_score(data):
        data_mean = StatsOps.mean(data)
        data_sd = StatsOps.std_deviation(data)
        z_score_list = []
        for num in data:
            z_score = (num - data_mean) / data_sd
            z_score_list.append(z_score)
        return z_score_list
