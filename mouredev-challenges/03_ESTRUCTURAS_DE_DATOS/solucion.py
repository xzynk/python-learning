"""ESTRUCTURA DE DATOS"""

# 1 - LISTAS (LIST)
# Crea una secuencia ordenada de elementos
print("1 - LISTAS (LIST)")
mi_lista = [1, 2, 3, 4, 5]
print(f"Mi lista: {mi_lista}")
# Operaciones
print(f"mi_lista[0] : {mi_lista[0]}")  # Acceso a elemento
mi_lista.append(6)  # Añadir elemento
print(f"mi_lista.append(6): {mi_lista}")
mi_lista.remove(3)  # Eliminar elemento
print(f"mi_lista.remove(3): {mi_lista}")
mi_lista.extend([7, 8, 9, 7, 7])  # Extender lista
print(f"mi_lista.extend([7, 8, 9]): {mi_lista}")
mi_lista.reverse()  # Revertir lista
print(f"mi_lista.reverse(): {mi_lista}")
mi_lista.sort()  # Ordenar lista
print(f"mi_lista.sort(): {mi_lista}")
print(
    f"mi_lista.pop(5): {mi_lista.pop(5)}"
)  # Sacamos un elemento de la lista y la retornamos
print(f"Mi lista: {mi_lista}")
print(f"len(mi_lista): {len(mi_lista)}")  # Verifica la longitud
print(
    f"mi_lista.count(7): {mi_lista.count(7)}"
)  # Contamos cuantas veces aparece cierto valor
print(type(mi_lista))
print("\n")

# 2 - TUPLAS (TUPLES)
# Una tupla es similar a la lista, pero es INMUTABLE
# es decir, no se puede modificar una vez creada
print("2 - TUPLAS (TUPLES)")
mi_tupla = (10, 20, 30, 20)
print(f"Mi tupla: {mi_tupla}")
print(f"mi_tupla[2] : {mi_tupla[2]}")  # Acceso a Elemento
print("a,b,c,d = mi_tupla")
a, b, c, d = mi_tupla  # Desempaquetar
print(f"a : {a}, b : {b}, c : {c}, d : {d}")
print(
    f"mi_tupla.count(20): {mi_tupla.count(20)}"
)  # Contamos cuantas veces aparece cierto valor
print(type(mi_tupla))
print("\n")

# 3 - CONJUNTOS (SET)
# Es una colección desordenada de elementos únicos
print("3 - CONJUNTOS (SET)")
mi_conjunto = {1, 2, 3, 4, 5}
print(f"Mi conjunto: {mi_conjunto}")
mi_conjunto.add(6)  # Añadir elemento
mi_conjunto.add(
    6
)  # No añade el elemento nuevamente, los sets solo tienen un elemento unico
print(f"mi_conjunto.add(6): {mi_conjunto}")
mi_conjunto.discard(9)  # Elimina el elemento si no lo encuentra no genera error
print(f"mi_conjunto.discard(9): {mi_conjunto}")
mi_conjunto.remove(5)  # Si no puede eliminar el elemento retorna error
print(f"mi_conjunto.remove(5): {mi_conjunto}")
# Retorna un nuevo conjunto que contiene todos los elementos de ambos sets
mi_conjunto = mi_conjunto.union({6, 7, 8, 9, 10})
print(f"mi_conjunto.union({{6, 7, 8, 9, 10}}): {mi_conjunto}")
# Retorna un nuevo conjunto que contiene los elementos que están en A pero no en B
mi_conjunto = mi_conjunto.difference({1, 4, 6, 8, 0})
print(f"mi_conjunto.difference({{1, 4, 6, 8, 0}}): {mi_conjunto}")
# Retorna un nuevo conjunto solo con los elementos presentes en ambos
mi_conjunto = mi_conjunto.intersection({2, 3, 9})
print(f"mi_conjunto.intersection({{2, 3, 9}}): {mi_conjunto}")
# Retorna un nuevo conjunto que contiene todos los elementos que son unicos.
mi_conjunto = mi_conjunto.symmetric_difference({1, 2, 3, 4, 5})
print(f"mi_conjunto.symmetric_difference({{1, 2, 3, 4, 5}}): {mi_conjunto}")
print(f"5 in mi_conjunto: {5 in mi_conjunto}")  # Buscar elemento IN
print(type(mi_conjunto))
print("\n")

