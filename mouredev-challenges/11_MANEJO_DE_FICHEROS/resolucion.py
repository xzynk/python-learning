"""
Manejo de Ficheros

# Desarrolla un programa capaz de crear un archivo que se llame como
# tu usuario de GitHub y tenga la extensión .txt.
# Añade varias líneas en ese fichero:
# - Tu nombre.
# - Edad.
# - Lenguaje de programación favorito.
# Imprime el contenido.
# Borra el fichero.

"""

import os

# Creamos el archivo, con open. Python crea automáticamente el archivo si no existe.

with open("mi_archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Anthony\n")
    archivo.write("35\n")
    archivo.write("Python")

# Imprimimos el contenido

with open("mi_archivo.txt", "r", encoding="utf-8") as archivo:
    linea = archivo.readline()

    while linea:
        print(linea.strip())  # Elimina saltos de línea adicionales
        linea = archivo.readline()

# Borramos el   fichero
if os.path.exists("mi_archivo.txt"):
    os.remove("mi_archivo.txt")
    print("Archivo eliminado exitosamente")
else:
    print("El archivo no existe")
