#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in matrix:
        line = ""
        for element in index:
            line += "{:d} ".format(element)
        print(line)
