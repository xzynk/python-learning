"""RECURSIVIDAD"""


def contador(numero):
    """Imprime números desde el parametro hasta 0 usando recursion"""
    if numero == 0:
        print(numero)
        return

    print(numero)
    contador(numero - 1)


contador(100)
print("FACTORIAL")


def factorial(numero):
    if numero == 0:
        return 1

    return numero * factorial(numero - 1)


print(factorial(7))
print("Fibonacci")

memo = {}


def fibonacci_memoizing(numero, memois):
    if numero in memois:
        return memois[numero]

    if numero == 0:
        return 0

    if numero == 1:
        return 1

    memo[numero] = fibonacci_memoizing(numero - 1, memois) + fibonacci_memoizing(
        numero - 2, memois
    )
    return memo[numero]


def fibonacci_dinamica(numero):
    if numero == 0:
        return 0
    if numero == 1:
        return 1

    fib = [0] * (numero + 1)
    fib[0], fib[1] = 0, 1
    for i in range(2, numero + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[numero]


print(fibonacci_memoizing(8, memo))
print(fibonacci_dinamica(12))
