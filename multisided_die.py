"""
Multi-sided Die Simulator
Create and roll n-sided dice
"""

from MSDie import MSDie


# def main():
#     die_1 = MSDie(12)
#     die_1.roll()
#     print(die_1.get_value())

def main():
    try:
        n_sides = int(input("Enter number of sides: "))
        while n_sides <= 0:
            print("Number of sides must be greater than zero.")
            n_sides = int(input("Enter number of sides: "))
        die = MSDie(n_sides)
        die.roll()
        print("Die roll results in {}".format(die.get_value()))
    except ValueError:
        print("Must be a number greater than zero")
        main()


main()
