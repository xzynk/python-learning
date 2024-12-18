# Pruebas Unitarias

Las pruebas unitarias (o unit test) son una tecnica fundamental en el desarrollo de software. Consiste en verificar el
comportamiento de las partes más pequeñas de un programa (generalmente funciones o métodos) de forma aislada.

#### Conceptos Clave sobre las pruebas unitarias

##### 1- ¿Que es una prueba unitaria?

- Una prueba unitaria evalua una unidad de código especifica de forma aislada (por ejemplo, una función)

##### 2- Características de una prueba unitaria

- **Independiente:** o depende de otras pruebas para ejecutarse.
- **Deterministica:** Produce siempre los mismos resultados si se ejecuta con las mismas entradas
- **Rapida:** Deberia ejecutarse en milisegundos
- **Simple y especifica:** Cada prueba debe evalua una unica funcionalidad especifca.

##### 3- Frameworks más utilizados

- Python: Unittest, pytest

#### Unittest en python

El modulo unittest es una biblioteca estandar de python para realizar pruebas unitarias.

```python
import unitTest


def add(a, b):
    return a + b


class TestMathOPerations(unittest.testCase):
    def test_add(self):
        self.assertEqual(add(2, 3)
        5)
        self.assertEqual(add(-1, 1)
        0)
        self.assertEqual(add(0, 0)
        0)

        if __name__ == "__main__"
            unittest.main()
```

- **assertEqual:** Verifica si dos valores son iguales
- **unittest.main():** Ejecuta todas las pruebas definidas en la clase.

##### Tipo de Asserts Comunes en unittest

1. **assertEqual(a,b):** Verifica si `a==b`
2. **assertTrue(x) / assertFalse(x):** Verifica si x es True o False
3. **assertRaise (exception, func, args):** Verifica si se lanza una excepcion especifica
4. **assertIn(a,b):** Verifica si **a** esta en **b**

#### Usando pytest: Alternativa más moderna

Pytest es otro framework muy popular por su simplicidad y flexibilidad

**Ejemplo de pytest**

```python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

Para ejecutar las pruebas simplemente ejecuta  
`pytest nombre_del_archivo.py`

Pytest detecta automaticamente las funciones de prueba que empiezan con test_

#### Ventajas de pruebas unitarias

1. **Deteccion temprana de errores:** Los problemas se detectan en etapas iniciales del desarrollo
2. **Facilitan los cambios:** Puedes refactorizar el código con confianza, sabiendo que las pruebas te alertaran si algo
   se rompe.
3. **Documentacion de código:** Las pruebas muestran como deberia comportarse cada función
4. **Evitan regresiones:** Detectan si cambios recientes rompen funcionalidades que antes funcionaban

#### Buenas practicas en las Pruebas Unitarias

1. **Prueba casos limite:** Asegurate de probar inputs extremos (como valores nulos o negativos)
2. **Cubre casos de error:** Verifica como maneja el código los inputs inesperados o errores.
3. **Evita dependencias externas:** Cada prueba deberia ejecutarse sin depende de elementos exgternos (como bases de
   datos o servicios externos)
4. **Usa mocks si es necesario:** Si tu función depende de recursos externos usa mocks para simular esos recursos.

```python
from unittest.mock import mock

# Simula una función que devuelve siempre 'Hola'
mock_func = Mock(return_value="Hola")
print(mock_func())  # 'Hola'
```
