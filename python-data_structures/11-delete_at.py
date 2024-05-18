#!/usr/bin/python3
def delete_at(my_list=[], idx=3):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for position, element in enumerate(my_list):
            if position != idx:
                new_list.append(element)
        for position, element in enumerate(my_list):
            if position == idx:
                my_list.remove(element)
        return new_list
