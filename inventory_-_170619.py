"""
Inventory Manager
A simple program for tracking where items are within a household.
"""

from itemcollection import ItemCollection


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
    menu_choice = ">>> ".upper()
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
        menu_choice = ">>> ".upper()


def add_item():
    pass


def move_item():
    pass


def delete_item():
    pass


def lookup_item():
    pass


if __name__ == '__main__':
    main()
