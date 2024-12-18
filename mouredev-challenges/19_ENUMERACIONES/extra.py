"""EJERCICIO EXTRA"""

from enum import Enum


# Crea un pequeño sistema de gestión del estado de pedidos.
# Implementa una clase que defina un pedido con las siguientes características:
# El pedido tiene un identificador y un estado.
# El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
# Implementa las funciones que sirvan para modificar el estado:
# Pedido enviado
# Pedido cancelado
# Pedido entregado
# (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc.)
# Implementa una función para mostrar un texto descriptivo según el estado actual.
# Crea diferentes pedidos y muestra cómo se interactúa con ellos.


class OrderStatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

    def __str__(self):
        return self.name


class Order:
    def __init__(self, order_id, status: OrderStatus = OrderStatus.PENDIENTE):
        self.order_id = order_id
        self.status = status

    def _get_id(self):
        return self.order_id

    def _get_status(self):
        return f"Orden {self._get_id()} {self.status}."

    def enviar(self):
        if self.status == OrderStatus.ENTREGADO or self.status == OrderStatus.CANCELADO:
            print(f"No se puede enviar una orden de estado {self.status}")
            return

        self.status = OrderStatus.ENVIADO
        print(self._get_status())

    def entregar(self):
        if self.status != OrderStatus.ENVIADO:
            print(f"La orden {self._get_id()} debe ser enviada antes de ser ENTREGADA")
            return

        self.status = OrderStatus.ENTREGADO
        print(f"Orden {self._get_id()} ENTREGADA.")

    def cancelar(self):
        if self.status == OrderStatus.ENTREGADO:
            print(f"No se puede cancelar una orden: {self.status}")
            return

        self.status = OrderStatus.CANCELADO
        print(f"Orden {self._get_id()} cancelada.")

    def mostrar_estado(self):
        return print(f"ESTADO: {self._get_status()}")


# EJEMPLOS USO
orden1 = Order("A123")
orden1.mostrar_estado()
orden1.enviar()
orden1.mostrar_estado()
orden1.entregar()
orden1.mostrar_estado()

orden2 = Order("B456")
orden2.cancelar()
orden2.mostrar_estado()

orden3 = Order("C789")
orden3.entregar()  # Intenta entregar sin enviar
orden3.mostrar_estado()
orden3.enviar()
orden3.cancelar()  # Intenta cancelar después de enviar
orden3.mostrar_estado()
orden3.entregar()
orden3.mostrar_estado()
