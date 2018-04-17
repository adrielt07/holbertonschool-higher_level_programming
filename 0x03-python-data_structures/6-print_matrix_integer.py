#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for i in range(3):
                print(" ".join("{}".format(j) for j in matrix[i]))
#                for i in matrix[i]:
#                        print(i)

#        for i in matrix:
#                print(" ".join("{}".format(j) for j in i:))
#                print("\n".join("{}".format(j) for j in i))
