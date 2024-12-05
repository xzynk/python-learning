# RECURSIVIDAD

La **recursividad** es una tecnica en programacion en la cual una funcion se llama a si misma para resolver un problema. Se divide un problema en pequeños subproblemas mas pequeños que son mas faciles de resolver.

#### Caracteristicas de la Recursivdad
1. **Caso Base:** Es la condicion que detiene la recursion. Sin el, el programa entraria en un bucle infinito.
2. **Llamada recursiva:** La funcion se invoca a si misma con parametros mas pequeños o modificados para acercase al **caso base**
#### Tipos de recursividad
1. **Recursividad Directa:** La funcion se llama a si misma.
2. **Recursividad Indirecta:** Una funcion llama a otra funcion que eventualmente lama de nuevo a la primera.
#### Ventajas de la Recursividad
- Simplifica la solucion de problemas que pueden dividirse en subproblemas, como los arboles y las estructuras jerarquicas.
- A menudo resulta en un codigo mas limpio y facil de leer.

#### Desventajas de la Recursividad
- Consume mas memoria debido a las multiples llamadas en la pila (stack) de ejecucion.
- Si no se implementa correctamente, puede causar desbordamiento de pila (stack overflow)
- Puede ser ineficiente para algunos problemas, donde las soluciones iterativas funcionan mejor.

#### Ejemplos comunes de recursividad
1. **Factorial de un numero:**
	- **Caso Base:** Si `n == 0` entonces `factorial(0) == 1`
	- **Caso Recursivo:** Si `n > 0` entonces `factorial(n) = n * factorial(n - 1)`
2. **Suma de los primeros n numeros naturales:**
	- **Caso Base:** Si `n == 0` entonces `suma(0) = 0`
	- **Caso Recursivo:** Si `n > 0` entonces `suma(n) = n + suma (n - 1)`
3. **Serie Fibonacci:** 
	- **Caso Base:** Si `n == 0` entonces `fibonacci(0) = 0` Si `n==1` entonces `fibonacci(1) = 1`
	- **Caso Recursivo:** Si `n>1` entonces `fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)`
	
	**Explicacion:** `fibonacci(6)` llama a `fibonacci(5)` que a su vez llama a otros valores mas pequeños hasta llegar a los casos `fibonacci(o) y fibonacci(1)`
4. **Busqueda Binaria:**
	La busqueda Binaria es un algortimo eficiente para buscar un elemento en una lsita ordenada, Si la lista esta ordenada, se puede dividir repetidamente a la mitad para encontrar el valor deseado.
	- **Caso Base:** Si el tamaño de la sublista es 0
	- **Caso Recursivo:** Si el elemento buscado es mayor o menor que el valor medio, se hace una llamada recursiva a la mitad derecha o izquierda de la lista.

#### Recursividad VS Iteracion
- **Ventajas de la recursividad:**
	- Es mas facil de entender y esxcribir para problemas que tienen estructura recursiva natural.
	- Proporciona un enfoque limpio y elegante para dividir y conquistar problemas
- **Desventajas de la recursividad:**
	- Consume mas memoria y generalmente es ma corta.