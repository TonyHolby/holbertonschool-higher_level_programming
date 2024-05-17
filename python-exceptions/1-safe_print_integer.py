#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{}".format(value))
            return True
        elif isinstance(value, str):
            for character in value:
                if character.isdigit() is False:
                    return False
                else:
                    print("{}".format(value))
                    return True
        else:
            raise TypeError
    except TypeError:
        return False
