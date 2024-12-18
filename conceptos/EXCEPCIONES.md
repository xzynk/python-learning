# Excepciones

Las excepciones son errores que ocurren durante la ejecucion de un programa. Cuando Python encuentra un error,
interrumpe el flujo del programa.

#### Bloques try - except

Para manejar excepciones, usas bloques try - except

```python
try:
# Código que puede causar una excepcion
except TipoDeExcepcion:
# Código que se ejecuta si ocurre esa excepcion
```

#### else y finally

- **else:** Se ejecuta si no ocurre ninguna excepcion

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Todo salio bien")
```

#### finally

Se ejecuta siempre, ocurra o no una expcecion

```python
try:
    archivo = open("archivo.txt", r)
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    print("Bloque finally ejecutado")
```

#### Lanzar excepciones con raise

Puedes lanzar una excepcion usando **raise**:

```python
if edad < 18:
    raise ValueError("La edad debe ser mayor de 18")
```

#### Excepciones Personalizadas

Puedes crear tus propias excepciones creando clases que hereden de **exception:**

```python
class MiError(Exception):
    pass


raise MiError("Este es un error personalizado")
```

#### Principales tipos de excepciones

- ZeroDivisionError : Division por cero
- FileNotFoundError: Archivo no encontrado
- ValueError: Valor incorrecto
- TypeError: Tipo de dato incorrecto
- IndexError: Indice fuera de rango