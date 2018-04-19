#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        new_matrix = []

        for row in matrix:
                new_matrix.append([elem**2 for elem in row])

        return new_matrix
