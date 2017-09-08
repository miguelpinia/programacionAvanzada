#!/usr/bin/python3

from pprint import pprint
import sys

num_cuadros = 0
posible = []

def constante_magica(n):
    """Calcula la constante mágica para n. La formula para
    calcular la constante mágica es n * (n ** 2 + 1) / 2."""
    return n * (n ** 2 + 1) / 2

def prueba_renglones(cuadro, constante):
    """Verifica que para un cuadro mágica, para cada renglón, la suma
    de los elementos del cuadro sea igual al valor de la constante
    mágica para el cuadro. Este valor es pasado como parámetro.  Si
    alguno de los renglones tiene un cero, pero los anteriores si
    tienen la suma de sus valores igual a la constante mágica, se
    considera que el cuadro es una posible solución."""
    for renglon in cuadro:
        if not (0 in renglon) and sum(renglon) != constante:
            return False
    return True

def prueba_columnas(cuadro, constante):
    """Verifica que para un cuadro mágico, para cada columna, la suma
    de los elementos del cuadro sea igual al valor de la constante
    mágica para el cuadro. Si alguno de los renglones tiene un cero,
    pero los anteriores si tienen la suma de sus valores igual a la
    constante mágica, se considera que el cuadro es una posible
    solución."""
    for i in range(len(cuadro)):
        columna = [renglon[i] for renglon in cuadro]
        if not (0 in columna) and sum(columna) != constante:
            return False
    return True

def prueba_diagonales(cuadro, constante):
    """Verifica que para un cuadro mágica, para cada renglón, la suma
    de los elementos del cuadro sea igual al valor de la constante
    mágica para el cuadro. Este valor es pasado como parámetro. Si
    alguno de los renglones tiene un cero, pero los anteriores si
    tienen la suma de sus valores igual a la constante mágica, se
    considera que el cuadro es una posible solución."""
    n = len(cuadro)
    diagonal_1 = [cuadro[i][i] for i in range(n)]
    diagonal_2 = [cuadro[i][(n - 1) - i] for i in range(n)]
    if not (0 in diagonal_1) and sum(diagonal_1) != constante:
        return False
    if not (0 in diagonal_2) and sum(diagonal_2) != constante:
        return False
    return True

def genera(cuadro, renglon, columna, constante):
    """Solución recursiva. En caso de encontrar una solución, la
    imprime en la consola."""
    total_secuencias = len(cuadro) ** 2
    if not prueba_renglones(cuadro, constante) \
       or not prueba_columnas(cuadro, constante) \
       or not prueba_diagonales(cuadro, constante):
        return
    if renglon == len(cuadro):
        global num_cuadros
        print("\nSolución #{}".format(num_cuadros + 1))
        pprint(cuadro)
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

def main(n):
    """Función de inicialización para el algoritmo de búsqueda de
    soluciones para un cuadrado mágico. Recibe como parámetro el
    tamaño del cuadrado mágico."""
    global num_cuadros
    global posible
    num_cuadros = 0
    cuadro = [[0 for i in range(n)] for i in range(n)]
    constante = constante_magica(n)
    posible = [True for i in range(n**2)]
    genera(cuadro, 0, 0, constante)
    print("\n\nHay {} soluciones.".format(num_cuadros))

def menu():
    """Menú del usuario."""
    mensaje = ("Generación de soluciones para cuadrados mágicos.\n"
               "Inserte el tamaño del cuadrado mágico para el cuál se generarán todas las soluciones.\n")
    try:
        n = int(input(mensaje))
    except ValueError:
        print("¡Debes ingresar un caracter!\n\n")
        menu()
    main(n)
    continuar = input("¿Desea generar otra solución s/n? ")
    while continuar.lower().strip() != "s" and continuar.lower().strip() != "n":
        print("¡Entrada inválida!, vuelve a intentar.\n")
        continuar = input("¿Desea generar otra solución s/n? ")
    if continuar == "n":
        sys.exit(0)
    elif continuar == "s":
        menu()

if __name__ == "__main__":
    menu()
