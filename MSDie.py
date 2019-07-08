"""
Multi-sided Die Class
Sets n-sided dice and returns roll values within n sides
"""

from random import randrange


class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
