from Fraction import Fraction

def __main__():
    fr = Fraction(1, 2)
    fr2 = Fraction("123")
    fr3 = Fraction("-32")
    fr4 = Fraction("     2/5     ")
    fr5 = Fraction("         -2/5")
    fr6 = Fraction("2/-5         ")
    notfr = Fraction("lol")

    print(fr.get_fraction())
    print(fr2.get_fraction())
    print(fr3.get_fraction())
    print(fr4.get_fraction())
    print(fr5.get_fraction())
    print(fr6.get_fraction())
    print(notfr.get_fraction())

__main__()
