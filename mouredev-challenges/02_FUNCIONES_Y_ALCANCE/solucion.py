# Funciones definidas por el usuario

# Funciones sin parámetros ni retorno


def saludo():
    """Imprime un saludo"""
    print("Hola, como estas")


saludo()


# Funciones con parámetros y sin retorno


def saludo_personalizado(nombre):
    """Aquí, la función toma un parametro nombre, lo utiliza en el print, pero no devuelve nada"""
    print(f"Hola, {nombre}")


saludo_personalizado("Mia")


# Funciones con parámetros y retorno


def suma(a, b):
    """Esta función toma dos parametros, los suma y devuelve el resultado"""
    return a + b


print(f"Sumamos 5 + 3 : {suma(5, 3)}")


# Funcion con multiples valores de retorno


def operaciones_basicas(a, b):
    """Esta funciona realiza varias operaciones con dos parametros y devuelve una tupla
    de los resultados"""
    sumando = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return sumando, resta, multiplicacion, division


print(operaciones_basicas(24, 3))

# También se pueden guardan los valores en distintas variables
plus, rest, mult, div = operaciones_basicas(24, 3)
print(plus)
print(rest)
print(mult)
print(div)


# Funcion con numero indefinido de parámetros
def sum_all(*args):
    """aquí *args permite pasar un numero variable de argumentos. La función
    sumara todos los números que reciba"""
    return sum(args)


print(f"Sumamos 1 + 2 + 3 = {sum_all(1, 2, 3)}")


# Funcion con argumentos nombrados indefinidos
def print_kwargs(**kwargs):
    """Este tipo de función aceptar un número indefinido de argumentos valor-clave"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(a=1, b=2, c=3)

# Funciones anónimas
# Las funciones lambda son útiles cuando necesitas una función pequeña y anónima
double = lambda x: x * 2
print(double(10))


# Funcion dentro de función
def operacion_compleja(a, b):
    """También llamadas nested function o funciones anidadas"""

    def potencia(a, b):
        return a**b

    def division_entera(a, b):
        return a // b

    return potencia(a, b), division_entera(a, b)


print(f"Ejecutamos 24**2 y 24//2 {operacion_compleja(24, 2)}")


# Funciones de Orden Superior
def aplicar_operacion(func, a, b):
    """Esta es una función de orden superior, como argumento le pasamos el nombre de una función"""
    return func(a, b)


print(f"Sumamos 24 + 100: {aplicar_operacion(suma, 24, 100)}")

# Variables LOCALES VS GLOBALES

numero = 10


def funcion_local():
    numero = 5  # Variable local
    print(f"Valor local de numero: {numero}")


def funcion_global():
    global numero
    numero = 20
    print(f"Valor global de numero modificado: {numero}")


print(f"Valor inicial de numero: {numero}")
funcion_local()
print(f"Valor global de numero despues de la función local: {numero}")
funcion_global()
print(f"Valor global de numero despues de la función global: {numero}")
print("\n")

# Funciones ya creadas en Python
# 1 - print(): Imprime objetos en la consola
print("Usando una función print")
# 2 - len(): Devuelve la longitud de un objeto (listas, string, etc)
print(f"len([1,2,3]) : {len([1, 2, 3])}")
print(f"len(\"Hello\") : {len('Hello')}")
# 3 - type(): Devuelve el tipo de un objeto
print(f"type(5) : {type(5)}")
print(f"type([1,2,3]) : {type([1, 2, 3])}")
# 4 - int(), float(), str(): Convierte datos a tipos números o string
print(f"int(\"10\") : {int('10')}")
print(f"float(\"10.5\") : {float('10.5')}")
print(f"str(10) : {str(10)}")
# 5 - sum(): Suma los elementos de un iterable (lista, tuple)
print(f"sum([10,25,55]) : {sum([10, 25, 55])}")
# 6 - max(), min(): Devuelve el valor máximo o minimo de un iterable
print(f"max([1,2,3]) : {max([1, 2, 3])}")
print(f"min([1,2,3]) : {min([1, 2, 3])}")
# 7 - abs(): Devuelve el valor absoluto de un numero
print(f"abs(-5) : {abs(-5)}")
# 8 - round(): Redondea un número de decimales especificado
print(f"round(5.678, 2) : {round(5.678, 2)}")
# 9 - range(): Genera una secuencia de números
print("range(5):")
for i in range(5):
    print(i)
# 10 - enumerate(): Devuelve un iterador que genera un indice y el valor correspondiente
print("enumerate([1, 2, 3, 4, 5])")
for index, value in enumerate([1, 2, 3, 4, 5]):
    print(f"{index}: {value}")
# 11 - zip(): Combina varios iterables, creando tuplas con sus elementos correspondientes
print(f"zip([1,2,3],['a','b','c']) : {list(zip([1, 2, 3], ['a', 'b', 'c']))}")
# 12 - map(): Aplica una función a todos los elementos de un iterable
print(
    f"map(lambda x: x * 2, [1, 2, 3, 4, 5]) : {list(map((lambda x: x * 2), [1, 2, 3, 4, 5]))}"
)
# 13 - filter(): Filtra los elementos de un iterable usando una función
print(
    f"list(filter(lambda x: x > 2, [1, 2, 3, 4, 5]) : {list(filter(lambda x: x > 2, [1, 2, 3, 4, 5]))})"
)
# 14 - sorted(): Devuelve una lista ordenada de un iterable
print(f"sorted([5, 4, 1, 2, 3]) : {sorted([5, 4, 1, 2, 3])}")
# 15 - all(), any():
# all(): Devuelve True si todos los elementos de un iterable son verdaderos
# any(): Devuelve True si al menos un elemento de un iterable es verdadero
print(f"all([True, True, True, True, True]): {all([True, True, True, True])}")
print(f"any([False, True, True, True, False]): {any([False, True, True, True, False])}")
# 16 - input(): Recibe una entrada de usuario
print("input(): Recibe entrada de usuario en consola")
# 17 - isinstance(): Verifica si un objeto es de un tipo en particular
print(f"isinstance(5, int) : {isinstance(5, int)}")
# 18 - open(): Abre un archivo para lectura o escritura
print("open(): Abre un archivo para lectura o escritura")
# 19 - help(): Muestra la documentacion de un objeto
# 20 - dir(): Muestra los atributos y métodos de un objeto
print(dir(str))
# 21- reversed(): Invierte el orden de una lista
print(f"reversed([1, 2, 3, 4, 5]) : {list(reversed([1, 2, 3, 4, 5]))}")
print("\n")


# EJERCICIO FINAL
def imprimir_con_reemplazos(firstStr, secondStr):
    """
    Imprime números del 1 al 100 si es multiplo de 3 lo reemplaza con el primer string
    si es multiple de 5 con el segundo string y si es multiplo de ambos muestra los dos string
    :param firstStr:
    :param secondStr:
    :return: Los números del 1 al 100 con el reemplazo de String
    """
    count = 0
    for val in range(1, 101):
        if val % 3 == 0 and val % 5 == 0:
            print(firstStr + secondStr)
        elif val % 3 == 0:
            print(firstStr)
        elif val % 5 == 0:
            print(secondStr)
        else:
            print(val)
            count += 1

    return count


print(imprimir_con_reemplazos("foo", "bar"))
