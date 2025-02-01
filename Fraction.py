class Fraction():
    '''
    @author: Lorenzo Duenas, Alinus Abuke, Pete Justin Dagaraga

    "
    We have not discussed the Python language code in our program with
    anyone other than our instructor or the teaching assistants assigned
    to this course.

    We have not used Python language code obtained from another student, or
    any other unauthorized source, either modified or unmodified.

    If any Python language code or documentation used in our program
    was obtained from another source, such as a textbook or course notes,
    that has been clearly noted with a proper citation in the comments
    of our program.
    "

    '''
    def __init__(self, *args):
        '''
        @brief generates a fraction based on input values
        '''

        numerator = 0
        denominator = 1

        try:
            if len(args) == 2:
                numerator = args[0]
                denominator = args[1]

            if len(args) == 1:
                if isinstance(args[0],str):
                    numerator, denominator = self.__parse_string__(args[0])

                else:
                    if not isinstance(args[0],int):
                        raise ValueError
                    numerator = args[0]

            self.numerator = numerator
            self.denominator = denominator

            if self.__are_integers__(self.numerator,self.denominator):
                raise ValueError

            if denominator == 0:
                raise ZeroDivisionError

        except ValueError:
            print("Input not integer")
            self.numerator = None
            self.denominator = None

        else:
            self.__simplify__()

    def __are_integers__(self, value1, value2):
        '''
        @brief returns True if either value is not an Integer
        '''

        return not isinstance(value1, int) or not isinstance(value2, int)


    def __parse_string__(self, str_fraction):
        '''
        @brief returns numerator and denominator from input string
        '''

        str_fraction = str_fraction.strip()
        str_fraction_values = str_fraction.split('/')
        numerator = 0
        denominator = 0

        if len(str_fraction_values) == 2:
            numerator = int(str_fraction_values[0])
            denominator = int(str_fraction_values[1])

        elif len(str_fraction_values) == 1:
            numerator = int(str_fraction_values[0])
            denominator = 1

        else:
            raise ValueError

        return numerator, denominator


    def gcd(a, b, level = 0):
        '''
        @brief returns the greatest common denominator of 2 values
        '''

        if level == 0 and (a == 0 or b == 0):
            return 0

        if b == 0:
            return a

        return Fraction.gcd(b,a%b, level + 1)


    def get_numerator(self) -> int:
        '''
        @brief returns the numerator of the fraction
        '''
        return self.numerator


    def get_denominator(self) -> int:
        '''
        @brief returns the denominator of the fraction
        '''
        return self.denominator


    def get_fraction(self):
        '''
        @brief returns the fraction as a string and in lowest form
        '''
        if self.__no_denominator__(self.denominator):
            return str(0)

        if self.denominator == 1:
            return f'{self.numerator}'

        remainder = self.numerator % self.denominator

        if remainder == 0:
            quotient = self.numerator // self.denominator
            return f'{quotient}'

        return f'{self.numerator}/{self.denominator}'


    def __simplify__(self):
        '''
        @brief simplifies the fraction
        '''
        fraction_gcd = Fraction.gcd(self.numerator, self.denominator)
        if fraction_gcd != 0:
            self.numerator = (int) (self.numerator // fraction_gcd)
            self.denominator = (int) (self.denominator // fraction_gcd)


    def __no_denominator__(self, denominator_value):
        '''
        @brief returns true if the fraction is invalid or the
        denominator is zero
        '''
        return denominator_value is None or denominator_value == 0
