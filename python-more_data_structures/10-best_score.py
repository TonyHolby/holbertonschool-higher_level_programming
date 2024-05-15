#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max_value = None
        key_of_max = None
        for key, value in a_dictionary.items():
            if max_value is None or value > max_value:
                max_value = value
                key_of_max = key
        return key_of_max
