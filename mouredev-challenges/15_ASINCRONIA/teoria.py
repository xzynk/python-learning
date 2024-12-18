"""Practica de teoría sobre asincronia"""

# La asincronia permite ejecutar tareas concurrentemente es decir que
# puede ocurrir al simultaneamente pero no necesariamente de forma paralela

# Modulos pricipales
# asyncio
# concurrent.futures

import asyncio
import time


# Couroutines
async def saludar():
    print("Hello!")
    await asyncio.sleep(1)  # Simulamos una espera
    print("Adios!")


# Tareas concurrentes
async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"Tarea {name}, completada en {delay} segundos")


async def main_tasks():
    await asyncio.gather(  # Ejecuta multiples couroutines concurrentemente.
        task("A", 2),
        task("B", 1),
        task("C", 3),
    )


# Sincronizacion en Asincronia
# Semaforos asyncio.Semaphore
# Limita el numero de tareas concurrentes


async def limited_task(semaphore):
    async with semaphore:
        print("Empezamos la tarea... GO")
        await asyncio.sleep(1)
        print("Terminamos la tarea...ufff")


async def ejecutar_semaforos():
    semaphore = asyncio.Semaphore(2)  # Maxima 2 tareas concurrentes
    await asyncio.gather(*(limited_task(semaphore) for _ in range(5)))


# Locks asyncio.Lock
# Garantiza que solo una tarea acceda a un recurso compartido

lock = asyncio.Lock()


async def access_database(user):
    print(f"{user} intentando acceder a la base de datos...")
    async with lock:  # Espera hasta que el Lock esté disponible
        print(f"{user} accediendo a la base de datos...")
        await asyncio.sleep(2)  # Simula el tiempo de acceso
        print(f"{user} terminó de usar la base de datos.")


async def ejecutar_locks():
    await asyncio.gather(
        access_database("Usuario 1"),
        access_database("Usuario 2"),
        access_database("Usuario 3"),
    )


# Manejo de excepciones
# Usamos blosques try-except para capturar errores en tareas asincronicas


async def faulty_task():
    raise ValueError("Ocurrio un error!")


# Integracion con funciones sincronicas
def blocking_function():
    time.sleep(2)
    return "Finalizada la función sincrona"


async def sincronicas():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, blocking_function)
    print(result)


# Punto de entrada principal
async def main():
    # Ejecuta cada sección secuencialmente
    await saludar()  # Corutina simple
    await main_tasks()  # Tareas concurrentes
    await ejecutar_semaforos()  # Uso de semáforos
    await ejecutar_locks()  # Uso de Locks
    try:
        await faulty_task()
    except ValueError as e:
        print(f"Tenemos un error: {e}")
    await sincronicas()


# Ejecuta el programa
if __name__ == "__main__":
    asyncio.run(main())
