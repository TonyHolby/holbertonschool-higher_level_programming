#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_number = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
        except (TypeError, ValueError):
            continue
    print()
    return printed_number
