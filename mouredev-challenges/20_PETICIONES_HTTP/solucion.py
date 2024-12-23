"""EJERCICIO PETICIONES HTTP"""

# Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza una petición a la web que tú quieras,
# verifica que dicha petición fue exitosa y muestra por consola el contenido de la web.

import requests

# Url Base y parámetros
url = "https://meowfacts.herokuapp.com/"
params = {"count": 5, "lang": "esp"}
cat_facts = None

try:
    # Realiza la petición GET
    response = requests.get(url, params, timeout=5)
    response.raise_for_status()  # Lanza un error si el código no es 2XX

    # Procesa la respuesta como JSON
    data = response.json()
    print("Conexión exitosa")

    # Nos aseguramos que la clave "data" exista en la respuesta
    if "data" in data:
        cat_facts = data["data"]
    else:
        print("La clave 'data' no se encontró en la respuesta.")
except requests.exceptions.RequestException as e:
    print(f"Error al realizar la petición: {e}")

# Iterar sobre los resultados si existen
if cat_facts:
    for fact in cat_facts:
        print(fact)
else:
    print("No se pudieron recuperar los datos de la API.")
