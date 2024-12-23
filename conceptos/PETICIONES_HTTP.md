# PETICIONES HTTP

Las peticiones HTTP en Python nos ayudan a interactuar con APIs, servidores web y servicios en línea. Python ofrece
varias bibliotecas para realizar esas peticiones, siendo `requests` la más popular debido a su simplicidad y
facilidad de uso.

---

### CONCEPTOS BÁSICOS

1. **Protocolo HTTP:** Es el protocolo principal para la comunicación en la web. Las peticiones HTTP tienen métodos
   principales como:
    - **GET**: Recupera información.
    - **POST**: Enviar datos al servidor.
    - **PUT**: Actualizar recursos.
    - **DELETE**: Eliminar recursos.
2. **Componentes de una petición HTTP:**
    - **URL**: Dirección del recurso.
    - **Headers**: Información adicional como tokens, tipo de contenido, etc.
    - **Body**: Datos enviados en el caso de POST/PUT

---

### LIBRERÍAS PRINCIPALES EN PYTHON

1. `requests`
   Es una biblioteca de terceros que facilita las peticiones HTTP.
   **Instalación:**

```bash
pip install requests
```

```python
import requests

# GET Request
response = requests.get("https://api.example.com/data")
print(response.status.code)  # Código de estado
print(response.json())  # Respuesta en formato JSON

# POST Request
payload = {"key": "value"}
response = requests.post("https://api.example.com/data", json=payload)
print(response.text)  # Respuesta como texto
```

**Características principales:**

- Fácil manejo de headers:

```python
headers = {"Authorization": "Bearer token123"}
response = requests.get("https://api.example.com/secure", headers=headers)
```

- Manejo de errores:

```python
try:
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()  # Lanza un error si el código no es 2xx
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

- Subida de archivos:

```python
files = {"file": open("example.txt", "rb")}
response = requests.post("https://api.example.com/upload", files=files)
```

---

2. `http.client`
   Es parte de la biblioteca standard de Python. Más bajo nivel y más control.
   **Ejemplo:**

```python
import http.client

conn = http.client.HTTPSConnection("api.example.com")
conn.request("GET", "/data")
response = conn.getresponse()
print(response.status, response.reason)
print(response.read().decode())
```

---

3. `urllib`
   También parte de la biblioteca standard. Más flexible, pero algo verbosa.
   **Ejemplo:**

```python
import urllib.request
import json

url = "https://api.example.com/data"
with urllib.request.urlopen(url) as response:
    data = json.load(response)
    print(data)
```

---

4. `aiohttp` (para peticiones asíncronas)
   Ideas para manejar multiples peticiones de manera concurrente

```bash
pip install aiohttp
```

```python
import aiohttp
import asyncio


async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.example.com/data") as response:
            print(await response.json())


asyncio.run(fetch_data())
```

---

### Aspectos importantes

1. Manejo de respuestas
    - `response.status_code`: Código HTTP (200,404,500,etc)
    - `response.text`: Respuesta en texto plano
    - `response.json()`: Respuesta parseada como JSON (si es aplicable)
2. Headers comunes:

```python
headers = {
    "Content-Type": "application/json",  # Tipo de contenido
    "Authorization": "Bearer token123"  # Token de autenticación
}
```

3. Parámetros en URL:

```python
params = {"q": "search term", "page": 1}
response = requests.get("https://api.example.com/search", params=params)
```

4. Autenticación:

```python
from requests.auth import HTTPBasicAuth

response = requests.get("https://api.example.com/auth", auth=HTTPBasicAuth("user", "pass"))
```

5. Time-outs y retires:

```python
response = requests.get("https://api.example.com/data", timeout=5)  # Timeout en segundos
```

6. Manejo de cookies:

```python
session = requests.Session()
session.cookies.set("name", "value")
response = session.get("https://api.example.com/cookies")
```

---

## Algunos consejos

- **Uso de una sesión para multiples peticiones:** Reduce la sobrecarga de abrir y cerrar conexiones repetidamente.

```python
session = requests.Session()
session.headers.update({"Authorization": "Bearer token123"})
response = session.get("https://api.example.com/data")
```

- **Manejo de Proxies:**

```python
proxies = {"http": "http://proxy.example.com:8080", "https": "https://proxy.example.com:8080"}
response = requests.get("https://api.example.com/data", proxies=proxies)
```

- **Seguridad:**
    - Nunca expongas tokens o credenciales en tu código.
    - Usa HTTPS siempre que sea posible
    - Valída los certificados SSL:

```python
response = requests.get("https://api.example.com/data", verify=True)
```

- **Depuración:** Habilita el registro para rastrear problemas:

```python
import logging
import http.client as http_client

http_client.HTTPConnection.debuglevel = 1
logging.basicConfig(level=logging.DEBUG)
```