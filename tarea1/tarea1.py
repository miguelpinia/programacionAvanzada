#!/usr/bin/python3

from collections import deque

class Stack(list):
    """Clase que representa una pila. Dado que hereda a partir de una
    lista, sólo se implementan los métodos push para agregar al
    principio de la pila y peek para ver el tope de la misma.

    Ejemplo de uso:

    pila = Stack()
    pila.push(1)
    pila.push(2)
    pila.push(3)
    print(pila) # [1, 2, 3]
    pila.pop()
    print(pila) # [1, 2]"""

    def __init__(self):
        """Constructor. Inicializa el constructor de la clase padre."""
        super(Stack, self).__init__()

    def push(self, val):
        """Inserta un elemento en el tope de la pila."""
        self.append(val)

    def peek(self):
        """Devuelve el valor del elemento en el tope de la pila sin
        eliminarlo de la pila."""
        return self[-1]

class Queue(deque):
    """Clase que representa una cola. Dado que hereda a partir de
    collections.deque, sólo se implementan los métodos enqueue y
    dequeue para facilitar su operación al insertar y eliminar
    elementos.

    Ejemplo de uso:

    cola = Queue()
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(4)
    print(cola) # deque([1, 2, 4])
    cola.dequeue()
    print(cola) # deque([2, 4])"""

    def __init__(self):
        """Constructor, inicializa el constructor de la clase padre."""
        super(Queue, self).__init__()

    def enqueue(self, value):
        """Inserta un elemento al final de la cola."""
        self.append(value)

    def dequeue(self):
        """Saca un elemento al principio de la cola."""
        self.popleft()

cuadro = [[4, 5, 16, 9], [14, 11, 2, 7], [1, 8, 13, 12], [15, 10, 3, 6]]

def valida_renglon(cuadro, renglon, constante):
    """
    Dados el cuadrado mágico, el índice del renglón a validar y el
    valor de la constante mágica, se realiza la suma de los elementos
    y se verifica si dicha suma es igual a la de la constante dada."""
    suma_parcial = sum(valor for valor in cuadro[renglon])
    return suma_parcial == constante

def valida_columna(cuadro, columna, constante):
    """
    Dados el cuadrado mágico, el índice de la columna a validar y
    el valor de constante mágica, se realiza la suma de los elementos
    para dicha columan y se verifica si dicha suma es igual a la de la
    constante dada."""
    suma_parcial = sum(renglon[columna] for renglon in cuadro)
    return suma_parcial == constante

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
    for columna in range(len(cuadro)):
        if not valida_columna(cuadro, columna, constante):
            return False
    return True

def horizontales(cuadro, constante):
    """
    Verifica que para un cuadro mágica, para cada renglón, la suma
    de los elementos del cuadro sea igual al valor de la constante
    mágica para el cuadro. Este valor es pasado como parámetro.
    """
    for renglon in range(len(cuadro)):
        if not valida_renglon(cuadro, renglon, constante):
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

def valida_cuadro(cuadro, constante):
    """
    Valida que un cuadro mágico sea valido para la constante
    dada. Para esto, valida que la suma de todas sus columnas,
    renglones y diagonales sea igual al valor de la constante mágica
    dada como parámetro.
    """
    return constante_magica(len(cuadro)) == constante \
        and diagonales(cuadro, constante) \
        and horizontales(cuadro, constante) \
        and verticales(cuadro, constante)

###################################################
# Vamos a escribir código hasta que algo funcione #
###################################################

cuadro = [[0 for i in range(3)] for i in range(3)]
totalSqs = 3*3
posible = [True for i in range(totalSqs)]
constante = constante_magica(3)
numSquares = 0

def testRenglon(c, const):
    for i in range(len(c)):
        test = 0
        unfilled = False
        for j in range(len(c[i])):
            test += c[i][j]
            if c[i][j] == 0:
                unfilled = True
        if not unfilled and test != const:
            return False
    return True

def testCols(c, const):
    for j in range(len(c[0])):
        test = 0
        unfilled = False
        for i in range(len(c)):
            test += c[i][j]
            if c[i][j] == 0:
                unfilled = True
        if not unfilled and test != const:
            return False
    return True

def testDiagonales(c, const):
    test = 0
    unfilled = False
    for i in range(len(c)):
        test += c[i][i]
        if c[i][i] == 0:
            unfilled = True
    if not unfilled and test != const:
        return False

    test = 0
    unfilled = False
    for i in range(len(c)):
        test += c[i][len(c) - 1  - i]
        if (c[i][len(c) - 1- i]) == 0:
            unfilled = True
    if not unfilled and test != const:
        return False
    return True

def pretty_print(c):
    for row in c:
        print('\t'.join(str(e) for e in row))

def llena(c, row, col, const):
    if not testRenglon(c, const) or not testCols(c, const) or not testDiagonales(c, const):
        return
    if row == len(c):
        print("\n\n")
        pretty_print(c)
        print("\n\n")
        global numSquares
        numSquares += 1
        return
    for i in range(totalSqs):
        if posible[i]:
            c[row][col] = i + 1
            posible[i] = False
            newCol = col + 1
            newRow = row
            if newCol == len(c):
                newRow += 1
                newCol = 0
            llena(c, newRow, newCol, const)
            c[row][col] = 0
            posible[i] = True

def main(n):
    cuadro = [[0 for i in range(n)] for i in range(n)]
    constante = constante_magica(n)
    llena(cuadro, 0, 0, constante)
    print("Hay {} soluciones".format(numSquares))

main(3)

########################################################################
# Probamos la salida, como por el momento sólo las imprimo en lugar de #
# meterlas en alguna lista, tengo que probar a mano que todas las      #
# soluciones son correctas :c                                          #
########################################################################


l = [[[2, 7, 6], [9, 5, 1], [4, 3, 8]], [[2, 9, 4], [7, 5, 3], [6, 1, 8]], [[4, 3, 8], [9, 5, 1], [2, 7, 6]], [[4, 9, 2], [3, 5, 7], [8, 1, 6]], [[6, 1, 8], [7, 5, 3], [2, 9, 4]], [[6, 7, 2], [1, 5, 9], [8, 3, 4]], [[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[8, 3, 4], [1, 5, 9], [6, 7, 2]]]

for x in l:
    print("Funcionó: {}".format(valida_cuadro(x, 15)))
