# Expresiones Regulares

Las **expresiones regulares** (regular expression o "regex") en Python son una herramienta poderosa para trabajar con patrones de texto. Se utilizan para buscar, analizar, validar o modificar cadenas de texto. Python proporciona el modulo `re` para trabajar con expresiones regulares.

### 1 - Importar el módulo `re`

```python
import re
```

### 2 - Funciones principales del módulo `re`

| Función          | Descripción                                                                                            |
| :--------------- | ------------------------------------------------------------------------------------------------------ |
| `re.match()`     | Busca un patron al **inicio** de un string. Devuelve un objeto de coincidencia o `None`                |
| `re.search()`    | Busca el patron en **cualquier parte** de la string. Devuelve el primer objeto o coincidencia o `None` |
| `re.findall()`    | Devuelve una lista con **todas las coincidencias** del patron.                                         |
| `re.finditer()`  | Devuelve un iterador con objetos de coincidencia para cada ocurrencia del patron.                      |
| `re.sub()`       | Reemplaza coincidencias del patron por un string especificado                                          |
| `re.subn()`      | Similar a `re.sub()` pero tambien devuelve el numero de reemplazos realizados.                         |
| `re.split()`     | Divide un string en partes usando un patron como delimitador                                           |
| `re.compile()`   | Compila un patron en un objeto regex reutilizable para busquedas mas eficientes                        |
| `re.fullmatch()` | Comprueba si toda la string coincide exactamente con un patron.                                        |

### 3 - Patrones basicos y metacaracteres

| Metacaracter | Significado                                           | Ejemplo de uso                                            |
| ------------ | ----------------------------------------------------- | --------------------------------------------------------- |
| `.`          | Cualquier caracter expecto nueva linea                | `"h.t"` coincide `hat`, `hit`,`hot`, etc                  |
| `^`          | Inicio de la string.                                  | `"^Hello"` coincide con strings que empiezan con `Hello`. |
| `$`          | Final de la string                                    | `"world$"` coincide con strings que terminan con `world`. |
| `*`          | Cero o mas repeticiones.                              | `"ab*"` coincide con `a`, `ab`, `abb`, etc.               |
| `+`          | Una o mas repeticiones                                | `"ab+"` coincide con `ab`, `abb`, pero no con `a`         |
| `?`          | Cero o una repeticion (opcionalidad)                  | `"ab?"` coincide con `a` o `ab`.                          |
| `{n}`        | Exactamente `n` repeticiones                          | `"a{3}"` coincide con `aaa`.                              |
| `{n, }`      | Al menos `n` repeticiones                             | `"a{2,}"` coincide con `aa`, `aaa`, etc.                  |
| `{n,m}`      | Entre `n` y `m` repeticiones                          | `"a{2,4}"` coincide con `aa`, `aaa`, o `aaaa`.            |
| `\`          | Escapa metacaracteres o define secuencias especiales. | `"a\+"` coincide con `a+`, no con `aa`.                   |
| `[]`         | Conjunto de caracteres                                | `"[aeiou]"` coincide con cualquier vocal.                 |
| `            | `                                                     | Alternativa lógica (OR).                                  |
| `()`         | Agrupacion o captura                                  | `"(ab)+"` coincide con `ab`, `abab`, etc.                 |
### 4 - Secuencias especiales

| Secuencia | Descripcion                                                 |
| --------- | ----------------------------------------------------------- |
| `\d`      | Digito (`[0-9]`)                                            |
| `\D`      | No es un digito (`[^0-9]`).                                 |
| `\w`      | Caracer alfanumerico (`[a-zA-Z0-9_]`).                      |
| `\W`      | No es alfanumérico (`[^a-zA-Z0-9_]`).                       |
| `\s`      | Espacio en blanco (incluye tabulaciones y saltos de línea). |
| `\S`      | No es un espacio en blanco.                                 |
| `\b`      | Límite de palabra.                                          |
| `\B`      | No es un límite de palabra.                                 |
| `\\`      | Escapa un backslash (`\`).                                  |
### 5 - Modificadores (flags)
Los **modificadores** cambian como se interpreta el patron:

| Flag                     | Descripcion                                                   |
| ------------------------ | ------------------------------------------------------------- |
| `re.IGNORECASE` o `re.I` | Ignora mayusculas y minusculas                                |
| `re.MULTILINE` o `re.M`  | Permite que `^` y `$`funciones en multiples lineas            |
| `re.DOTALL` o `re.S`     | Hace que `.` coincida tambien con saltos de linea             |
| `re.VERBOSE` o `re.X`    | permite agregar comentarios y espacios en patrones complejos. |
| `re.ASCII` o `re.A`      | Fuerza el patron a usar caracteres ASCII en lugar Unicode.    |
### 6 - Objetos de coincidencia (Match Object)
Cuando una busqueda tiene exito, se devuelve un objeto de coincidencia con varios metodos utiles:

| Metodo     | Descripcion                                          |
| ---------- | ---------------------------------------------------- |
| `.group()` | Devuelve la parte de la string que coincide          |
| `.start()` | Devuelve el indice inicial de la coincidencia        |
| `.end()`   | Devuelve el indice final de la coincidencia          |
| `.span()`  | Devuelve una tupla `(start, end) `de la coincidencia |

### 7 - Manejo de Excepciones
En python puedes manejar **expresiones regulares** y **manejo de excepciones**

#### Ejemplo 1: Manejo de errores de sintaxis en un patron
Si el patron tiene errores de sintaxis, puedes capturar la excepcion `re,error`.

```python
import re

try:
    #Patron mal formado (parentesis sin cerrar)
    pattern = re.compile(r"(\d+")
except re.error as e:
    print(f"Error en el patron: {e}")
```
#### Ejemplo 2: Validar numeros con expresiones regulares
Supongamos que quieres validar una entrada que debe ser un numero, y lanzar una excepcion personalizada si no cumple.

```python
import re

def validate_number(input_str):
    try:
        # Validar si la entrada es un número entero positivo
        if not re.fullmatch(r"\d+", input_str):
            raise ValueError(f"Invalid input: '{input_str}' is not a valid number")
        print(f"Valid number: {input_str}")
    except ValueError as e:
        print(e)

# Ejemplo de uso
validate_number("123")    # Válido
validate_number("12a3")   # No válido
```
#### Ejemplo 3: Manejo de excepciones al buscar patrones
Algunas funciones con expresiones regulares, como el acceso a un grupo inexistente en `re.match`pueden generar excepciones.

```python
import re

def extract_digits(input_str):
    try:
        match = re.search(r"(\d+)", input_str)
        if not match:
            raise ValueError("No numbers found in the input string")
        # Intentar acceder a un grupo inexistente genera IndexError
        print(f"First group: {match.group(1)}")
    except IndexError as e:
        print(f"Error accessing group: {e}")
    except ValueError as e:
        print(e)

# Ejemplo de uso
extract_digits("Hello 2024!")   # Encuentra números
extract_digits("No numbers!")  # No encuentra números
```
#### Ejemplo 4: Reintentar en caso de error
Si estas procesando varias cadenas y alguna no cumple, puedes capturar el error y continuar con el siguiente elemento.

```python
import re

strings = ["abc123", "456", "789xyz", "error!"]

for s in strings:
    try:
        # Intentar extraer el número completo de la cadena
        number = re.fullmatch(r"\d+", s).group()
        print(f"Valid number: {number}")
    except AttributeError:
        print(f"'{s}' is not a valid number")
```
