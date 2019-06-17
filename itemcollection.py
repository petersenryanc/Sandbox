"""
Item Collection class for storing items for inventory
"""

from item import Item


class ItemCollection:
    def __init__(self):
        self.items = {}

    def __str__(self):
        print_items = ""
        if len(self.items) > 0:
            for item in self.items:
                temp_item = "{} \n".format(item)
                print_items += temp_item
        else:
            print("No items in this location.")
        return "{}".format(print_items)

    def add_place(self, item, location):
        item_to_add = Item(item)
        location_to_add = Item(location)
        self.items.update({item_to_add: location_to_add})
