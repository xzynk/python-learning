"""Expresiones Regulares"""

import re

string1: str = "Texto de prueba 1405"
string2: str = "Asi que el texto, para el texto, por el texto!"
string3: str = "13401023"

# re.match() Busca un patron al inicio de un string
rematch = re.match(r"Texto", string1)
print(rematch.group())  # .group() Devuelve la parte del string que coincide

# re.search() Busca el patron en cualquier parte de la string
research = re.search(r"texto", string2)
print(research.group())

# re.findall() Devuelve una lista con todas las coincidencias del patron.
refindall = re.findall(r"texto", string2)
print(refindall)

# re.finditer() Devuelve un iterador con objetos de coincidencia
refinditer = re.finditer(r"el", string2)
for coincidencia in refinditer:
    print(coincidencia.group())

# re.sub() Reemplaza la coincidencias por un string especificado
resub = re.sub(r"\s+", "-", string1)
print(resub)

# re.subn() Similar a re.sub() pero tambien devuelve el numero de reemplazos
resubn = re.subn(r"\s+", "-", string1)
print(resubn)

# re.split() Divide un string en partes usando un patron o delimitador
resplit = re.split(r"\s+", string1)
print(resplit)

# re.compile() Compila un patron en un objeto regex reutilizable
patron = re.compile(r"\d+")
resultado = patron.findall(string1)
print(resultado)

# re.fullmatch() Comprueba si toda la string coincide exactamente con un patron.
refullmatch = re.fullmatch(r"\d+", string3)
print(refullmatch.group())

# PATRONES BASICOS Y METACARACTERES
patron1 = re.findall(r"h.t", "hat ,hit, hot")
print(patron1)

patron2 = re.findall(r"^Hello", "Hello World, hello")
print(patron2)

patron3 = re.findall(r"hello$", "Hello World, hello")
print(patron3)

patron4 = re.findall(r"ab*", "a ab abb")
print(patron4)

patron5 = re.findall(r"ab+", "a ab abb")
print(patron5)

patron6 = re.findall(r"ab?", "a ab abb")
print(f"ab?: {patron6}")

patron7 = re.findall(r"\ba{3}\b", "a aa aaa aa abaaaba")
print(f"a{3}: {patron7}")

patron8 = re.findall(r"a{2,}", "a aa aaa aaaa")
print(patron8)

patron9 = re.findall(r"a{3,4}", "a aa aaa aaaa")
print(patron9)

patron10 = re.findall(r"a\+", "a+ aa aaa aaaa")
print(patron10)

patron10 = re.findall(r"[aeiou]", "a+ ve ci no nu")
print(patron10)

patron11 = re.findall(r"(ab)+", "ab abab")
print(patron11)

# SECUANCIAS ESPECIALES
# \d Digitos del 0 al 9
# \D No es un digito
# \w Caracter alfanumerico
# \W No es un caracter alfanumerico
# \s Espacio en blanco
# \S No es un espacio en blanco
# \b Limite de palabra
# \B No es un limite de palabra
# \\ Backslash

# Modificadores FLAGS
# re.IGNORECASE o re.I IGNORA MAYUSCULAS Y MINUSCULAS
flag1 = re.findall(r"ab*", "a ab Abb", re.I)
print(flag1)
# re.MULTILINE o re.M permite que funcione en multiple linea
# Tambien se pueden combinar diferentes FLAGS
flag2 = re.findall(r"^hello", "hello world\nHello Python\nHELLO everyone", re.M | re.I)
print(flag2)
