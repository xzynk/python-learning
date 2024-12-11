# Iteraciones

Las **iteraciones** en python son fundamentales para recorrer secuencias, colecciones y cualquier objeto iterable. Estas permiten ejecutar un bloque de codigo varias veces, ya sea un numero de conocido de veces o hasta que se cumpla una condicion.

#### 1 - Tipos princpales de iteraciones

**Bucles Basicos**
1. `for`: Se utiliza para iterar sobre elementos de una secuencia (como listas, tuplas, cadenas o rangos)
2. `while`: Ejecuta un bloque de codigo mientras una condicion sea verdaera

---
#### 2 - Bucle `for`
El bucle `for` se utiliza para recorrer elementos de un iterable

**Sintaxis:**
```python
for element in iterable:
	# Codigo a ejecutar con cada elemento
```

**Ejemplo:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---
##### Uso de `range` en `for`
La funcion `range()` genera una secuencia de numeros

**Ejemplos**
```python
for i in range(5) #De 0 a 4
	print(i)

for i in range(2,10,2) # De 2 a 10 (excluido) pero de 2 en 2
	print(i)
```
---
#### 3 - Bucle `while`
El bucle while ejecuta codigo mientras una condicion sea verdaera

**Sintaxis:**
```python
while condition:
	#Codigo a ejecutar
```

**Ejemplo:**
```python
count = 0
while count < 5:
	print(count)
	count += 1
```

---

#### 4 - Palabras clave en bucles

| Palabra clave | Descripcion                                                                 |
| ------------- | --------------------------------------------------------------------------- |
| `break`       | Sale del bucle inmediatamente                                               |
| `continue`    | Salta a la siguiente iteracion del bucle                                    |
| `else`        | Ejecuta un bloque despues de que el bucle termine normalmente (sin `break`) |

**Ejemplo de `break` y `continue`**
```python
for i in range(10):
	if i == 5:
		break # Detiene el bucle cuando i es 5
	if i % 2 == 0:
		continue #Salta los numeros pares
	print(i)
```

**Ejemplo de `else`**
```python
for i in range(5):
	print(i)
else:
	print("El bucle termino sin interrupciones.")
```

---

#### 5 - Iteradores e iterables

**¿Que es un iterable?**  
Un objeto es iterable si se puede recorrer con un bucle `for`. Ejemplos: listas, cadenas, diccionarios, conjuntos, tuplas.

**¿Que es un iterador?**  
Un **iterador** es un objeto que produce elementos uno a uno al llamar a su metodo especial `__next__()`

**Convertir un iterable en iterador**
```python
iterable = [1,2,3]
iterador = iter(iterable) #Convierte el iterable en un iterador

print(next(iterador)) # Output: 1
print(next(iterador)) # Output: 2
```

Crear un **Iterador personalizado:** Puedes usar clases para crear tus propios iteradores implementando los metodos `__iter___()` y `__next__()`

```python
class Counter:
	def __init__(self, start, end):
		self.current = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.current > self.end:
			raise StopIteration
		self.current += 1
		return self.current - 1

counter = Counter(1,5)
for num in counter:
	print(num)
```

#### 6 - Comprensiones

**Compresion de listas**  
Es una forma concisa de crear listas usando bucles.

**Sintaxis:**
```python
[expression for item in iterable if condition]
```

**Ejemplo:**
```python
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares) #Output: [0,4,16,36,44]
```

**Compresion de diccionarios y conjutos**
```python
#Diccionarios
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict) #Output: {0:0,1:1,2:4,3:9,4:16}

#Conjuntos
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
print(unique_squares) #Output: {0,1,4}
```

**Compresion de generadores**  
Usa parentesis en lugar de corchetes para crear un generador:
```python
gen = (x**2 for x in range(10))
print(next(gen)) #Output: 0
print(next(gen)) #Output: 1
```

#### 7 - Itertools: Iteraciones Avanzadas
El modulo `itertools` proporciona herramientas avanzadas para iteraciones.

**Funciones utiles:**

| Funcion                    | Descripcion                                                        |
| -------------------------- | ------------------------------------------------------------------ |
| `itertools.count()`        | Genera una secuencia infinita de números desde un valor inicial.   |
| `itertools.cycle()`        | Cicla infinitamente a través de un iterable.                       |
| `itertools.repeat()`       | Repite un valor un número especificado de veces (o infinitamente). |
| `itertools.chain()`        | Combina múltiples iterables en uno solo.                           |
| `itertools.permutations()` | Genera todas las permutaciones posibles de un iterable.            |
| `itertools.combinations()` | Genera combinaciones únicas de un iterable.                        |        
**Ejemplo**
```python
from itertools import count, cycle, permutations

#Genera numeros infinitos desde 10
for num in count(10):
	if num > 15:
		break
	print(num)

#Permutaciones de "AB"
for p in permutations("AB",2):
	print(p) #Output: ('A', 'B') , ('B','A')
```

#### 8 - Manejo de multiples iterables

`zip()`  
Une elementos de multiples iterables en tuplas:
```python
names = ["Alice", "Bob"]
ages = [25, 30]

for name, age in zip(names, ages):
	print(f"{name} is {age} years old")
```

`enumerate()`  
Devuelve indices juntos con elementos:
```python
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
	print(f"{idx}: {fruit}")
```