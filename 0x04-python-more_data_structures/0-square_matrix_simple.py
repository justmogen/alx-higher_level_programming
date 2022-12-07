#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda v: v ** 2, row_values)) for row_values in matrix]
