#!/usr/bin/python3
def delete_at(my_list=[], idx=3):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for index, element in enumerate(my_list):
            if index != idx:
                new_list.append(element)
        return new_list
