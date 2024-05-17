#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_number = 0
    for index in range(x):
        try:
            if isinstance(my_list[index], int):
                print("{}".format(my_list[index]), end="")
                printed_number += 1
            else:
                raise ValueError
        except ValueError:
            continue
    print()
    return printed_number
