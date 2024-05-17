#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int) is True:
            print("{}".format(value))
            return True
        else:
            raise TypeError
    except TypeError:
        if isinstance(value, str) is True:
            for index in value:
                if index >= '0' and index <= '9':
                    print("{}".format(value))
                    return True
        return False
