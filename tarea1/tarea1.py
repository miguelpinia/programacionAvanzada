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
