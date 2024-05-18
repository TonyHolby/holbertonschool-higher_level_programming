#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for index, element in enumerate(line):
            if index == len(line) - 1:
                print("{:d}".format(element), end='')
            else:
                print("{:d}".format(element), end=' ')
        print()
