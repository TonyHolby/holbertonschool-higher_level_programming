#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            elements_printed += 1
        except IndexError:
            break
    print()
    return elements_printed
