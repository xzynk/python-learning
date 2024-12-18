# RECURSIVIDAD

La **recursividad** es una técnica en programación en la cual una función se llama a sí misma para resolver un problema.
Se divide un problema en pequeños subproblemas más pequeños que son más fáciles de resolver.

#### Características de la Recursividad

1. **Caso Base:** Es la condición que detiene la recursion. Sin él, el programa entraria en un bucle infinito.
2. **Llamada recursiva:** La función se invoca a si misma con parametros más pequeña o modificados para acercarse al *
   *caso base**

#### Tipos de recursividad

1. **Recursividad Directa:** La función se llama a si misma.
2. **Recursividad Indirecta:** Una función llama a otra función que eventualmente lama de nuevo a la primera.

#### Ventajas de la Recursividad

- Simplifica la solución de problemas que pueden dividirse en subproblemas, como los arboles y las estructuras
  jerárquicas.
- A menudo resulta en un código más limpio y fácil de leer.

#### Desventajas de la Recursividad

- Consume más memoria debido a las multiples llamadas en la pila (stack) de ejecución.
- Si no se implementa correctamente, puede causar desbordamiento de pila (stack overflow)
- Puede ser ineficiente para algunos problemas, donde las soluciones iterativas funcionan mejor.

#### Ejemplos comunes de recursividad

1. **Factorial de un numero:**
    - **Caso Base:** Si `n == 0` entonces `factorial(0) == 1`
    - **Caso Recursivo:** Si `n > 0` entonces `factorial(n) = n * factorial(n - 1)`
2. **Suma de los primeros n números naturales:**
    - **Caso Base:** Si `n == 0` entonces `suma(0) = 0`
    - **Caso Recursivo:** Si `n > 0` entonces `suma(n) = n + suma (n - 1)`
3. **Serie Fibonacci:**
    - **Caso Base:** Si `n == 0` entonces `fibonacci(0) = 0` Si `n==1` entonces `fibonacci(1) = 1`
    - **Caso Recursivo:** Si `n>1` entonces `fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)`

   **Explicación:** `fibonacci(6)` llama a `fibonacci(5)` que a su vez llama a otros valores más pequeños hasta llegar a
   los casos `fibonacci(o) y fibonacci(1)`
4. **Búsqueda Binaria:**
   La búsqueda Binaria es un algortimo eficiente para buscar un elemento en una lsita ordenada, Si la lista esta
   ordenada, se puede dividir repetidamente a la mitad para encontrar el valor deseado.
    - **Caso Base:** Si el tamaño de la sublista es 0
    - **Caso Recursivo:** Si el elemento buscado es mayor o menor que el valor medio, se hace una llamada recursiva a la
      mitad derecha o izquierda de la lista.

#### Recursividad VS Iteracion

- **Ventajas de la recursividad:**
    - Es más fácil de entender y escribir para problemas que tienen estructura recursiva natural.
    - Proporciona un enfoque limpio y elegante para dividir y conquistar problemas
- **Desventajas de la recursividad:**
    - Consume más memoria y generalmente es ma corta.