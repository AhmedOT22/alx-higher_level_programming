#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda x: x * x)), c) for c in matrix]
