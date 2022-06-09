#!/usr/bin/python3
"""Function that returns the Pascal's triangle"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascals triangle of n"""

    lista = []

    if n <= 0:
        return lista

    if n == 1:
        lista1 = [[1]]
        return lista1

    lista = [[1], [1, 1]]

    # bucle que se generara tantas veces como lineas vayamos a tener
    for i in range(1, n - 1):

        # inicializamos la linea
        linea = [1]

        # bucle por cada uno de los valores de la anterior linea
        for j in range(0, len(lista[i]) - 1):

            # añadimos a la lista los nuevos valores
            # sumamos el valor de la lista anterior con el siguinte
            linea.extend([lista[i][j] + lista[i][j+1]])

        # añadimos el ultimo valor a la nueva linea
        # siempre es un 1 igual que el primero
        linea += [1]

        # añadimos la linea a la lista
        lista.append(linea)

    # devolvemos la lista ya creada
    return lista
