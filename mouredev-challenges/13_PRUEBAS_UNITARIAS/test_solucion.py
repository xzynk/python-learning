keys = ["nombre", "apellido", "edad", "birth_date", "programming_languages"]
diccionario_completo = {
    "nombre": "Anthony",
    "apellido": "Sotomayor",
    "edad": 35,
    "birth_date": "04-09-1989",
    "programming_languages": ["Python", "JavaScript"],
}
diccionario_incompleto = {
    "nombre": "Anthony",
    "apellido": "Sotomayor",
    "birth_date": "04-09-1989",
    "programming_languages": "Python, JavaScript",
}
diccionario_no_lista = {
    "nombre": "Anthony",
    "apellido": "Sotomayor",
    "edad": 35,
    "birth_date": "04-09-1989",
    "programming_languages": "Python, JavaScript",
}
diccionario_valor_vacio = {
    "nombre": "",
    "apellido": "Sotomayor",
    "edad": 35,
    "birth_date": "04-09-1989",
    "programming_languages": "Python, JavaScript",
}


# Función que verifica si un diccionario tiene las claves requeridas
def verify_keys(diccionario, claves_requeridas):
    return all(clave in diccionario for clave in claves_requeridas)


def verify_data(diccionario):
    claves_requeridas = [
        "nombre",
        "apellido",
        "edad",
        "birth_date",
        "programming_languages",
    ]

    if not all(clave in diccionario for clave in claves_requeridas):
        return False

    if not all(diccionario[clave] for clave in claves_requeridas if clave != "edad"):
        return False

    if not isinstance(diccionario["programming_languages"], list):
        return False

    if not isinstance(diccionario["edad"], int):
        return False

    return True


def test_diccionario():
    assert verify_data(diccionario_completo)


def test_diccionario_incompleto():
    assert verify_data(diccionario_incompleto)


def test_valor_vacio():
    assert verify_data(diccionario_valor_vacio)


def test_diccionario_vacio():
    assert verify_data({})
