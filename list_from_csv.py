"""
CP1404 - Testing method of pulling csv data into list
"""

input_file = open("places.csv", "r")
list_of_places = []
# list_of_places = [input_file.rstrip() for line in input_file]
# print(list_of_places)
for line in input_file:
    list_of_places.append(line)
print(list_of_places)