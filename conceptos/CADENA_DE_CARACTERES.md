
# Cadena de Caracteres
####  1 - Creacion de Cadenas

```python
cadena1 = "Hola Mundo"
cadena2 = "Python es genial"
cadena3 = "Esto es una cadena \n
			de multiples lineas"
```

####  2 - Acceso a caracteres

```python
primer_caracter = cadena1[0] # 'H'
ultimo_caracter = cadena1[-1] # 'O'
```

#### 3 - Slicing

```python
subcadena1 = cadena1[0] # 'H'
subcadena2 = cadena1[5:] # ', mundo'
```

#### 4 - Longitud de la cadena

```python
longitud = len(cadena1) # 12
```

#### 5 - Metodos de cadenas

```python
# Convertir a mayusculas y minusculas
mayusculas = cadena1.upper() # 'HOLA, MUNDO'
minusculas = cadena1.lower() # 'hola, mundo'

#Capitalizar la cadena
capitalizada = cadena1.capitalize() # 'Hola, mundo'

#Reemplazar parte de la cadena
cadena_reemplazada = cadena1.replace("mundo" , "Python") # 'Hola, Python'

#Dividir la cadena
partes = cadena1.split(", ") # ['Hola', 'mundo']

#Unir una lista de cadenas
nueva_cadena = " ".join(partes) # 'Hola mundo'

#Buscar subcadenas
indice = cadena1.find("mundo") # 6
existe = "Python" in cadena1 # False
```

#### 6 - Formateo de Cadenas

```Python
nombre = "Juan"
edad = 30

#Usando el metodo formart()
cadena_formateada = "Mi nombre es {} y tengo {} años".format(nombre,edad)

#Usando f-strings (Python 3.6+)
cadena_formateada = f"Mi nombre es {nombre} y tengo {edad} años"
```

#### 7 - Concatenacion de Cadenas

```python
cadena_concatenada = cadena1 + " " + cadena2
```

#### 8 - Eliminar espacios en blanco

```python
cadena_con_espacios = " Hola,  mundo. "
cadena_sin_espacios = cadena_con_espacios.strip()
```

#### 9 - Verificacion de prefijos y sufijos

```python
empieza_con = cadena1.startswith("Hola") # True
termina_con = cadena1.endswith("mundo") # True
```

#### 10 - Repeticion de Cadenas

```python
cadena_repetida = "Hola" * 3 #HolaHolaHola
```

#### 11 - Invertir una cadena

```python
cadena_invertida = cadena1[::-1] #'odnum, aloH'
```

#### 12 - Cadenas vacias

```python
cadena_vacia = " "
es_vacia = len(cadena_vacia) == 0 # True
```

#### 13 - Iteracion sobre cadena

```python
for caracter in cadena:
	print(caracter) #Imprime cada caracter en una nueva linea
```

#### 14 - Contar ocurrencias

```python
contador = cadena1.count("o") # 2
```

#### 15 - Algunas funciones adicionales

```python
#Cambiar el case de una cadena
cadena_mayus = cadena1.title()

#Obtener el indice de la primera aparicion de un caracter
indice_caracter = cadena1.index('m') # 7

#Comprobar si todos los caracter son alfabeticos
todos_alfabeticos = cadena1.isalpha() #False por que contiene espacio y coma
todos_numericos = cadena1.isdigit() #False no son todos numeros

#Ordenar Palabras
palabra_ordenada = sorted(cadena1)
```