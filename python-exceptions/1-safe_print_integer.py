#!/usr/bin/python3
def safe_print_integer(value):
    printed_value = False
    try:
        if isinstance(value, int):
            print("{}".format(value))
            printed_value = True
    except ValueError:
        print("{} is not an integer".format(value))
    finally:
        return printed_value
