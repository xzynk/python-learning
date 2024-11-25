"""04 -CADENAS DE CARACTERES"""

# 1 - CREACIÓN DE CADENAS
CADENA1 = "Hola, mundo"
CADENA2 = 'python es genial'
CADENA3 = '''Esto es una cadena
de multiuples lineas.'''

print(f"{CADENA1}\n{CADENA2}\n{CADENA3}")
print("\n")

# 2 - ACCESO A CARACTERES
PRIMER_CARACTER = CADENA1[0]
print(f"cadena1[0] : {PRIMER_CARACTER}")
ULTIMO_CARACTER = CADENA1[-1]
print(f"cadena1[-1] : {ULTIMO_CARACTER}")
print("\n")

# 3 - SLICING
SUBCADENA = CADENA1[0:4]
print(f"cadena1[0:4] : {SUBCADENA}")
SUBCADENA2 = CADENA1[5:]
print(f"cadena1[5:] : {SUBCADENA2}")
print("\n")

# 4 - LONGITUD DE LA CADENA
LONGITUD = len(CADENA1)
print(f"len(cadena1) : {LONGITUD}")
print("\n")

# 5 - MÉTODOS DE CADENAS
# Convertir mayúsculas y minúsculas
MAYUSCULAS = CADENA1.upper()
print(f"CADENA1.upper() : {MAYUSCULAS}")
MINUSCULAS = CADENA1.lower()
print(f"CADENA1.lower() : {MINUSCULAS}")

# Capitalizar la cadena
CAPITALIZADA = CADENA2.capitalize()
print(f"CADENA2.capitalize() : {CAPITALIZADA}")

# Reemplazar parte de la cadena
CADENA_REEMPLAZADA = CADENA1.replace("mundo", "Python")
print(f"CADENA1.replace('mundo', 'Python') : {CADENA_REEMPLAZADA}")

# Dividir la cadena
PARTES = CADENA1.split(", ")
print(f"CADENA1.split(\", \") = {PARTES}")

# Unir una lista de cadenas
NUEVA_CADENA = " ".join(PARTES)
print(f"\" \".join(PARTES)) : {NUEVA_CADENA}")

# Buscar subcadenas
INDICE = CADENA1.find("mundo")
print(f"CADENA1.find('mundo') : {INDICE}")
EXISTE = "Python" in CADENA1
print(f"\"Python\" in CADENA1 : {EXISTE}")
print("\n")

# 6 - FORMATEO DE CADENAS
# Usando format()
NOMBRE = "JUAN"
EDAD = 30
CADENA_FORMATEADA = "Mi nombre es {} y tengo {} años".format(NOMBRE, EDAD)
print(f"CADENA_DE_TEXTO.format(NOMBRE, EDAD) : {CADENA_FORMATEADA}")

# Usando F-STRINGS (Python 3.6)
CADENA_FORMATEADA_F = f"Mi nombre es {NOMBRE} y tengo {EDAD} años"
print(f"f\"Mi nombre es {{NOMBRE}} y tengo {{EDAD}} años\" = {CADENA_FORMATEADA_F}")
print("\n")

# 7 - CONCATENACIÓN DE CADENAS
CADENA_CONCATENADA = CADENA1 + " " + CADENA2
print(f"CADENA1 + \" \" + CADENA2 : {CADENA_CONCATENADA}")
print("\n")

# 8 - ELIMINAR ESPACIOS EN BLANCO
CADENA_CON_ESPACIOS = "     Hola,    mundo     "
print(f"CADENA_CON_ESPACIOS : {CADENA_CON_ESPACIOS}")
CADENA_SIN_ESPACIOS = CADENA_CON_ESPACIOS.strip()
print(f"CADENA_CON_ESPACIOS.strip() : {CADENA_SIN_ESPACIOS}")
print("\n")

# 9 - VERIFICACIÓN DE PREFIJOS Y SUFIJOS
EMPIEZA_CON = CADENA1.startswith("Hola")
print(f"CADENA1.startswith('Hola') : {EMPIEZA_CON}")
TERMINA_CON = CADENA1.endswith("mundo")
print(f"CADENA1.endswith('mundo') : {TERMINA_CON}")
print("\n")

# 10 - REPETICION DE CADENAS
CADENA_REPETIDA = "Hola" * 3
print(f"\"Hola\" * 3 : {CADENA_REPETIDA}")
print("\n")

# 11 - INVERTIR UNA CADENA
CADENA_INVERTIDA = CADENA1[::-1]
print(f"CADENA1[::-1] : {CADENA_INVERTIDA}")
print("\n")

# 12 - CADENAS VACÍAS
CADENA_VACIA = ""
ES_VACIA = len(CADENA_VACIA) == 0
print(f"len(CADENA_VACIA) == 0 : {ES_VACIA}")
print("\n")

# 13 - ITERACIÓN SOBRE UNA CADENA
print("for caracter in CADENA1:")
for caracter in CADENA1:
    print(caracter)
print("\n")

# 14 - CONTAR OCURRENCIAS
CONTADOR = CADENA1.count("o")
print(f"CADENA1.count('o') : {CONTADOR}")
print("\n")

# 15 - ALGUNAS FUNCIONES ADICIONALES
# Cambiar el case de una cadena
CADENA_MAYUS = CADENA1.title()
print(f"CADENA1.title() : {CADENA_MAYUS}")
# Obtener el índice de la primera aparición de un carácter
INDICE_CARACTER = CADENA1.index("m")
print(f"CADENA1.index('m') : {INDICE_CARACTER}")
# Comprobar si todos los caracteres son alfabéticos
TODOS_ALFABETICOS = CADENA1.isalpha()
print(f"CADENA1.isalpha() : {TODOS_ALFABETICOS}")
TODOS_NUMERICOS = CADENA1.isdigit()
print(f"CADENA1.isdigit() : {TODOS_NUMERICOS}")
print("\n\n")


def verifica_palabras(palabra1, palabra2):
    """ Crea un programa que analice dos palabras diferentes y realice comprobaciones
     para descubrir si son: PALINDROMOS, ANAGRAMAS, ISOGRAMAS"""

    def es_palindromo(palabra):
        if palabra.lower() == palabra.lower()[::-1]:
            return f"{palabra} es Palindromo"

        return f"{palabra} no es Palindromo"

    def son_anagramas():
        if len(palabra1) != len(palabra2):
            return "No son anagramas"

        return "Son Anagramas" \
            if sorted(palabra1.lower()) == sorted(palabra2.lower()) \
            else f"{palabra1} y {palabra2} no son Anagramas"

    def es_isograma(palabra):
        letra_dict = {}

        for letra in palabra:
            letra_dict[letra] = letra_dict.get(letra, 0) + 1

        valores_set = set(letra_dict.values())

        return f"{palabra} es isograma" if len(valores_set) == 1 else f"{palabra} no es isograma"

    print(es_palindromo(palabra1))
    print(es_palindromo(palabra2))
    print(son_anagramas())
    print(es_isograma(palabra1))
    print(es_isograma(palabra2))


verifica_palabras("gato", "loco")
