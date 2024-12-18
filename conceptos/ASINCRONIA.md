# Asincronia

La asincronia nos permite ejecutar tareas concurrentemente, lo que es util en programa que realizan multiples
operaciones que podrian esperar por recursos externos, como llamadas a bases de datos, APIs o lectura de archivos.

## 1. Modulos Principales para Asincronia

`asyncio`

- Es el modulo principal de Python para manejar programación asincronica.
- Introduce el concepto de **couroutines**, eventos, bucles de eventos y tareas.

`concurrent.futures`

- Se utiliza para ejecutar tareas en subprocesos o procesos separados.
- Compatible con programación concurrente basada en hilos o multiprocesos.

**Librerias externas**

- `aiohttp`: Para realizar peticiones HTTP asincronicas.
- `trio` y `curio`: Librerias avanzadas para programación asincronica.

## 2. Conceptos clave

#### Coroutines

- Funciones definidas con `async def`. Representan tareas asincronicas
- Se ejecutan usando `await`.

```Python
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)  # Simula una tarea de espera
    print("Goodbye!")
```

## 3. Funciones y Estructuras Asincronicas

#### Crear Coroutines

```python
async def main():
    print("Start")
    await asyncio.sleep(2)  # Simula una operación asincrónica
    print("End")

# Ejecutar la coroutine
asyncio.run(main())

```

#### Correr Tareas Concurrentes

```python
async def task(name, delay):
	await asyncio.sleep(delay)
	print(f"Task {name} completed after {delay} seconds")

async def main():
	await asyncio.gather(
		task("A", 2),
		task("B", 1),
		task("C", 3)
	)

asyncio.run(main())
```

**Salida**

```python
Task B completed after 1 seconds
Task A completed after 2 seconds
Task C completed after 3 seconds
```

**Crear y ejecutar Tareas**

- `asyncio.create_task()`: Inicia una tarea asincronica.
- `asyncio.gather()`: Ejecuta multiples *coroutines* concurrentemente.
- `asyncio.run()`: Inicia el bucle de eventos y ejecuta la *coroutine* principal.

## 4. Sincronizacion en Asincronia

#### Semaforos (`asyncio.Semaphore`)

- Limita el numero de tareas concurrentes

```python
async def limited_task(semaphore):
	async with semaphore:
		print("Task started")
		await asyncio.sleep(2)
		print("Task finished")

async def main():
	semaphore = asyncio.Semaphore(2) #Maximo 2 tareas concurrentes
	await asyncio.gather(*(limited_task(semaphore) for _ in range(5)))

asyncio.run(main())
```

#### Locks (`asyncio.Lock`)

- Garantiza que solo una tarea acceda a un recurso compartido.

```python
lock = asyncio.Lock()

async def critical_section():
	async with lock:
	print("Resource in use")
	await asyncio.sleep(1)
```

## 5. Manejo de Excepciones en Asincronia

Usa bloques `try-except` para capturar errores en tareas asincronicas.

```python
async def faulty_task():
	raise ValueError("An error ocurred!")

async def main():
	try:
		await faulty_task()
	except ValueError as e:
		print(f"Caught an exception: {e}")

asyncio.run(main())
```

## 6. Integracion con Funciones Sincronicas

**Ejecutar funciones sincronicas en un hilo separado**

```python
import asyncio
import time

def blocking_function():
	time.sleep(2)
	return "Finished blocking task"

async def main():
	loop = asyncio.get_running_loop()
	result = await loop.run_in_executor(None, blocking_function)
	print(result)

asyncio.run(main())
```

## 7. Buenas Practicas

- **Evitar Bloqueos:** Usa `await` para llamadas que podrian ser bloqueantes
- **Limita las Tareas Concurrentes:** Usar semaforos puede prevenir la saturacion de recursos.
- **Manejo de errores:** Siempre maneja excepciones en tareas asincronicas.

## 8. Herramientas Externas para Asincronia

- `aiohttp`: Para realizar peticiones HTTP asincronicas.

```python
import aiohttp
import asyncio

async def fetch_url(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			return await response.text() 
			
asyncio.run(fetch_url("https://example.com"))
```

## 9. Comparacion entre Concurrencias y Paralelismo

- **Concurrencia:** Ejecuta multiples tareas en un solo hilo utilizando un bucle de eventos.
- **Paralelismo:** Ejecuta multiples tareas en paralelo utilizando varios nucles de CPU o procesos.

## 10. Ejemplo Completo

```python
import asyncio
import random

async def download_file(file_id):
    print(f"Starting download {file_id}")
    await asyncio.sleep(random.randint(1, 3))  # Simula descarga
    print(f"Finished download {file_id}")

async def main():
    files = [download_file(i) for i in range(5)]
    await asyncio.gather(*files)

asyncio.run(main())
```

**Salida:**

```
Starting download 0
Starting download 1
Starting download 2
Starting download 3
Starting download 4
Finished download 1
Finished download 0
Finished download 2
Finished download 3
Finished download 4
```