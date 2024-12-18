"""EJERCICIO ENUMS"""

from enum import Enum


# Empleando tu lenguaje, explora la definición del tipo de dato
# que sirva para definir enumeraciones (Enum).
# Crea un Enum que represente los días de la semana del lunes
# al domingo, en ese orden. Con ese enumerado, crea una operación
# que muestre el nombre del día de la semana dependiendo del número entero
# utilizado (del 1 al 7).


class DiasSemana(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7


def mostrar_dia(numero):
    try:
        return DiasSemana(numero).name
    except ValueError:
        return "Numero invalido"


print(mostrar_dia(4))
print(mostrar_dia(5))
print(mostrar_dia(6))
print(mostrar_dia(9))
