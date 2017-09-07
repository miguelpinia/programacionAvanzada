#!/usr/bin/python3

from pprint import pprint

num_cuadros = 0
posible = []

def constante_magica(n):
    return n * (n ** 2 + 1) / 2

def prueba_renglones(cuadro, constante):
    for renglon in cuadro:
        if not (0 in renglon) and sum(renglon) != constante:
            return False
    return True

def prueba_columnas(cuadro, constante):
    for i in range(len(cuadro)):
        columna = [renglon[i] for renglon in cuadro]
        if not (0 in columna) and sum(columna) != constante:
            return False
    return True

def prueba_diagonales(cuadro, constante):
    n = len(cuadro)
    diagonal_1 = [cuadro[i][i] for i in range(n)]
    diagonal_2 = [cuadro[i][(n - 1) - i] for i in range(n)]
    if not (0 in diagonal_1) and sum(diagonal_1) != constante:
        return False
    if not (0 in diagonal_2) and sum(diagonal_2) != constante:
        return False
    return True

def genera(cuadro, renglon, columna, constante):
    total_secuencias = len(cuadro) ** 2
    if not prueba_renglones(cuadro, constante) \
       or not prueba_columnas(cuadro, constante) \
       or not prueba_diagonales(cuadro, constante):
        return
    if renglon == len(cuadro):
        pprint(cuadro)
        global num_cuadros
        num_cuadros += 1
        return
    for i in range(total_secuencias):
        if posible[i]:
            cuadro[renglon][columna] = i + 1
            posible[i] = False
            nueva_columna = columna + 1
            nuevo_renglon = renglon
            if nueva_columna == len(cuadro):
                nuevo_renglon += 1
                nueva_columna = 0
            genera(cuadro, nuevo_renglon, nueva_columna, constante)
            cuadro[renglon][columna] = 0
            posible[i] = True

def main_2(n):
    global num_cuadros
    global posible
    num_cuadros = 0
    cuadro = [[0 for i in range(n)] for i in range(n)]
    constante = constante_magica(n)
    posible = [True for i in range(n**2)]
    genera(cuadro, 0, 0, constante)
    print("Hay {} soluciones.".format(num_cuadros))

main_2(3)
