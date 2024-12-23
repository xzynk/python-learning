"""EJERCICIO EXTRA"""

import re
from collections import OrderedDict

import requests
import requests.exceptions
from colorama import Fore

# Utilizando la PokéAPI (https://pokeapi.co), crea un programa por terminal al que le puedas solicitar información
# de un Pokémon concreto utilizando su nombre o número.
#
# - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
# - Muestra el nombre de su cadena de evoluciones
# - Muestra los juegos en los que aparece
# - Controla posibles errores

BASE_POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"
DEFAULT_TIMEOUT = 5

RE_NUMBERS = re.compile(r"\d+")
RE_LETTERS = re.compile(r"[a-zA-Z]+")

cache = OrderedDict()
CACHE_LIMIT = 50

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
LIGHTBLUE_EX = Fore.LIGHTBLUE_EX
LIGHTRED_EX = Fore.LIGHTRED_EX
LIGHTMAGENTA_EX = Fore.LIGHTMAGENTA_EX
RESET = Fore.RESET


def get_from_api(url, timeout=DEFAULT_TIMEOUT):
    """Función que hace llamado a una API pasándole un URL"""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print(f"Tiempo de espera agotado al acceder a {url}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"Error de conexión al acceder a {url}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP al acceder a {url}: {e.response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a {url},\n: {e}")
        return None


def get_pokemon_data(pokemon):
    print("Consultando...")
    url = f"{BASE_POKEAPI_URL}{pokemon.lower()}"

    pokemon_data = get_from_api(url)
    if not pokemon_data:
        return None, None

    species_data = get_from_api(pokemon_data["species"]["url"])
    if not species_data:
        return None, None

    evolution_chain_data = get_from_api(species_data["evolution_chain"]["url"])
    if not evolution_chain_data:
        return None, None

    return pokemon_data, evolution_chain_data


def get_abilities(data):
    return [ability["ability"]["name"] for ability in data["abilities"]]


def get_types(data):
    return [type_data["type"]["name"] for type_data in data["types"]]


def get_games(data):
    return [game["version"]["name"] for game in data["game_indices"]]


def get_evolutions(chain_data):
    evolutions = []

    def _find_evolutions(find_data):
        evolutions.append(find_data["species"]["name"])
        if find_data.get("evolves_to"):
            for evolution in find_data["evolves_to"]:
                get_evolutions(evolution)

    _find_evolutions(chain_data)
    return evolutions


def process_pokemon_data(data, data_evo):
    ability = get_abilities(data)
    types = get_types(data)
    game = get_games(data)
    evolutions = get_evolutions(data_evo["chain"])

    stats = "\n".join(
        f"{stat['stat']['name'].capitalize()} : {stat['base_stat']}"
        for stat in data["stats"]
    )

    pokemon_info = {
        "name": data["name"],
        "id": data["id"],
        "height": data["height"] / 10,
        "weight": data["weight"] / 10,
        "type": types,
        "stats": stats,
        "abilities": ability,
        "games": game,
        "evolutions": evolutions,
    }

    return pokemon_info


def add_to_cache(data):
    if data["name"] not in cache:
        if len(cache) > CACHE_LIMIT:
            cache.popitem(last=False)
        cache[data["name"]] = data
        cache[str(data["id"])] = cache[data["name"]]


def show_pokemon_data(pokemon):
    """Muestra información del pokemon"""
    print(
        f"{GREEN}Name: {pokemon['name'].capitalize()} (ID: {pokemon['id']})\n"
        f"------------------------------{YELLOW}\n"
        f"Height: {pokemon['height']}m\n"
        f"Weight: {pokemon['weight']}kg\n"
        f"Type: {', '.join(pokemon['type']).capitalize()}\n"
        f"Abilities: {', '.join(pokemon['abilities']).capitalize()}\n"
        f"{LIGHTBLUE_EX}------------------------------\n"
        f"Stats:\n"
        f"{pokemon['stats']}\n"
        f"{LIGHTRED_EX}------------------------------\n"
        "Evolutions Chain:\n"
        f"{', '.join(pokemon['evolutions'])}\n"
        f"{LIGHTMAGENTA_EX}------------------------------\n"
        f"Juegos:\n"
        f"{', '.join(pokemon['games'])}\n"
        f"{RESET}"
    )


def validate_input():
    while True:
        user_input = input("Ingresa solo un nombre (letras) o un ID (números): ")
        if re.fullmatch(RE_NUMBERS, user_input) or re.fullmatch(RE_LETTERS, user_input):
            result = user_input.lower()
            break

        print("Nombre inválido. Por favor, intenta de nuevo.")

    return result


def fetch_pokemon_data(name):
    if name in cache:
        return cache[name]
    poke, evo = get_pokemon_data(name)
    if poke and evo:
        data = process_pokemon_data(poke, evo)
        add_to_cache(data)
        return data
    print(f"No se encontró información para: {name}")
    return None


while True:
    valid_name = validate_input()
    poke_data = fetch_pokemon_data(valid_name)
    if poke_data:
        show_pokemon_data(poke_data)
