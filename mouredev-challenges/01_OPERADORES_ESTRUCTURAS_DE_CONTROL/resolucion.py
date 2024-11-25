"""
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# Operadores
# 1 - Operadores Aritméticos
print("1 - Operadores Aritméticos")
print(f"Suma: 10 + 5 = {10 + 5}")  # Resultado : 15
print(f"Resta: 10 - 5 = {10 - 5}")  # Resultado : 5
print(f"Multiplicación: 10 * 5 = {10 * 5}")  # Resultado : 50
print(f"Division (Decimales): 10 / 5 = {15 / 4}")  # Resultado : 3.75
print(f"Division entera: 10 // 3 = {10 // 3}")  # Resultado : 3
print(f"Modulo (resto de la division): 10 % 3 = {10 % 3}")  # Resultado 1
print(f"Potencia: 10 ** 5 = {10 ** 5}")  # Resultado: 100000
print("\n")

# 2 - Operadores de Comparación
print("2 - Operadores de comparación")
print(f"Igual a (12 == 15) : {12 == 15}")  # Resultado False (no son iguales)
print(f"Diferente de (12 != 15) : {12 != 15}")  # Resultado True (son diferentes)
print(f"Mayor que (12 > 15) : {12 > 15}")  # Resultado False (no es mayor)
print(f"Menor que (12 < 15) : {12 < 15}")  # Resultado True (si es menor)
print(f"Mayor o igual (12 >= 15) : {12 >= 15}")  # Resultado False (no es mayor o igual)
print(f"Menor o igual (15 <= 15) : {15 <= 15}")  # Resultado True (si es menor o igual)
print("\n")

# 3 - Operadores de Asignación
MY_VAR = 5
print("3 - Operadores de Asignación")

print("Asignación simple: x=5")
print(MY_VAR)
print("Suma y asignación: x+=15")
MY_VAR += 15
print(MY_VAR)
print("Resta y asignación: x-=12")
MY_VAR -= 12
print(MY_VAR)
print("Multiplicación y asignación: x*=12")
MY_VAR *= 12
print(MY_VAR)
print("División y asignación: x/=2")
MY_VAR /= 2
print(MY_VAR)
print("División entera y asignación: x//=2")
MY_VAR //= 2
print(MY_VAR)
print("Módulo y asignación: x%=5")
MY_VAR %= 5
print(MY_VAR)
print("Exponente y asignación: x**=5")
MY_VAR **= 5
print(MY_VAR)
print("\n")

# 4 - Operadores Lógicos
print("4 - Operadores Lógicos")
print(f"Operador AND: (10 > 5 AND 25 < 10) = {10 > 5 and 25 < 10}")
print(f"Operador OR: (10 > 5 OR 25 < 10) = {10 > 5 or 25 < 10}")
print(f"Operador NOT: (not 15 < 5) = {not 15 < 5}")
print("\n")

# 5 - Operadores de Identidad
X = 15
Y = 12
print("5 - Operadores de Identidad")
print(f"Operador IS: 15 is 12 = {X is Y}")
print(f"Operador IS NOT: 15 is not 12 = {X is not Y}")
print("\n")

# 6 - Operadores de Pertenencia
print("6 - Operadores de Pertenencia")
print(f"Operador IN: 'a' in 'apple' = {'a' in 'apple'}")
print(f"Operador NOT IN: 'b' not in 'apple' = {'b' in 'apple'}")
print("\n")

# 7 - Operadores a Nivel de Bits
print("7 - Operadores a Nivel de Bits")
print(f"Operador AND (&): 1 & 0 = {1 & 0}")  # 0
print(f"Operador OR (|): 1 | 0 = {1 | 0}")  # 1
print(f"Operador XOR (^): 1 ^ 0 = {1 ^ 0}")  # 1
print(f"Operador NOT (~): ~ 0 = {~0}")  # 1
print(f"Desplazamiento a la izquierda (<<): 5 << 1 = {5 << 1}")  # 1
print(f"Desplazamiento a la derecha (<<): -10 >> 1 = {-10 >> 1}")  # -5
print("\n")

# Estructuras de control
print("Estructuras de control")

# 1 - Condicionales
print("1 - Condicionales")
# if, elif, else: Permite ejecutar un bloque de código o otro dependiendo de si
# una condición es verdadera o falsa
print("- if, elif, else:")
print("\tage = 15")

AGE = 15

if AGE < 18:
    print("\tEs menor de edad")
elif AGE == 18:
    print("\tJusto 18 años")
else:
    print("\tEs mayor de edad")

# 2 - Estructuras Iterativas
print("2 - Estructuras Iterativas")

print("- For:")
# For: Se usa para iterar sobre secuencias

for i in range(5):
    print(f"\t {i}")

print("- While:")
# While: Se ejecuta mientras la condición sea verdadera

VALUE = 0
while VALUE < 5:
    print(f"\t {VALUE}")
    VALUE += 1

print("- Palabras Útiles (break, continue):")
# break: interrumpe el bucle inmediatamente
# continue: Salta a la siguiente iteración del bucle
for i in range(5):
    if i == 3:
        break
    print(f"\t {i}")

print("\n")

# 3 - Manejo de excepciones
# Las excepciones se usan para manejar errores durante la ejecución
print("3 - Manejo de excepciones")
print("- try, except:")
print("\t1/0")
try:
    # Intentamos hacer la division
    division = 1 / 0
except ZeroDivisionError:
    # Se captura el error si intentamos dividir por cero
    print("\tError : Division por cero")

print("- try, except, finally:")
print("\t2/5")
try:
    # Intentamos hacer la division
    DIVISION = 2 / 5
except ZeroDivisionError:
    # Se captura el error si intentamos dividir por cero
    print("\tError : Division por cero")
else:
    # Este bloque se ejecuta si no ocurre ninguna excepción
    print(f"\tResultado: {DIVISION}")
finally:
    # Este bloque se ejecuta siempre, ocurra o no una excepción
    print("\tFinalizando la operación")

# 4 - Otras Estructuras de Control
print("4 - Otras Estructuras de Control")
print("- Funciones pass, return, yield")


def empty_function():
    """
    Funcion con un pass:
    pass: Se utiliza cuando se requiere una declaración sintácticamente,
    pero no se quiere ejecutar ningún código.
    """
    pass  # No hace nada


empty_function()


def add(a, b):
    """
    Funciona con un return final:
    return: Termina la ejecución de una funciona y devuelve un valor.
    """
    return print(f"\tEl resultado de la suma es: {a + b}")


print("\tFuncion con return: Suma(5+1)")
add(5, 1)


def my_generator():
    """
    Funcion con un generator y devuelve un valor.
    """
    yield 1
    yield 2
    yield 3


print("- Assert")
# Assert lanza una excepción si la expresión evaluada es falsa

ASSERT_VALUE = -1
# assert ASSERT_VALUE >= 0  # ASSERT_VALUE debe ser no negativo

print("\n")

# EJERCICIO EXTRA:
print("EJERCICIO EXTRA:")


def ret_values():
    """
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
    """
    for val in range(10, 56):
        if val % 2 == 0 and not (val % 3 == 0 or val == 16):
            print(val)


ret_values()
