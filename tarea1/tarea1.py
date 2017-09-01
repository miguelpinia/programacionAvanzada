#!/usr/bin/python3

def constante_magica(n):
    """Calcula la constante mágica para un número n. La formula para
    calcular la constante mágica es n * (n ** 2 + 1) / 2."""
    return n * (n ** 2 + 1) / 2

def verticales(cuadro, constante):
    """
    Verifica que para un cuadro mágico, para cada columna, la suma
    de los elementos del cuadro sea igual al valor de la constante
    mágica para el cuadro.
    """
    for column in range(len(cuadro)):
        suma_parcial = sum(renglon[column] for renglon in cuadro)
        if suma_parcial != constante:
            return False
    return True

def horizontales(cuadro, constante):
    """
    Verifica que para un cuadro mágica, para cada renglón, la suma
    de los elementos del cuadro sea igual al valor de la constante
    mágica para el cuadro. Este valor es pasado como parámetro.
    """
    for renglon in cuadro:
        suma_parcial = sum(val for val in renglon)
        if suma_parcial != constante:
            return False
    return True

def diagonales(cuadro, constante):
    """
    Verifica que para un cuadro mágico, para cada diagonal, la suma
    de los elementos del cuadro sea igual al valor de la constante
    mágica para el cuadro. Este valor es pasado como parámetro.
    """
    n = len(cuadro)
    sum_1 = sum(cuadro[i][i] for i in range(n))
    sum_2 = sum(cuadro[i][(n - 1) - i] for i in range(n))
    return sum_1 == constante == sum_2
