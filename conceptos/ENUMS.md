# ENUMERACIONES

Las enumeraciones (o "enums") en Python son una forma de agrupar un conjunto de nombres simbólicos vinculados a
valores unicos y constantes. Son utiles para hacer que el código sea más legible y mantenible al reemplazar valores
mágicos (números o cadenas que tienen un significado especifico en el código pero que no son explícitos) con nombres
descriptivos.

### 1. Introducción y Propósito:

- **Legibilidad:** Las enumeraciones mejoran la legibilidad del código al proporcionar nombres claros y descriptivos
  para los valores.
- **Mantenimiento:** Facilitan el mantenimiento al centralizar las constantes en un solo lugar. Si necesitas cambiar
  un valor, solo lo haces en la definición de la enumeración.
- **Prevención de errores:** Ayudan a prevenir errores al limitar los valores posibles a un conjunto definido.

### 2. Cómo se definen las enumeraciones en Python:

Python proporciona el módulo `enum` para trabajar con enumeraciones.

```python
from enum import Enum


class Color(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3


# Accediendo a los miembros de la enumeración
print(Color.ROJO)  # Output: Color.ROJO
print(Color.ROJO.name)  # Output: ROJO
print(Color.ROJO.value)  # Output: 1
```

En este ejemplo:

- `Color` es el nombre de la enumeración.
- `ROJO`, `VERDE` y `AZUL` son los miembros de la enumeración.
- `1`, `2` y `3` son los valores asociados a cada miembro.

### 3. Características importantes de las enumeraciones:

- **Unicidad de los valores (por defecto):** Por defecto los valores de los miembros de una enumeración deben ser
  únicos. Si intentas asignar el mismo valores a dos miembros se generará un error `ValueError`

```python
from enum import Enum

try:
    class Duplicado(Enum):
        A = 1
        B = 1  # Generará un ValueError: duplicate values found in <enum 'Duplicado'>: B -> 1
except ValueError as e:
    print(e)
```

- `auto()` **para la generación automática de valores:** Puedes usar `auto()` para que Python asigne automaticamente
  valores únicos a los miembros de la enumeración:

```python
from enum import Enum, auto


class Fruta(Enum):
    MANZANA = auto()
    BANANA = auto()
    CEREZA = auto()


print(Fruta.MANZANA.value)  # Output: 1
print(Fruta.BANANA.value)  # Output: 2
print(Fruta.CEREZA.value)  # Output: 3
```

- **Iteración sobre los miembros de una enumeración:** Puedes iterar sobre los miembros de una enumeración.

```python
from enum import Enum


class Dia(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3


for dia in Dia:
    print(f"{dia.name}: {dia.value}")
# Output:
# LUNES: 1
# MARTES: 2
# MIÉRCOLES: 3
```

- **Comparaciones:** Puedes comparar miembros de la misma enumeración:

```python
from enum import Enum


class Estado(Enum):
    ACTIVO = 1
    INACTIVO = 2


estado_actual = Estado.ACTIVO

if estado_actual == Estado.ACTIVO:
    print("El estado es activo")  # Se ejecuta esta línea
```

### 4. Subclases de `enum` y otros tipos de enumeraciones:

- `IntEnum`: Si queremos que la enumeración here de `int`, puedes usar `IntEnum`. Esto permite comparar miembros de
  la enumeración con enteros

```python
from enum import IntEnum


class Numero(IntEnum):
    UNO = 1
    DOS = 2


print(Numero.UNO == 1)  # Output: True
```

- `StrEnum` **(Python 3.11+)**: Para enumeraciones que hereden de `str`y se comparan como string, puedes usar `StrEnum`

### 5. Ejemplos de uso común:

- Representar estrados: Estados de una aplicación (ej: `Estado.CONECTADO`, `ESTADO.DESCONECTADO`)
- Opciones de configuración: Opciones que un usuario puede seleccionar (ej: `Formato.PDF`, `Formato.CSV`)