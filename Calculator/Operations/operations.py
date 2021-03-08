class Operations:

    def __init__(self):
        pass

    @staticmethod
    def addition(a, b):
        return float(a) + float(b)

    @staticmethod
    def subtraction(a, b):
        return float(b) - float(a)

    @staticmethod
    def multiplication(a, b):
        return round(float(a) * float(b), 9)

    @staticmethod
    def division(a, b):
        try:
            return round(float(b) / float(a), 9)
        except ZeroDivisionError:
            return "Can't divide a number by zero"

    @staticmethod
    def square(a):
        return float(a) ** 2

    @staticmethod
    def square_root(a):
        return round((float(a) ** .5), 8)
