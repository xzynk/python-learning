# CONJUNTOS

En Python, los **conjuntos** (sets) son una estructura de datos integrada que representa una colección  
**desordenada** y **mutable** de elementos únicos. Son utiles para operaciones como eliminar duplicados de una lista,  
realizar intersecciones, uniones y deferencias entre colecciones.

### Características principales de los conjuntos

1. **Elementos unicos:** Los conjuntos no permiten elementos duplicados. Si se intenta añadir un duplicado, se ignorara.
2. **Desordenados:** Los elementos no tienen un orden fijo
3. **Mutables:** Puedes añadir o eliminar elementos de un conjunto despues de crearlo.
4. **Elementos inmutables:** Los elementos dentro de un conjunto deben ser inmutables, como números, string o tuplas.  
   Sin embargo, no se pueden incluir listas, diccionarios ni otros conjuntos.

### Tipos de Conjuntos en Python

1. `set`: Conjuntos mutables que permiten agregar o eliminar elementos.
2. `fronzenset`: Conjuntos **inmutables**. Una vez cerados no pueden ser modificados

### Como trabajar con conjuntos

**Crear un conjunto**

```python
# Crear un conjunto vacio
empty_set = set()

# Crear un conjunto con elementos
numbers = {1, 2, 3, 4}

# Crear un conjunto a partir de una lista (automaticamente elimina duplicados)
unique_numbers = set([1, 2, 2, 3, 4])  # {1,2,3,4}
```

**Crear un** `frozenset`

```python
inmutable_set = frozenset([1, 2, 3, 4])
```

---

### Operaciones basicas con conjuntos

**Añadir y eliminar elementos**

```python
# Añadir un elemento
numbers.add(5)  # {1,2,3,4,5}

# Eliminar un elemento
numbers.remove(3)  # {1,2,4,5}
# Si no existe lanza un KeyError. Para evitarlo, usa discard():
numbers.discard(6)  # No pasa nada si no existe

# Eliminar y devolver un elemento aleatorio
numbers.spot()  # Eliminar un elemento cualquiera

# Vaciar el conjunto
numbers.clear()  # set()
```

### Operaciones entre conjuntos

- **Union (`|` o `union`):** Combina los elementos de dos conjuntos, eliminando duplicados

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # {1,2,3,4,5}
```

- **Intersección (`&` o `intersection`):** Obtiene los elementos comunes entre conjuntos.

```python
intersection_set = set1 & set2  # {3}
```

- **Diferencia (`-`o`difference`)**: Obtiene los elementos que están en un conjunto pero no en el otro.

```python
difference_set = set1 - set2    # {1, 2}
```

- **Diferencia simétrica (`^`o`symmetric_difference`)**: Elementos que están en un conjunto u otro, pero no en ambos.

```python
symmetric_diff_set = set1 ^ set2  # {1, 2, 4, 5}
```

---

### Operaciones utiles

#### Comprobaciones

- **Pertenencia**

```python
1 in set1  # True
6 in set1  # False
```

- **Subconjuntos y superconjuntos**

```python
set1 = {1, 2}
set2 = {1, 2, 3}
set1.issubset(set2)  # True
set2.issuperset(set1)  # True
```

- **Conjuntos disjuntos (sin elementos en comun)**

```python
set1 = {1, 2}
set2 = {3, 4}
set1.isdisjoint(set2)  # True
```

---

### Otras funciones utiles

- **Copiar un conjunto**

```python
copy_set = set1.copy()
```

- **Longitud**

```python
len(set1)  # Número de elementos en el conjunto
```

- **Convertir a lista o tupla**

```python
set_as_list = list(set1)
set_as_tuple = tuple(set1)
```

---

### Casos de uso de conjuntos

- **Eliminar duplicados de una lista:**

```python
my_list = [1, 2, 2, 3, 4, 4]
unique_elements = list(set(my_list))  # [1, 2, 3, 4]
```

- **Operaciones matemáticas entre colecciones:**

```python
primes = {2, 3, 5, 7}
evens = {2, 4, 6, 8}
primes_and_evens = primes & evens  # {2}
```

- **Verificar elementos unicos rapidamente:**

```python
my_set = {1, 2, 3}
print(4 in my_set)  # False
```

- **Eliminar elementos especificos de una coleccion:**

```python
to_remove = {1, 3}
data = {1, 2, 3, 4}
filtered_data = data - to_remove  # {2, 4}
```

---

**Diferencias entre `set` y `frozenset`**

| Caracteristica | `set`                 | `frozenset`                                   |
|----------------|-----------------------|-----------------------------------------------|
| Mutabilidad    | Mutable               | Inmutable                                     |
| Operaciones    | Puede añadir/eliminar | Solo lectura                                  |
| Uso comunes    | Manipulacion directa  | Clave en diccionarios o elementos de otro set |

---

### Ejemplo práctico: Contar palabras unicas en un texto

```python
text = "the quick brown fox jumps over the lazy dog the fox was quick"
words = text.split()  # Divide el texto en palabras
unique_words = set(words)  # Elimina duplicados
print(f"Unique words ({len(unique_words)}): {unique_words}")
# Resultado:
# Unique words (9): {'dog', 'lazy', 'over', 'brown', 'jumps', 'fox', 'quick', 'was', 'the'}
```