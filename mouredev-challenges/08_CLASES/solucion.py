# CLASES


class ExampleClass:
    def __init__(self, name: str, lastname: str, user_code: int, supercode: int):
        self.name = name
        self.lastname = lastname
        # _ para proteger los atributos: aun se puede cambiar
        self._user_code = user_code
        # __ para proteger implementa el name mangling, que cambia el nombre
        self.__supercode = supercode

    def saludar(self):
        print(f"Hola yo soy {self.name} y me apellido {self.lastname}")

    def mostrar_codigo(self):
        print(f"Mi código es {self._user_code}")

    def mostrar_supercode(self):
        print(f"Mi código super secreto es: {self.__supercode}")


class Stack:
    """Genera funciones para el manejo de una lista como un stack"""

    def __init__(self) -> None:
        self._stack = []

    def push(self, element):
        """Agrega un elemento al stack
        Args:
            element (Any): Elemento a agregar
        Returns:
            Any: Retorna el elemento agregado
        """

        self._stack.append(element)
        return element

    def pop(self):
        """Elimina y retorna el ultimo elemento de la pila."""

        if len(self._stack) > 0:
            return self._stack.pop()

        return None  # Maneja el caso de una pila vacia

    def peek(self):
        """Devuelve el ultimo elemento de la pila sin eliminarlo"""

        if len(self._stack) > 0:
            return self._stack[-1]

        return None  # Manejo cuando la pila esta vacia

    def display(self):
        """Imprime todos los elementos en el stack"""

        for element in self._stack:
            print(element)

    def size(self):
        """Retorna el tamaño del stack"""
        return self._stack


# my_stack = Stack()
# print("Agrego elementos:")
# print(my_stack.push(1))
# print(my_stack.push(2))
# print(my_stack.push(3))
# print(my_stack.push(4))
# print("Elimino elementos:")
# print(my_stack.pop())
# print(my_stack.pop())
# print("Elementos en el stack:")
# my_stack.display()
# print("Veo el ultimo elemento:")
# print(my_stack.peek())
# print("Tamaño del stack:")
# print(my_stack.size())


class Queue:
    def __init__(self) -> None:
        self._list = []

    def add(self, element):
        self._list.append(element)
        return element

    def remove(self):
        if len(self._list) > 0:
            return self._list.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self._list[0]

        return None

    def is_empty(self) -> bool:
        return len(self._list) == 0

    def size(self):
        return len(self._list)

    def display(self):
        print(self._list)


my_list = Queue()
print(my_list.add(10))
print(my_list.add(20))
print(my_list.add(30))
print(my_list.add(40))
print(my_list.remove())
print(my_list.peek())
print(my_list.is_empty())
print(my_list.size())
my_list.display()
