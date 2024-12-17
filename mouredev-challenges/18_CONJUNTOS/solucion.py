"""SOLUCIÓN EJERCICIO"""

# Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes operaciones (debes utilizar una estructura que
# las soporte):
#
# - Añade un elemento al final.
# - Añade un elemento al principio.
# - Añade varios elementos en bloque al final.
# - Añade varios elementos en bloque en una posición concreta.
# - Elimina un elemento en una posición concreta.
# - Actualiza el valor de un elemento en una posición concreta.
# - Comprueba si un elemento está en un conjunto.
# - Elimina el contenido del conjunto.


# Para solucionar este ejercicio crearé una clase con métodos que cumplan las funciones
# No es necesario y tranquilamente se podría hacer sin el uso de una clase.


class ConjuntoDatos:
    def __init__(self, lista=None):
        if lista is None:
            lista = []
        self.lista = lista

    def append(self, valor):
        self.lista.append(valor)

    def prepend(self, valor):
        self.lista.insert(0, valor)

    def extend(self, iterable, position=None):
        if position is None:
            self.lista.extend(iterable)
            return

        if position < 0 or position > len(self.lista):
            raise IndexError("position out of range")

        self.lista[position + 1 : position + 1] = iterable

    def pop_at(self, index):
        return self.lista.pop(index)

    def update_at(self, index, valor):
        self.lista[index] = valor

    def exist(self, value):
        return value in self.lista

    def remove(self):
        self.lista.clear()


# No hace falta asignar ningún parametro, creará una lista vacía
conjunto = ConjuntoDatos([1, 2, 3, 4])

# - Añade un elemento al final.
conjunto.append(5)
# - Añade un elemento al principio.
conjunto.prepend(0)
# - Añade varios elementos en bloque al final.
conjunto.extend([6, 7, 8, 9])
# - Añade varios elementos en bloque en una posición concreta.
conjunto.extend(["a", "b", "c"], 3)
# - Elimina un elemento en una posición concreta.
conjunto.pop_at(4)
# - Actualiza el valor de un elemento en una posición concreta.
conjunto.update_at(4, 5)
# - Comprueba si un elemento está en un conjunto.
print(conjunto.exist(6))  # Existe
print(conjunto.exist(10))  # No existe
# - Elimina el contenido del conjunto.
conjunto.remove()
print(conjunto.lista)

# Ejercicio extra
# Muestra ejemplos de las siguientes operaciones con conjuntos:
# - Unión.
# - Intersección.
# - Diferencia.
# - Diferencia simétrica.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)
print(union_set)
# Intersección
intersection_set = set1.intersection(set2)
print(intersection_set)
# Diferencia
difference_set = set1.difference(set2)
print(difference_set)
# Diferencia Simétrica
difference_symmetric = set1.symmetric_difference(set2)
print(difference_symmetric)
