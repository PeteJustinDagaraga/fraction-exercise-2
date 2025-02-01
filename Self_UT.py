from Fraction import Fraction

def __main__():
    fr = Fraction(2,1)
    fr2 = Fraction(3)
    fr3 = Fraction('4')
    fr4 = Fraction('5/1')
    print(fr.get_fraction())
    print(fr2.get_fraction())
    print(fr3.get_fraction())
    print(fr4.get_fraction())

__main__()