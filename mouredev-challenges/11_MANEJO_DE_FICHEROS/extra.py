'''11 MANEJO DE FICHEROS'''

def sales_manager():
    filename = "mis_ventas.txt"

    # Opciones del menu
    menu_options = {
        "1": add_product,
        "2": get_products,
        "3": update_product,
        "4": delete_product,
        "5": get_sell,
        "6": "6",
    }

    # Interfaz via terminal
    while True:
        print("Ingresa el numero para realizar la operación")
        print("1 - Añadir")
        print("2 - Consultar")
        print("3 - Actualizar")
        print("4 - Eliminar")
        print("5 - Calcular Venta Total")
        print("6 - Salir")

        option = get_input("Selecciona una opción:")
        action = menu_options.get(option)

        if action:
            if option < "6":
                action(filename)
            else:
                # os.remove(filename)
                break
        else:
            print("Escoge una opción del 1 al 6")


def add_product(filename):
    name = get_input("Nombre del producto: ")
    quantity = get_input("Cantidad vendida: ")
    price = get_input("Precio: ")

    write_file(filename, "a", f"{name}, {quantity}, {price}\n")


def get_products(filename):
    product_name = get_input("Ingresa el producto a consultar:")

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, quantity, price = split_line(line)

            if name == product_name:
                print(f"Producto:   {name}")
                print(f"Cantidad:   {quantity}")
                print(f"Precio:     {price}")
                return
    print("No existe el producto")


def delete_product(filename):
    product_name = input("Que deseas eliminar:").upper()
    new_products = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, _, _ = split_line(line)

            if name != product_name:
                new_products.append(line)

    write_file(filename, "w", new_products)


def update_product(filename):
    product_name = get_input("Ingresa el producto a actualizar:")
    new_products = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, quantity, price = split_line(line)
            if name == product_name:
                new_products.append(get_input_update([name, quantity, price]))
            else:
                new_products.append(line)

    write_file(filename, "w", new_products)


def get_input_update(product):
    print("Que deseas actualizar:")
    print("1. Nombre")
    print("2. Cantidad")
    print("3. Precio")

    option = input("Selecciona una opción: ")

    match option:
        case "1":
            new_name = get_input("Nuevo nombre: ")
            return f"{new_name}, {product[1]}, {product[2]}\n"
        case "2":
            new_quantity = get_input("Nueva cantidad: ")
            return f"{product[0]}, {new_quantity}, {product[2]}\n"
        case "3":
            new_price = get_input("Nuevo precio: ")
            return f"{product[0]}, {product[1]}, {new_price}\n"
        case _:
            print("Opción invalida")
            return f"{product[0]}, {product[1]}, {product[2]}\n"


def get_sell(filename):
    print("Hacer el calculo por producto o en total")
    print("1. Producto")
    print("2. Total")
    option = get_input("Selecciona una opción: ")

    match option:
        case "1":
            product = get_input("Producto a consultar: ")
            total_product = calculate_sell(filename)[1]
            if product in total_product:
                print(f"{product} hizo un total de: {total_product[product]}")
            else:
                print("Producto no encontrado")
        case "2":
            total = calculate_sell(filename)[0]
            print(f"El total es de: {total}")


def calculate_sell(filename):
    total = 0
    total_product = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, quantity, price = split_line(line)
            profit = float(quantity) * float(price)
            total += profit

            total_product[name] = total_product.get(name, 0) + profit

    return [total, total_product]


def write_file(filename: str, mode: str, lines):
    with open(filename, mode, encoding="utf-8") as file:
        if isinstance(lines, list):
            file.writelines(lines)
        else:
            file.write(lines)


def split_line(line):
    return line.strip().split(", ")


def get_input(prompt=""):
    return input(prompt).upper()


sales_manager()
