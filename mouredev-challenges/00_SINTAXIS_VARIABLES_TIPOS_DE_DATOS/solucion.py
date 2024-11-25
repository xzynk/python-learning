# Esto es un comentario
# http://www.python.org

"""
    Aunque esto lo podría usar para comentar en multiple línea,
    esto es una docstring que se usa para documentar, funciones, clases y modulos.
    A diferencia de los comentarios regulares, las docstrings están
    encerradas entre triple comillas y se colocan al inicio del bloque de código que documentan.
    Sirven para describir qué hace el código,
    sus parámetros, el valor de retorno, y otros detalles útiles.
"""
############

# - Crea una variable (y una constante si el lenguaje lo soporta).

my_var : int = 35
MY_VARIABLE_CONSTANTE : str = 'INMUTABLE'

# ---------------------------
# No existen variables constantes pero por convencion se usa MAYÚSCULAS
# Aunque python es de tipado dinamico puedes declarar el tipo de variable
# ---------------------------

# Tipo String
my_string : str = 'soy un cadena de texto'

# Tipo Numeric
my_number : int = 1 # Números enteros sin parte decimal
my_float : float = 3.14 #Numeros de punto flotante o parte decimal
my_complex : complex # Números complejos con parte real o imaginaria

# Tipo Boolean
my_bol : bool = True

# - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
print('Hola, Python')
