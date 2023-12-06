#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for element in my_list:
        new_list.append(replace if element == search else element)
    return new_list