# 4 - DICCIONARIO
# Un diccionario es una colección desordenada de pares clave-valor
print("4 - DICCIONARIO")
mi_diccionario = {"nombre": "Carlos", "edad": 25}
print(f"Mi diccionario: {mi_diccionario}")
print(f"mi_diccionario['nombre'] : {mi_diccionario['nombre']}")  # Acceso a los valores
print(f"mi_diccionario.get('edad') : {mi_diccionario.get('edad')}")
print(f"mi_diccionario['edad'] : {mi_diccionario['edad']}")
mi_diccionario["edad"] = 55  # Añadir o modificar valores
mi_diccionario.update({"nombre": "Cesar"})
print(f"mi_diccionario.update({{'nombre': 'Cesar'}}): {mi_diccionario})")
print(f"mi_diccionario['edad'] = 55 : {mi_diccionario}")
mi_diccionario["dni"] = 67859301
print(f"mi_diccionario['dni'] = 67859301 :{mi_diccionario}")
del mi_diccionario["edad"]
print(
    f"del mi_diccionario['edad']: {mi_diccionario}"
)  # Eliminar un elemento del diccionario
print(
    f"mi_diccionario.keys(): {mi_diccionario.keys()}"
)  # Retorna todas las clave como lista
print(
    f"mi_diccionario.values(): {mi_diccionario.values()}"
)  # Retorna todos los valores como lista
print(
    f"mi_diccionario.items(): {mi_diccionario.items()}"
)  # Retorna todos los items en lista
print(
    f"'nombre' in mi_diccionario : {'nombre' in mi_diccionario}"
)  # items existe en diccionario
print(f"mi_diccionario['nombre'] : {mi_diccionario}")
print(type(mi_diccionario))
print("\n")

# 5 - CONJUNTOS ORDENADOS
# Igual que los diccionarios, pero mantienen el orden
print("5 - CONJUNTOS ORDENADOS")
from collections import OrderedDict

mi_ordenado = OrderedDict()
mi_ordenado["uno"] = 1
mi_ordenado["dos"] = 2
mi_ordenado["tres"] = "tres"

print(f"Mi ordenado: {mi_ordenado}")
print("\n")

# 6 - COLAS (QUEUE)
# Se utiliza cuando necesitas estructuras FIFO (FIRST IN FIRST OUT)
from queue import Queue

print("6 - COLAS (QUEUE)")
mi_cola = Queue()
mi_cola.put(1)  # Añadir elementos
mi_cola.put(2)
mi_cola.put(3)
mi_cola.put(4)
# Conversion implícita de una Dequeue para visualizar
print(f"Mi cola: {mi_cola.queue}")  # Visualizar elementos
print(f"Extrae y elimina el elemento más 'antiguo' mi_cola.get(): {mi_cola.get()}")
print(f"Extrae y elimina el elemento más 'antiguo' mi_cola.get(): {mi_cola.get()}")
print(f"Mi cola: {mi_cola.queue}")
print(f"Mi cola esta vacia?: {mi_cola.empty()}")
print(type(mi_cola))
print("\n")

# 7 - Deques (DEQUEUE)
# Útil en casos cuando necesitas una estructura con acceso rapido tanto al frente como al final
print("7 - DEQUES (DEQUEUE)")
from collections import deque

mi_deque = deque()
mi_deque.append(4)  # Añadir elementos
mi_deque.append(5)
mi_deque.append(6)
print(f"Mi deque: {mi_deque}")
mi_deque.appendleft(7)
print(f"mi_deque.appendleft(7): {mi_deque}")  # Añadimos a la izquierda
print(f"mi_deque.pop(): {mi_deque.pop()}")  # Eliminamos y retornamos
print(f"mi_deque.popleft(): {mi_deque.popleft()}")  # Eliminamos el de la izquierda
print(f"Mi deque: {mi_deque}")
mi_deque.rotate()
print(f"mi_deque.rotate() : {mi_deque}")
print("\n")

