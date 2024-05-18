#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    pair_list = []
    for index, element in enumerate(my_list):
        if element % 2 == 0:
            pair_list.append(True)
        else:
            pair_list.append(False)
    return pair_list
