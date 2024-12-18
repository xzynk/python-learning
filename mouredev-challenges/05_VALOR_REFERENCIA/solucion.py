"""VALOR Y REFERENCIA"""


# POR VALOR
# LOS TIPOS INMUTABLES (COMO ENTEROS, FLOTANTES, CADENAS Y TUPLAS)
# SE COMPORTAN COMO SI SE PASARAN POR VALOR


def modificar_valor(x):
    print(f"Valor dentro de la función antes de modificar: {x}")
    x += 10
    print(f"Valor de la función después de modificar: {x}")


MY_INT = 5
modificar_valor(MY_INT)
print(f"Valor fuera de la función: {MY_INT}")


def modificar_cadena(s):
    print(f"Cadena dentro de la función antes de modificar: {s}")
    s = "Modificado"
    print(f"Cadena dentro de la funciona despues de moficiar: {s}")


MY_CADENA = "Original"
modificar_cadena(MY_CADENA)
print(f"Cadena fuera de la función: {MY_CADENA}")


# POR REFERENCIA
# LOS TIPOS MUTABLES PUEDE SER MODIFICADOS DESPUÉS DE SER CREADOS


def modificar_lista(lst):
    print(f"Lista dentro de la funciona antes de modificar: {lst}")
    lst.append(100)  # Modificamos la lista existente
    print(f"Lista dentro de la función después de modificar: {lst}")


lista = [1, 2, 3, 4, 5]
modificar_lista(lista)
print(f"Lista fuera de la función: {lista}")  # La lista original se ve afectada


# EJERCICIO


def intercambiar_parametros(param1, param2):
    param1, param2 = param2, param1
    return param1, param2


x: int = 100
y: int = 200

nueva_x, nueva_y = intercambiar_parametros(x, y)
print(x, y)
print(nueva_x, nueva_y)

list_a = [1, 2, 3, 4, 5]
lista_b = [100, 200, 300, 400, 500]

nueva_lista_a, nueva_lista_b = intercambiar_parametros(list_a, lista_b)
print(f"Listas fuera de la función:\n{list_a, lista_b}")
print(f"Listas modificadas retornadas de la función:\n{nueva_lista_a, nueva_lista_b}")
