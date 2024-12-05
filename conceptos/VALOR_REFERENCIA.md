# VALOR Y REFERENCIA

En Python, la asignacion de variables y la forma en que se pasan a la funciones depende del **tipo de datos**, python utiliza un enfoque que se denomina **"paso por asignacion de referencia"**

#### Tipos inmutables
Como enteros, flotantes, cadenas, tuplas... se comportan como si se pasaran **"por valor"**

#### Tipos Multables
Como listas, diccionario y conjuntos, se comportan como si se pasaran **"por referencia"**

## 1 - Tipos inmutables

Los tipos inmutables no pueden ser modificados una vez creados. si intentas modificar uno de estos tipos dentro de una funcion, Python crea una nueva instancia del objeto, por lo que el objeto original fuera de la funciona no se ve afectado.

**Tipos inmutables en Python:**
- float (flotantes)
- Int (Enteros)
- str (cadenas)
- tuple (tuplas)

```Python
#Ejemplos

def modificar_valor(x):
	print(f"Valor antes de modificar: {x}")
	x += 10 # Se crea un nuevo entero
	print(f"Valor de x despues de modificar: {x}")

a = 5
modificar_valor(a)
print(f"Valor fuera de la funcion : {a}")
```

## 2 - Tipos mutables

Los tipos mutables pueden ser modificados despues de ser creados. Si modificas uno de estos tipos dentro de la funcion, los cambios se reflejan fuera de la funcion porque no se crea un nuevo objeto, si no que se modifica el objeto existente.

**Tipos mutables en python**
- list (listas)
- dict (diccionarios)
- set (conjuntos)

```python
#Ejemplos

def modificar_lista(lis):
	print(f"Lista dentro de la funciona antes de modificar: {lis}")
	lis.append(100)
	print(f"Lista dentro de la funciona despues de modificar: {lis}")

lista = [1,2,3]
modificar_lista(lista)
print(f"Lista fuera de la funcion: {lista}")
#La lista original se ve afectada
```

## 3 - Diferencias entre "por valor" y "por referencia"

- **Por valor (tipos inmultables)** Se crea una copia del valor dentro de la funciona y cualquier modificacion no afecta el valor original fuera de la funcion
- **Por referencia (tipos mutables)** Se pasa una referencia al mismo objeto, por lo que las modificaciones dentro de la funcion afectan al objeto original.

## 4 - Copia Superficial

- **¿Que es?** Crea una nueva estructura de datos, pero los elementos internos que son referencias a otros objetos apuntan a los mismos objetos que en la estructura original
- **¿Cuando se usa?** Cuando necesitas una nueva instancia de una estructura de datos, pero no quieres duplicar los objetos anidados.

```python
import copy
lista_original = [1,[2,3]]
lista_copia = copy.copy(lista_original)
lista_copia[1].append(4)

print(lista_original) # [1,[2,3,4]]
print(lista_copia) # [1,[2,3,4]]
```

## 5 - Copia Profunda

- **¿Que es?** Crea una nueva estructura de datos y tambien crea copias de todos los objetos anidados.
- **¿Cuando se usa?** Cuando nesecitas una copia completamente independiente de una estrucutra de datos, incluyendo todo sus elementos anidados.

```python
import copy

lista_orignal = [1,[2,3]]
lista_copia = copy.deepcopy(lista_original)
lista_copia[1].append(4)

print(lista_original) # [1,[2,3]]
print(lista_copia) # [1, [2,3,4]]
```


|        **Caracteristicas**         | **Copia Superficial** | **Copia Profunda** |
| :--------------------------------: | :-------------------: | :----------------: |
|           Nuevos Objetos           |          Si           |         Si         |
|      Copias Objetos Anidados       |          No           |         Si         |
| Mod en la copia afecta el original |          Si           |         No         |
|         Funcion de Python          |       copy.copy       |   copy.deepcopy    |
