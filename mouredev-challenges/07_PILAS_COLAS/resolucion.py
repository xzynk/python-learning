# PILAS (STACK)

stack = []

# Es una lista pero depende como la tratamos para ser considerado un stack
print(type(stack))

# Agregar elementos
stack.append(10)  # Push
stack.append(20)
stack.append(30)

# Ver el tope
print(stack[-1])  # Peek

# Sacar elementos
stack.pop()  # Elimina 30
stack.pop()  # ELimina 20

# Ver si esta vacía
print(len(stack) == 10)  # False aun tiene el 10

# COLAS (QUEUE)

from collections import deque

queue = deque()

print(type(queue))

# Agregar elementos
queue.append(100)  # enqueue
queue.append(200)
queue.append(300)

# Ver el primer elemento
print(queue[0])

# Sacar elemento
queue.popleft()
queue.popleft()

# Ver si esta vacía
print(len(queue) == 0)


# Ejercicio


def navegacion_historial():
    historial_navegacion: list = []
    indice_actual: int = 0

    def retornar_posicion():
        return print(f"\tEstas en: {historial_navegacion[indice_actual-1]}")

    def desplazar_indice(direccion: int):
        nonlocal indice_actual

        indice_actual += direccion

    def es_limite_inferior():
        return len(historial_navegacion) == 0 or indice_actual == 1

    def es_limite_superior():
        return len(historial_navegacion) == indice_actual

    while True:
        action = input(
            "Añade una url, o interactúa con las palabras adelante/atrás/salir:"
        ).lower()

        match action:
            case "adelante":
                if es_limite_superior():
                    print("No puedes ir mas adelante")
                else:
                    desplazar_indice(1)
                    retornar_posicion()
            case "atras":
                if es_limite_inferior():
                    print("No se puede ir mas atras")
                else:
                    desplazar_indice(-1)
                    retornar_posicion()
            case "salir":
                break
            case _:
                if es_limite_superior():
                    historial_navegacion.append(action)
                    indice_actual += 1
                else:
                    historial_navegacion = historial_navegacion[:indice_actual]
                    historial_navegacion.append(action)
                    indice_actual += 1

                retornar_posicion()


# navegacion_historial()


def manejo_impresion():
    cola_impresion = []

    def agregar_a_cola(archivo: str):
        nonlocal cola_impresion

        cola_impresion.append(archivo)
        return print(f"Se agrego: {archivo}")

    def procesar_impresion():
        if len(cola_impresion) == 0:
            return print("La cola de impresion esta vacia")

        return print(f"Se imprimio: {cola_impresion.pop(0)}")

    def ver_cola_impresion():
        if len(cola_impresion) == 0:
            print("La cola de impresion esta vacia.")
        else:
            print(f"Documentos en cola ({len(cola_impresion)}):")
            for idx, doc in enumerate(cola_impresion, 1):
                print(f"{idx}. {doc}")

    while True:
        action = input(
            "Agrega un documento, interactua con las palabras imprimir/salir\n"
        )

        match action:
            case "imprimir":
                procesar_impresion()
                ver_cola_impresion()
            case "salir":
                break
            case _:
                agregar_a_cola(action)
                ver_cola_impresion()


# manejo_impresion()
