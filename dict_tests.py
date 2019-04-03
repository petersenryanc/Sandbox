"""
CP1404 - Dictionary with csv imports
Testing dictionary functionality when reading/writing csv files
Prototyping for CP1404 Assignment 1
"""

input_file = open("places.csv", "r")
for line in input_file:
    print("* ", line, end="")
input_file.close()

input_file = open("places.csv", "r")
dictionary_file = {input_file}
for line in input_file:
    print("* ", line, end="")
input_file.close()

list_1 = (1, 2, 3, 4, 5)
list_2 = ["a", "b", "c", "d", "e"]
my_dict = {}
my_dict[list_1] = list_2
new_list = list(my_dict.items())
for line in new_list:
    print("* ", line, end="")

list_1 = (1, 2, 3, 4, 5)
list_2 = ["a", "b", "c", "d", "e"]
my_list = [list_1, list_2]
for line in new_list:
    print("* ", line, end="")
print(my_list[0])
