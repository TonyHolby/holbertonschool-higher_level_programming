#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int) is False:
            return False
        else:
            raise ValueError
    except ValueError:
            print("{}".format(value))
    return True
