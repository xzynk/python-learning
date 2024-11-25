#### 1 - LISTAS

```python
mi_lista = [1,2,3]
```

- Crea una secuencia ordenada de elementos

###### Operaciones Importantes

- **Acceso a elementos:** `mi_lista[0]` (primer elemento)
- **Añadir elemento:** `mi_lista.append(6)` añade al final
- **Eliminar elementos:** `mi_lista.remove(3)` elimina el 3
- **Concatenar lista:** `mi_lista.extend([7,8])` añade `[7,8]`
- **Ordenar:** `mi_list.sort()`

###### Casos de Uso
Una lista de carritos de compra, donde se necesita acceso rapido y la posibilidad de modificar el contenido.

###### Operaciones extras

- pop(): Elimina por indice y devuelve el valor, si no espeficas un indice elimina el ultimo
- reversed(): Invierte la lista
- len(): Verifica la longitud
- index(): Buscar elementos

#### 2 - TUPLA

```Python
mi_tupla = (10,20,30)
```

- Una tupla es similar a una lista, pero es **inmutable**, es decir, no se puede modificar una vez creada.
###### Operaciones importantes

- **Acceso a elementos:** `mi_tupla[1]` (segundo elemento)
- **Inmutabilidad:** No se puede cambiar `mi_tupla[1] = 25`
- **Desempaquetado:** `a, b, c = mi_tupla`

###### Casos de Uso
Coordenadas fijas (x,y) o una lista de constantes que no cambiaran, como los dias de la semana.

#### 3 - CONJUNTOS (SETS)

```python
mi_conjunto = {1,2,3,4,5}
```

- Es una coleccion desordenada de elementos unicos

###### Operaciones importantes

- **Añadir:** `mi_conjunto.add(6)`
- **Eliminar:** `mi_conjunto.remove()`
- **Eliminar duplicados:** Convertir una lista a un conjunto `set([1,1,2,2,3,3]) -> {1,2,3}`
- **Operacion de conjuntos:** Union (union()) , interseccion(), diferencia (difference())

###### Casos de uso
Cuando necesitar eliminar duplicados o realizar operaciones de teoria de conjuntos, como encontrar elementos comunes entre dos grupos.

#### 4 - DICCIONARIO (DICT)

```Python
mi_diccionario = {'nombre' : 'Carlos', 'edad' : 25}
```

###### Operaciones importantes

- **Acceso a valores:** `mi_diccionario['nombre']` devuelve *Carlos*
- **Añadir / Modificar valores:** `mi_diccionario['edad'] = 35`
- **Eliminar claves:** `del mi_diccionario['edad']`
- **Operaciones Comunes:** Obtener valores clave `keys()` los valores `values()`, o los pares `items()`
- **Buscar elementos:** Verificar si una clave esta presente `in`

###### Otras formas de eliminar

|               | **Modifica** | **Devuelve** |              **Caso**              |
| ------------- | :----------: | :----------: | :--------------------------------: |
| del           |      Si      |      No      | Cuando estas seguro de key y value |
| pop()         |      Si      |      Si      |     Cuando necesitas el valor      |
| popitem()     |      Si      | Si (Ultimo)  |    Necesitas eliminar el ultimo    |
| clear()       |  Si (todo)   |      No      |            Borrar Todo             |
| comprehension |  No (Copia)  |      No      |       Basado en condiciones        |
###### Casos de uso
Almacenar informacion donde cada elemento tiene una clave unica, como una libreta de direcciones.

#### 5 - CONJUNTOS ORDENADOS (OrderedDict)

```python
from collections import OrderedDict
mi_ordenado = OrderedDict()
mi_ordenado["uno"] = 1
mi_ordenado["dos"] = 2
```

- Igual que los diccionarios, pero mantienen el orden de insercion

###### Casos de uso
Cuando el orden de insercion importa, como registrar el orden de llegada de los clientes.

#### 6 - COLAS (queue)

```Python
from queue import Queue
mi_cola = Queue()
mi_cola.put(1)
mi_cola.put(2)
```

- Se utiliza cuando necesitas estructuras FIFO (first in first out)

###### Operaciones Importantes
- **Añadir y eliminar elementos:** `put(), get()`
- **Verficiar tamaño:** `qsize()`

###### Casos de Uso
Utilizada en procesamientos de tarea o en simulaciones donde los elementos deben procesarse en el orden que se añadieron.

#### 7 - DEQUES (deque)

```Python
from collections import deque
mi_deque = deque([1,2,3])
mi_deque.append(4)
mi_deque.appendleft(0)
```

###### Operaciones importantes
- **Añadir a ambos extremos:** `append(), appendLeft()`
- **Eliminar elementos por ambos extremos:** `pop(), popleft()`
- **Rotar:** `rotate()` rotar los elementos izquierda o derecha

###### Casos de uso
Util cuando necesitas una estructura con acceso rapido tanto al frente como al final, como una lista de navegacion (atras / adelante)

#### 8 - PILAS (stack)

```Python
mi_pila = []
mi_pila.append(1)
mi_pilar.pop()
```

###### Operaciones importantes
- **Añadir elementos:** `mi_pila.append(2)`
- **Eliminar ultimo elemento:** `mi_pila.pop()` devuelve el ultimo elemento y lo elimina

###### Casos de uso
Usada en algortimos que requieren una estructura LIFO (Last In, First out), como evaluar expresiones o hacer backtracking.

#### 9 - MATRICES (Arrays)

```python
import array
mi_array = array.array('i', [1,2,3,4])
```

###### Operaciones importantes
- **Acceso a elementos:** `mi_array[2]`
- **Añadir elementos:** `mi_array.append(5)`
- **Slicing:** Extraer subconjuntos de la matriz
- **Transformacion:** Usar expresiones algebraicas para modificarlo.

###### Casos de uso
Se usa cuando quieres modificar grandes cantidades de datos numericos, como en calculos cientificos o imagenes.