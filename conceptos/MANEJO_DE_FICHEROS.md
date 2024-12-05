# Manejo de Ficheros

El manejo de ficheros (o archivos) en Python es importante para leer y escribir datos en archivos, ya sea para almacenar, procesar o analizar informacion.

#### 1 - Apertura de Archivos
Antes de leer o escribir en un archivo debes **abrirlo**. Python usa la funcion `open()` para abrir archivos.

```python
archivo = open("nombre_de_archivo.txt", modo)
```

##### Modos de Apertura
- **"r" (read)** : Modo de lectura, El archivo debe existir de lo contrario, se lanzara un error.
- **"w" (write):** Modo de escritura. Si le archivo existe, se sobreescribira. Si no existe, se creara.
- **"a" (append):** Modo de Adicion. Escribe al final del archivo sin sobrescribirlo. Si no existe, lo crea.
- **"x" (exclusive creation):** Crea un nuevo archivo. Si el archivo ya existe se lanzara un error
- **"b" (binary):** Modo binario, se usa para archivos binarios como imagenes o videos
- **"t" (text):** Modo Texto **(es el modo predeterminado)**
- **T (read/write):** Abrir el archivo tanto para lectura como para escritura.

#### 2 - Cerrar Archivos
Es fundamental **cerrar** un archivo despues de usarlo para liberar recursos del sistema. Se puede hacer usando el metodo `close()`

```python
archivo.close()
```

Sin embargo es mas recomendable usar la sentencia `with` para manejar archivos, ya que automaticamente cierra el archivo al terminar el bloque de codigo incluso si ocurre una excepcion.

```python
with open("nombre_archivo.txt", "r")
	contenido = archivo.read()
#Aqui el archivo ya esta cerrado
```

#### 3 - Lectura de Archivo
Python proporciona varias formas de leer datos de un archivo

**read()** : Lee todo el contenido del archivo como una cadena de texto

```python
with open("nombre_archivo.txt", "r")
	contenido = archivo.read()
	print(contenido)
```

**readline()** : Lee una sola linea del archivo a la vez

```python
with open("nombre_archivo.txt", "r")
	linea = archivo.readline()
	while linea:
		print(linea.strip())
		#Eliminar salto de lineas adicionales
		linea = archivo.readline()
```

**readlines()** : Lee todas las lineas del archivo y las devuelve como una lsita, donde cada linea es un elemento.

```python
with open("nombre_archivo.txt", "r")
	linea = archivo.readlines()
	for linea in lineas:
		print(linea.strip())
```

**Iteracion directa** Otra forma de leer un archivo linea por linea es iterar directamente sobre el objeto archivo:

```python
with open("nombre_archivo.txt", "r") as archivo
	for linea in archivo:
		print(linea.strip())
```

#### 4 - Escritura en Archivo
Para escribir en una archivo, se usa el modo "w", "a" o "x"

**write()** : Escribe una cadena de texto en el archivo. Si el archivo no existe, lo crea
```python
with open("nombre_archivo.txt", "w")
	archivo.write("Este es un archivo de prueba.\n")
	archivo.write("Esta es otra linea.\n")
```

**writelines()**: Escriba una lista de lineas en el archivo.
```python
lineas = ["Primera linea\n", "Segunda linea\n", "Tercera linea\n"]
with open("nombre_archivo.txt", "w") as archivo:
	archivo.writelines(lineas)
```

**Adicion de contenido ("a")**: Si quieres añadir contenido a un archivo sin sobrescribir su contenido.
```python
with open("nombre_archivo.txt", "w") as archivo:
	archivo.write("Nueva linea añadida al final \n")
```

#### 5 - Modos binarios
Para trabajar con archivos binarios (como imagenes, videos, etc) debes abrirlos en modo binario ("b")

##### Lectura de archivos binarios
```python
with open("imagen.png", "rb") as archivo:
	contenido = archivo.read()
	#Procesar el archivo binario
```

##### Escritura de archivos binarios
```python
with open("imagen.png", "wb") as archivo:
	archivo.write(contenido_binario)
```

#### 6 - Gestion de excepcion al manejar archivos
Es importante manejar los errores que pueden ocurrir durante la manipulacion de archivos, como archivos no encontrados, o permisos denegados. Para ello, puedes usar blosque `try - except`

```python
try:
	with open("nombre_archivo.txt", "r") as archivo:
		contenido = archivo.read()
except FileNotFoundError:
	print ("El archivo no existe")
except IOError:
	print ("Ocurrio un error al manejar el archivo.txt")
```

#### 7 - Ubicacion de archivos
Si no se proporciona una ruta completa Python asume que el archivo esta en el directorio de trabajo actual. Puedes usar rutas **realtivas** o **absolutas**

##### Rutas relativas
```python
with open("carpeta/archivo.txt", "r") as archivo:
	contenido = archivo.read()
```

##### Rutas absolutas
```python
with open("home/usuario/documentos/archivo.txt", "r") as archivo:
	contenido = archivo.read()
```

#### 8 - Metodos adicionales utiles
- **Seek (offset)**: Cambia la posicion actual del cursor en el archivo
- **teel()**: Retorna la posicion actual del cursor en el archivo
- **truncate(size)**: Corta el archivo al tamaño especificado

```python
with open("nombre_archivo.txt", "w") as archivo:
	print(archivo.tell()) #Posicion inicial: 0
	archivo.read(5) #Lee los primeros 5 caracteres
	print(archivo.tell()) #Posicion despues de leer 5 caracteres: 5
	archivo.seek(0) # Vuelve al inicio del archivo
	print(archivo.tell()) #Posicion despues de seek(0): 0
```

#### 9 - Gestion de archivos temporales
El modulo tempfile en Python permite crear archivos temporales que se eliminan automaticamente al finalizar el programa.

```python
import tempfile

with tempfile.NamedTemporaryFile(delete = False) as archivo_temp
	archivo_temp.write("Contenido temporal")
	print(f"Archivo temporal creado en {archivo_temp.name}")
```

#### 10 - Serializacion y deserializacion
Python permite **serializar** objetos (convertirlos a una representacion que se puede almacenar en archivos) usando el modulo pickle

##### Serializacion con Pickle
```python
import pickle
datos = {"Nombre" : "Juan", "Edad": 23}

with open("datos.pickle", "wb") as archivo:
	pickle.dump(datos, archivo)
```

##### Desceralizacion con Pickle
```python
with open("datos.pickle", "rb") as archivo:
	datos_recuperados = pickle.load(archivo)
	print(datos_recuperados)
```

#### 11 - Leer y escribir CSV
El modulo CSV permite trabajar facilmente con archivos CSV **(Valores separados por comas)**

##### Leer archivos CSV
```python
import csv

with open("archivo.csv", newline = " ") as archivo_csv
	lector = csv.reader(archivo_csv)
	for file in lector:
		print(file)
```

##### Escribir archivos CSV
```python
import csv

with open("archivo.csv", newline = " ") as archivo_csv
	escritor = csv.writer(archivo_csv)
	escritor.writerow(["Nombre", "Edad", "Ciudad"])
	escritor.writerow(["Juan", 25, "Lima"])
	escritor.writerow(["Ana", 30, "Bogota"])
```

#### 12 - Eliminar Archivos

```python
import os

if os.path.exists("mi_archivo.txt")
	os.remove("mi_archivo.txt")
	print("Archivo eliminado exitosamente")
else:
	print("El archivo no existe")
```