#!/usr/bin/python3
"""

    this module divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: is the matrix to be divided
        div: is the divisor of the matrix
    Returns:
        New matrix with the elements of the matrix divided
    Raises:
        TypeError: If num or div arent integers
        ZeroDivisionError: Ifdiv is equal to zero
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    def check_operation(num):
        """ this function checks and operates the numbers of the matrix
        Args:
            num: is each element of the matrix
        Returns:
            The result of the operation
        Raises:
            TypeError: If num is not a number integer
        """
        if num == " ":
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if type(num) is not int and type(num) is not float:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        result = round(num/div, 2)
        return result

    new_matrix = matrix.copy()
    i = 0
    while i < len(new_matrix):
        if new_matrix[i] == [] or type(new_matrix[i]) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        new_matrix[i] = list(map(check_operation, new_matrix[i]))
        i += 1
    rows = len(matrix)-1
    while (rows != 0):
        if (len(matrix[rows]) != len(matrix[rows-1])):
            raise TypeError("Each row of the matrix must have the same size")
        rows -= 1
    return new_matrix
