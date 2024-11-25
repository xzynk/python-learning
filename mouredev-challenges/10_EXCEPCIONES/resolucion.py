"""Excepciones"""

# Bloques Try-Except

try:
    # Código que puede causar una excepción
    division = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una excepción
    print("No se puede dividir entre 0")

# Else y Finally
# Else: Se ejecuta si no ocurre ninguna excepción

try:
    X = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Todo salio bien")

# Finally: Se ejecuta siempre, ocurra o no una excepción

try:
    with open("archivo.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    print("Bloque finally ejecutado")

# Lanzar excepciones con raise
# EDAD = 15
# if EDAD < 18:
#    raise ValueError("La edad debe ser mayor a 18")


# Excepciones personalizadas
class MiError(Exception):
    pass


# raise MiError("Este es un error personalizado")

# Principales tipos de excepciones:
# ZeroDivisionError
# FileNotFoundError
# ValueError
# TypeError
# IndexError


# Ejercicio
def procesador(one, two):
    """
    Crea una función que sea capaz de procesar parámetros, pero que también
    pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
    corresponderse con un tipo de excepción creada por nosotros de manera
    personalizada, y debe ser lanzada de manera manual) en caso de error.

    - Captura todas las excepciones desde el lugar donde llamas a la función.
    - Imprime el tipo de error.
    - Imprime si no se ha producido ningún error.
    - Imprime que la ejecución ha finalizado.
    """

    try:
        if one > 100:
            raise MiErrorPersonalizado(one, "El numero no puede ser mayor a 100")
        operacion = one / two
    except ZeroDivisionError:
        print("ZeroDivisionError: No se puede dividir entre cero")
    except TypeError:
        print("TypeError: Solo puedes dividir números")
    else:
        print(f"No hubo error: {operacion}")
    finally:
        print("Se acabo la ejecucion")


class MiErrorPersonalizado(Exception):
    def __init__(self, value, message="Numero invalido"):
        self.value = value
        self.message = message
        super().__init__(self.message)


procesador(2, 0)
procesador("a", "b")
procesador(10, 2)
procesador(155, 2)
