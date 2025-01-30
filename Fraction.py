class Fraction(object):

    def __init__(self, *args):
        numerator = 0
        denominator = 0
        try:
            if len(args) == 2:
                numerator = args[0]
                denominator = args[1]
            
            if len(args) == 1:
                str_fraction = args[0]
                str_fraction = str_fraction.strip()

                str_fraction_values = str_fraction.split('/')

                if len(str_fraction_values) == 2:
                    numerator = int(str_fraction_values[0])
                    denominator = int(str_fraction_values[1])
                else:
                    numerator = int(str_fraction_values[0])
                    denominator = 1

            self.numerator = numerator
            self.denominator = denominator

            if not isinstance(numerator, int):
                raise ValueError
            if not isinstance(denominator, int):
                raise ValueError
            if denominator == 0:
                raise ZeroDivisionError
        except ValueError:
            print("Input not integer")
            self.numerator = None
            self.denominator = None
            
    def gcd(a, b, level = 0):
        if level == 0 and (a == 0 or b == 0):
            return 0
        if b == 0:
            return a
        return Fraction.gcd(b,a%b, level + 1)

    def get_numerator(self) -> int:
        return self.numerator

    def get_denominator(self) -> int:
        return self.denominator

    def get_fraction(self):
        if self.denominator is None or self.denominator == 0:
            return str(0)
        if self.denominator == 1:
            return f'{self.numerator}'
        
        remainder = self.numerator % self.denominator

        if remainder == 0:
            quotient = self.numerator // self.denominator
            return f'{quotient}'        

        return f'{self.numerator}/{self.denominator}'
