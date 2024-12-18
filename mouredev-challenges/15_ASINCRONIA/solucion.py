"""Mi solución para el ejercicio sobre Asincronía"""

import asyncio
from datetime import datetime


# Ejercicio
async def my_async_function(name, wait_time):
    print(f"La función {name} empieza: {obtener_hora_minuto()}")
    await asyncio.sleep(wait_time)
    print(f"La función {name} termina: {obtener_hora_minuto()}")


def obtener_hora_minuto():
    return datetime.now().strftime("%M:%S")


# asyncio.run(my_async_function("Gato", 3))

# Dificultar extra:
# Utilizando el concepto de asincronía y la función anterior, crea
# el siguiente programa que ejecuta en este orden:
# - Una función C que dura 3 segundos.
# - Una función B que dura 2 segundos.
# - Una función A que dura 1 segundo.
# - Una función D que dura 1 segundo.
# - Las funciones C, B y A se ejecutan en paralelo.
# - La función D comienza su ejecución cuando las 3 anteriores han finalizado.


async def main():
    await asyncio.gather(
        my_async_function("C", 3), my_async_function("B", 2), my_async_function("A", 1)
    )
    await my_async_function("D", 1)


asyncio.run(main())
