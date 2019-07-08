"""
Multi-sided Die Simulator
Create and roll n-sided dice
"""

from MSDie import MSDie


def main():
    die_1 = MSDie(12)
    die_1.roll()
    print(die_1.get_value())


main()
