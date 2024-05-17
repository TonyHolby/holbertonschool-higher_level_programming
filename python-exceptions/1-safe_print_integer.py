#!/usr/bin/python3
def safe_print_integer(value):
    if value == "" or value is None:
        print()
        return True
    try:
        if isinstance(value, int):
            print("{}".format(value))
            return True
        elif isinstance(value, str):
            for character in value:
                if character.isdigit() is True:
                    continue
                else:
                    return False
            print("{}".format(value))
            return True
        else:
            raise TypeError
    except TypeError:
        return False