# 8 - Pilas (STACK)
# Son iguales a las listas solo depende de su uso, el conjunto de operaciones que realizamos
# y el orden le dan un funcionamiento distinto
print("8 - PILAS (STACK)")
mi_pila = []
mi_pila.append(1)  # Añade elementos
mi_pila.append(2)
print(f"Mi pila: {mi_pila}")
mi_pila.pop(1)  # Elimina elementos
print(f"Mi pila: {mi_pila}")
print(type(mi_pila))
print("\n")

# 9 - Matrices (ARRAY)
# Se usa cuando quieres modificar grandes cantidades de datos numéricos,
# como calculos científicos o imágenes
print("9 - MATRICES (ARRAY)")
import array

mi_array = array.array(
    "i",
    [1, 2, 3, 4, 5],
)
print(f"Mi array: {mi_array}")
print(f"mi_array[0] : {mi_array[0]}")  # Acceso a los elementos
print(f"mi_array.append(6) : {mi_array.append(6)}")
print(f"Mi array: {mi_array}")
print("\n")


def mi_agenda():
    """Crea una agenda de contactos por terminal
    Debes implementar funcionalidades de búsqueda,
    inserción, actualización y eliminación de contactos"""

    agenda = {}

    def verificar_telefono(num_tel):
        cantidad_caracteres = 9

        if num_tel.isdigit() and len(num_tel) == 9:
            return int(num_tel)

        print(f"El número de telefono debe ser de {cantidad_caracteres} caracteres.")
        return None

    def actualizar_usuario(nombre, nuevo_nombre=None, nuevo_telefono=None):
        if nuevo_nombre:
            agenda[nuevo_nombre] = agenda.pop(nombre)
        if nuevo_telefono:
            agenda[nombre if not nuevo_nombre else nuevo_nombre] = nuevo_telefono

    def generar_input(mensaje):
        return input(mensaje + "\t")

    while True:
        print("Escogue una opcion:")
        print("\t" + "1. Buscar Contacto")
        print("\t" + "2. Agregar Contacto")
        print("\t" + "3. Actualizar Contacto")
        print("\t" + "4. Eliminar Contacto")
        print("\t" + "5. Salir" + "\n")

        option = generar_input("Selecciona tu opción:")

        match option:
            case "1":
                buscar_nombre = generar_input("Inserta el nombre de contacto: ")
                if buscar_nombre in agenda:
                    print(f"{buscar_nombre} y su telefono: {agenda[buscar_nombre]}")
                else:
                    print("No existe el contacto")
            case "2":
                es_valido = False

                while es_valido is False:
                    usuario = generar_input("Ingresa el nombre de usuario:")
                    telefono = verificar_telefono(
                        generar_input("Telefono del contacto: ")
                    )
                    if telefono is not None:
                        es_valido = True
                        agenda[usuario] = telefono
            case "3":
                usuario = generar_input("Ingresa el nombre de usuario:")
                if usuario in agenda:
                    print("Que deseas actualizar:")
                    print("\t" + "1. Nombre")
                    print("\t" + "2. Telefono")
                    print("\t" + "3. Ambas")

                    option = generar_input("Selecciona tu opcion:")

                    match option:
                        case "1":
                            actualizar_usuario(
                                usuario, generar_input("Nombre nuevo: "), None
                            )
                        case "2":
                            actualizar_usuario(
                                usuario, None, generar_input("Telefono nuevo: ")
                            )
                        case "3":
                            actualizar_usuario(
                                usuario,
                                generar_input("Nombre nuevo: "),
                                generar_input("Telefono nuevo: "),
                            )

                else:
                    print(f"No se encuentra {usuario} ")
            case "4":
                eliminar_usuario = generar_input("Ingrese el usuario a eliminar:")
                if eliminar_usuario in agenda:
                    print(f"Se elimino: {eliminar_usuario}")
                    del agenda[eliminar_usuario]
                else:
                    print("No existe el contacto")
            case "5":
                print("Hasta luego")
                break
            case _:
                print("Escogue un opcion válida")


mi_agenda()
