"""EJERCICIO EXTRA"""

import asyncio

# Escribe el mayor número de mecanismos que posea tu lenguaje
# para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
from itertools import chain, count, islice

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Bucles Básicos
# 1
for element in valores:
    print(element)

# 2
i = 0
while i < 3:
    print(i)
    i += 1

# Funciones y métodos
# 3
for i in range(5):
    print(i)

# 4
# enumerate: proporciona un indice y el valor
for index, value in enumerate(valores):
    print(index, value)

# 5
for a, b in zip([1, 2, 3], ["x", "y", "z"]):
    print(a, b)

# 6
for value in map(str.upper, ["antes", "después"]):
    print(value)

# 7
for value in filter(lambda x: x % 2 == 0, valores):
    print(value)

# 8 Comprensiones
# List
squares = [x**2 for x in valores]
print(squares)
# Set
unique_squares = {x**2 for x in valores}
print(unique_squares)
# Dictionary
square_dict = {x: x**2 for x in valores}
print(square_dict)
# Generator
gen = (x**2 for x in valores)

# 9 Iteradores y Generadores
# Explícitos
my_iter = iter([1, 2, 3])
print(next(my_iter))
print(next(my_iter))


# Generadores
def generator():
    yield from range(5)


for value in generator():
    print(value)

# 10 Especificos
# Strings
for char in "Hola":
    print(char)

# Diccionarios
my_dict = {"a": 1, "b": 2}
for key, value in my_dict.items():
    print(key, value)

# 11 IterTools
# Count: cuenta infinitamente desde un valor inicial
for i in count(10):
    print(i)
    if i == 15:
        break

# Cycle: Itera infinitamente sobre un iterable
# for value in cycle([1, 2, 3]):
# print(value)

# Chain: Combina multiples iterables
for value in chain([1, 2, 3], ["a", "b", "c"]):
    print(value)

# islice
for value in islice(range(10), 3, 6):
    print(value)


# 12 Asincronía
async def async_def():
    for i in range(5):
        await asyncio.sleep(1)
        yield i


async def main():
    async for value in async_def():
        print(value)


asyncio.run(main())

# 13 Excepciones
for value in valores:
    try:
        print(1 / value)
    except ZeroDivisionError:
        print("No se puede dividir por cero!!")


# 14 Mecanismo personalizados
class MyIterable:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current

        raise StopIteration


for value in MyIterable(5):
    print(value)
