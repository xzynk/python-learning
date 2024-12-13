"""ITERACIONES SOLUCIÓN"""

# Utilizando tu lenguaje, emplea 3 mecanismos diferentes para
# imprimir números del 1 al 10 mediante iteración.

# Usando FOR y un iterable
print("Usando FOR y un Iterable")
iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for element in iterable:
    print(element)

# Usando FOR y RANGE
print("Contando del 1 al 10 con FOR con RANGE")
for number in range(1, 11):
    print(number)

# Usando WHILE
print("Contando del 1 al 10 usando WHILE")
COUNTER = 1
while COUNTER <= 10:
    print(COUNTER)
    COUNTER += 1
