from Fraction import Fraction

def __main__():
    fr = Fraction(1, 2)
    fr2 = Fraction("123")
    fr3 = Fraction("-32")
    fr4 = Fraction("     2/5     ")
    fr5 = Fraction("         -2/5")
    fr6 = Fraction("2/-5         ")
    notfr = Fraction("lol")

    print(Fraction.gcd(0,1))
    print(Fraction.gcd(0,0))
    print(Fraction.gcd(1,0))
    print(Fraction.gcd(2,1))
    print(Fraction.gcd(5,7))
    print(Fraction.gcd(7,5))
    print(Fraction.gcd(4,10))
    print(Fraction.gcd(10,4))

__main__()


a = 0
b = 1
print(a or b == 0)
