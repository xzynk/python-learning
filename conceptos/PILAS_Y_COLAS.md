# Pilas y Colas

#### Pilas (stack)

Una pila es una estrcutura de datos que sigue el principio **LIFO (Last in, first out)**, lo que significa que el ultimo
elemento que entra es el primero en salir.

- **Operaciones Básicas**
    1. push(elemento): Añadir un elemento al tope de la pila.
    2. pop(): Eliminar y devolver el elemento en el tope de la pila.
    3. peek() o top() : Obtener el elemento del tope sin eliminarlo.
    4. is.empty(): Verifica si la pila esta vacia.
    5. size(): Devolver el numero de elementos de la pila.

```python
stack = []

# Agregar elementos
stack.append(10)  # Push
stack.append(20)
stack.append(30)

# Ver el tope
print(stack[-1])  # Output: 30 (peek)

# Sacar elemento
stack.pop()  # Elimina 30
stack.pop()  # Elimina 20

# Ver si esta vacia
print(len(stack) == 0)  # Output: False
```

- **Aplicaciones de las Pilas:**
    - **Recursion:** La pila se usa para almacenar los estados de las funciones recursivas
    - **Backtracking:** Resolver problemas como laberintos, pruebas exhaustivas, etc.
    - **Algoritmo de evaluacion de expresiones:** Expresiones en notacion polaca inversa (Reverse Polish Notation)
    - **Deshacer / Rehacer:** Los comando se apilan y desapilan segun el flujo de cambios.

#### Colas (Queue)

Una **cola** es una estructura de datos que sigue el principio **FIFO (first in, first out)**, es decir, el primer
elemento que entra es el primer elemento en salir.

- **Operaciones Básicas**
    1. enqueue(elemento): Añadir un elemento al final de la cola.
    2. dequeue(): Eliminar y devolver el primer elemento de la cola.
    3. peek() o front(): Obtener el primer elemento sin eliminarlo.
    4. is_empty(): Verificar si la cola esta vacia.
    5. size(): Devolver el numero de elementos en la cola.

```python
from collections import deque

queue = deque()

# Agregar elementos
queue.append(10)  # enqueue
queue.append(20)
queue.append(30)

# Ver el primer elemento
print(queue[0])  # Output: 10 (peek)

# Sacar elementos
queue.popleft()  # Elimina 10
queue.popleft()  # Elimina 20

# Ver si esta vacia
print(len(queue) == 0)  # Output: False
```

- **Tipos especiales de Cola**
    1. **Cola Circular:** La cola tiene un tamaño fijo y los indices se 'envuelven' cuando llegan al final de la cola.
    2. **Cola de Prioridad:** los elementos se procesan en función a su prioridad, no en el orden que llegaron.
    3. **Deque (Double - ended Queue):** Permite agregar elementos tanto al inicio como al final de la cola..

*El más eficiente es con deque del modulo collections, ya que las operaciones de añadir y eliminar elementos en una
lista son costosas.*