"""
Class for representing items being collected and stored
"""


class Item:
    def __init__(self, item="", location=""):
        self.item = item
        self.location = location

    def __repr__(self):
        return "{} is located in {}".format(self.item, self.location)
