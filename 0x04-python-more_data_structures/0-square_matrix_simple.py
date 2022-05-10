#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    i = 0
    while i < len(new_matrix):
        new_matrix[i] = list(map(lambda x: x * x, new_matrix[i]))
        i += 1
    return new_matrix
