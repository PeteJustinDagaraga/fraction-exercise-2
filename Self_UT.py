from Fraction import Fraction

def __main__():
    fr = Fraction(5,1)
    fr2 = Fraction(5)
    fr3 = Fraction('5/7')
    fr4 = Fraction('-5/7')
    fr5 = Fraction('5/-7')
    fr6 = Fraction('-5/-7')
    fr7 = Fraction('       -5/7        ')
    notfr = Fraction("lol")
    notfr2 = Fraction(1.123)
    # notfr3 = Fraction(5,0)

    print(fr.get_fraction())
    print(fr2.get_fraction())
    print(fr3.get_fraction())
    print(fr4.get_fraction())
    print(fr5.get_fraction())
    print(fr6.get_fraction())
    print(fr7.get_fraction())
    print(notfr.get_fraction())
    print(notfr2.get_fraction())
    # print(notfr3.get_fraction())

    # print(Fraction.gcd(0,0))
    # print(Fraction.gcd(1,0))
    # print(Fraction.gcd(2,1))
    # print(Fraction.gcd(5,7))
    # print(Fraction.gcd(7,5))
    # print(Fraction.gcd(4,10))
    # print(Fraction.gcd(10,4))
    # print(Fraction.gcd(-9,-3))

__main__()