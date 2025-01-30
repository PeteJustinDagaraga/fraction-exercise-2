class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        try:
            self.numerator = numerator
            self.denominator = denominator
        except:
            print("Input not integer")

    def __init__(self, fraction_string: str):
        #TODO
        actual_fraction = fraction_string.strip()
        values = actual_fraction.split(/)
        self.numerator=int(values[0])
        self.denominator=int(values[1])

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
