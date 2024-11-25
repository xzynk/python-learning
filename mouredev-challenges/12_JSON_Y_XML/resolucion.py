import json
import xml.etree.ElementTree as ET

data = {
    "name": "Raul",
    "age": 30,
    "birthday": "04/15/2015",
    "languages": ["Python", "Java", "C++"],
}


def create_json(content):
    """Crea un archivo JSON"""

    # Convertimos el diccionario a string JSON
    json_string = json.dumps(content, indent=4, ensure_ascii=False)
    # Guardar el diccionario como JSON en un archivo
    with open("Personas.json", "w", encoding="utf-8") as file:
        file.write(json_string)


def create_xml(content):
    """Crea un archivo XML"""

    # Convertimos la data a XML
    root = ET.Element("User")

    for key, value in content.items():
        if isinstance(value, list):
            item_list = ET.SubElement(root, key)
            for item in value:
                ET.SubElement(item_list, "item").text = str(item)
        else:
            ET.SubElement(root, key).text = str(value)

    # Escribimos el XML
    tree = ET.ElementTree(root)
    tree.write("Personas.xml", encoding="utf-8", xml_declaration=True)


# Creamos los archivos JSON Y XML
create_json(data)
create_xml(data)


# Leemos el XML

# xml_tree = ET.parse("Personas.xml")
# root = xml_tree.getroot()

# print(root.find("name").text)
# print(root.find("age").text)
# find_languages = root.find("languages")

# for item in find_languages.findall("item"):
#     print(item.text)

# También podemos cargar el archivo directamente
# with open("Personas.xml", "r", encoding="utf-8") as file:
#     print(file.read())

# Leemos el archivo Json

# with open("Personas.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#     print(data)  # Imprimimos el diccionario
#     print(data.get("name"))  # También podemos imprimir cada dato


# DIFICULTAD EXTRA (opcional):
# Utilizando la lógica de creación de los archivos anteriores, crea un
# programa capaz de leer y transformar en una misma clase custom de tu
# lenguaje los datos almacenados en el XML y el JSON.
# Borra los archivos.


class Data:
    def __init__(self, name, age, birthday, languages):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.languages = languages


def load_xml(xml_file):
    xml_loaded = ET.parse(xml_file)
    root = xml_loaded.getroot()

    name = root.find("name").text

    age = root.find("age").text
    birthday = root.find("birthday").text
    find_languages = root.find("languages")
    languages = []

    for item in find_languages.findall("item"):
        languages.append(item.text)

    data_from_xml = Data(name, age, birthday, languages)

    print(data_from_xml.__dict__)


def load_json(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    data_from_json = Data(
        data["name"], data["age"], data["birthday"], data["languages"]
    )
    print(data_from_json.__dict__)


load_xml("Personas.xml")
load_json("Personas.json")
