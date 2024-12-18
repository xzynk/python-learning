"""Solucion para ejercicio sobre EXPRESIONES REGULARES"""

import re

# Utilizando tu lenguaje, explora el concepto de expresiones regulares,
# creando una que sea capaz de encontrar y extraer todos los números de un texto.

STRNUMBERS = "Texto con números, 520123, más números 112344"
justNumbers = re.findall(r"\d+", STRNUMBERS)
print(justNumbers)


# Crea 3 expresiones regulares (a tu criterio) capaces de:
# Creo un función que validara segun un patron
def validator(check, pattern, label="Value"):
    for value in check:
        try:
            find = re.fullmatch(pattern, value)
            print(f"{label}: {find.group()} is VALID")
        except AttributeError:
            print(f"{label}: {value} is not valid")


# - Validar un email.
print("Validating emails")
emails = ("anthony@gatos.com", "gatos.net@", "email.valido@gmail.com", "·!#@gmail.com")
patternEmail = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
validator(emails, patternEmail, label="Email")

# - Validar un número de teléfono.
print("\nValidating phone numbers")
phoneNumbers = (
    "981239812",
    "978-123-455",
    "91241a231",
    "987 736 123",
    "987277166",
    "912--345--678",
)
patternPhoneNumbers = re.compile(r"^9\d{2}[-\s]?\d{3}[-\s]?\d{3}$")
validator(phoneNumbers, patternPhoneNumbers, label="Phone Number")

# - Validar una url.
print("\nValidating phone numbers")
urls = (
    "http://www.google.com",
    "https://www.a.com",
    "google.com",
    "http://www..google..com",
    "https://www.yahoo.com",
    "google.com",
)
patternUrls = re.compile(r"^(https?://)?(www\.)?\w+(\.\w+)+$")
validator(urls, patternUrls, label="URL")
