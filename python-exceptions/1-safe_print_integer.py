#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int) is True:
            print("{}".format(value))
            return True
        else:
            raise ValueError
    except ValueError:
        return False
