"""
Inventory Manager
A simple program for tracking where items are within a household.
"""

from itemcollection import ItemCollection
from item import Item


def main():
    list_of_items = ItemCollection()
    menu = """
    [A]dd an item
    [M]ove an item
    [D]elete an item
    [L]ookup item location
    [Q]uit
    """
    print(menu)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "A":
            add_item(list_of_items)
        elif menu_choice == "M":
            move_item()
        elif menu_choice == "D":
            delete_item()
        elif menu_choice == "L":
            lookup_item()
        else:
            print("Invalid input; enter bracketed letter only.")
        print(menu)
        menu_choice = input(">>> ").upper()


def list_items(list_of_items):
    for key, value in list_of_items.items():
        print("Item: {}, Location: {}".format(key, value))


def add_item(list_of_items):
    item = input("""
    Enter the item:
    >>> """)
    while not item:
        print("Input cannot be blank")
        item = input("""
            Enter the item:
            >>> """)
    location = input("""
    Enter the item's location:
    >>> """)
    while not location:
        print("Input cannot be blank")
        location = input("""
            Enter the item's location:
            >>> """)
    item_to_add = Item(item, location)


def move_item():
    pass


def delete_item():
    pass


def lookup_item():
    pass


if __name__ == '__main__':
    main()
