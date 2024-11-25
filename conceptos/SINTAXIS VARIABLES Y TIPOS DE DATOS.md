Los comentarios suelen llevar el simbolo **#**
Los comentarios en multilinea en si no existen pero existen los **DOCSTRING** se coloca al inicio del bloque de código que se documenta. Se usan para documentar funcionaes, clases y modulos.

**Variables**: En Python no necesitar declarar explicitamente una variable antes de usarla. Solo un valor.

```python
x = 5 # Variable de tipo entero
nombre = "Mia" # Variable de tipo string
pi = 3.14 # Variable de tipo float
```
<center>La asignacion se hace con el simbolo de = igual</center>

#### Reglas
- El nombre de una variable debe comenzar con una letra o un guion bajo, **pero no con un numero**
- No puede contener caracteres especiales **(!, @, #, %, $, etc)**
- No se permiten espacios
- No se pueden usar palabras reservadas **(if, while, for, etc)**

#### Tipo de Variables

1. Tipos Numéricos:
	- **INT** : Enteros, numeros sin parte decimal.
	- **FLOAT**: Números de punto flotante o decimales
	- **COMPLEX** : Números complejos con parte real o imaginaria
2. Tipo String:
	- **STR:** Cadenas de texto
		*Los string pueden ser cortados, manipulados o indexados*
		
```python
mensaje = "Hola, Mundo"
print(mensaje[0]) # H (Primer caracter)
print(mensaje[1:5]) # Ola, (subcadena desde el indice 1 al 4)
```

3. Tipo Booleano:
	- **Bool**: Valores de verdad, TRUE o FALSE
4. Tipo de Secuencia:
	- **List**: Lista de elementos que pueden ser de diferente tipos, es **mutable** (sus elementos pueden cambiar)
	- **Tuple**: Tupla de elementos, similar a una lista pero **inmutable**
	- **Range**: Secuencia de números útil para iterar en bucles
5. Tipo Set:
	- **Set**: Conjunto de elementos únicos, no tienen orden es mutable
6. Tipo Diccionario:
	- **Dict**: Estructura de datos que almacena clave-valor