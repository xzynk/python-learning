# Operadores y Estructura de Control

Los operadores en python son simbolos que permiten realizar operaciones sobre variables y valores.

---
####  1 - Operadores Aritmeticos

| **<center>Operador</center>** |     <center>**Descripcion**</center>      | **<center>Ejemplo</center>** |
| :---------------------------: | :---------------------------------------: | :--------------------------: |
|      <center>+</center>       |           <center>Suma</center>           |    <center>x + y</center>    |
|      <center>-</center>       |          <center>Resta</center>           |    <center>x - y</center>    |
|      <center>*</center>       |      <center>Multiplicación</center>      |    <center>x * y</center>    |
|      <center>/</center>       | <center>Division (con decimales)</center> |    <center>x / y</center>    |
|      <center>//</center>      |              Division entera              |   <center>x // y</center>    |
|      <center>%</center>       |       Modulo (resto de la division)       |    <center>x % y</center>    |
|      <center>**</center>      |               Potenciacion                |   <center>x ** y</center>    |
####  2 - Operadores Comparación
Se usan para comprar dos valores, devolviendo **true** o **false**

| **<center>Operador</center>** | **<center>Descripcion</center>** | **<center>Ejemplo</center>** |
| :---------------------------: | :------------------------------: | :--------------------------: |
|              = =              |     <center>Igual a</center>     |            x = y             |
|              !=               |           Diferente de           |            x != y            |
|               >               |            Mayor que             |            x > y             |
|               <               |            Menor que             |            x < y             |
|              >=               |        Mayor o igual que         |            x >= y            |
|              <=               |        Menos o igual que         |            x <= y            |
####  3 - Operadores Asignación
Se usan para asignar valores de manera directa o con operaciones.

| **Operador** |       **Descripcion**        | **Ejemplos** |
| :----------: | :--------------------------: | :----------: |
|      =       |      Asignacion simple       |    x = 5     |
|      +=      |      Suma y asignacion       |    x += 5    |
|      -=      |      Resta y asignacion      |    x-= 5     |
|     * =      | Multiplicacion y asignacion  |   x * = 5    |
|     / =      |    Division y asignacion     |    x /= 5    |
|     //=      | Division entera y asignacion |   x //= 5    |
|      %=      |     Modulo y asignacion      |    x %= 5    |
|     ** =     |    Exponente y asignacion    |   x **= 5    |
#### 4 - Operadores Lógicos
Se utilizan para combinar varias condiciones logicas.

| **Operador** |                    **Descripcion**                    |     **Ejemplos**     |
| :----------: | :---------------------------------------------------: | :------------------: |
|     and      | Devuelve **true** si ambas condiciones son verdaderas | x > 5 **and** y < 10 |
|      or      |        Devuelve **true** si alguna es verdaera        | x > 5 **or** y < 10  |
|     not      |       Invierte el valor logico de la condición        |   **not** (x > 5)    |
#### 5 - Operadores de Identidad
Verifica si el valor se encuentra en una secuencia **(lista, string, etc )**

| **Operador** |            **Descripcion**            |  **Ejemplos**  |
| :----------: | :-----------------------------------: | :------------: |
|      is      |  Devuelve **true** si son identicos   |   x **is** y   |
|    is not    | Devuelve **true** si no son identicos | x **is not** y |
####  6 - Operadores de pertenencia

| **Operador** |            **Descripcion**            |      **Ejemplos**      |
| :----------: | :-----------------------------------: | :--------------------: |
|      in      |  Devuelve **true** si el valor esta   |   "a" **in** "apple"   |
|    not in    | Devuelve **true** si el valor no esta | "b" **not in** "apple" |
#### 7 - Operadores a nivel de bits

| **Operador** |         **Descripcion**         | **Ejemplos** |
| :----------: | :-----------------------------: | :----------: |
|      &       |       AND a nivel de bits       |    x & y     |
|      \|      |       OR a nivel de bits        |    x \| y    |
|      ^       |       XOR a nivel de bits       |    x ^ y     |
|      ~       | NOT a nivel de Bits (inversion) |    x ~ y     |
|      <<      |  Desplazamiento a la izquierda  |    x << 2    |
|      >>      |   Desplazamiento a la derecha   |    x >> 2    |

## Estructuras de control

Permiten alterar el flujo de ejecucion de un programa como condicionales, bucles o intrucciones para manejar excepciones.

#### 1 - Condicionales

Permite ejecutar un bloque de codigo u otro dependiendo de si una condicion es verdadera o falsa.

###### a) if, elif, else
```python
if condicion1
	# Codigo condicion1 si es TRUE
elif condicion2
	#Codigo si condicion2 es TRUE
else
	#Codigo si ninguna condicion es TRUE
```

###### b) match-case (Python 3.10+)
```python
def calculadora(operacion, a, b):
    match operacion:
        case "suma":
            return a + b
        case "resta":
            return a - b
        case "multiplicacion":
            return a * b
        case _:
            return "Operación no válida"

print(calculadora("suma", 10, 5))           # 15
print(calculadora("division", 10, 5))      # Operación no válida
```

#### 2 - Estructuras iterativas

###### a) Bucle for
Se usa para iterar sobre secuencias (listas, string, rangos, etc)

```Python
for element in iterable:
	# Codigo que se ejecuta en cada iteracion
```

###### b) While
Se ejecuta mientras la condicion sea verdadera

```Python
while condicion:
	# Codigo a ejecutar mientras la condicion sea TRUE
```

###### c) Palabras claves utiles
- **Break**: Interrumpe el bucle inmediatamente
- **Continue**: Salta a la siguiente iteracion del bucle

#### 3 - Manejo de excepciones

Las excepciones se usan para manejar errores durante la ejecucion del programa sin que este termine de forma abrupta.

###### a) try - except

```python
try:
	# Codigo que podria generar una excepcion
except:
	# Codigo que se ejecuta si ocurre una excepcion
```

###### b) try - except - finally

El bloque **finally** se ejecuta siempre, independientemente de si ocurrio o no una excepcion

```python
try:
	# Codigo que podria fallar
except:
	# Codigo para manejar la excepcion
finally:
	# Codigo que siempre se ejecuta
```

#### 4 - Otras estructuras de control

###### a) funciones - pass, return, yield

- **pass**: Se utiliza cuando se requiere una declaracion sintacticamente, pero no se quiere ejecutar ningun codigo
- **return**: Termina la ejecucion de una funcion y devuelve un valor
- **yield**: Se usa con funciones generadoras. Pausa la funcion y devuelve un valor. Al reanudar, el control regresa exactamente donde quedo.

###### b) assert

El operador **assert** lanza una excepcion si la expresion evaluada es falsa