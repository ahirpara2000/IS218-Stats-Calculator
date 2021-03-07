class Operations:

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
        return round(float(b) / float(a), 9)