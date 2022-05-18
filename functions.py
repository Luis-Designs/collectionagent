import json
data = []   # Almacena el json
buy = []    # Almacena la compra
id = 0      # Hara como nuestro identificador del producto
toPay = 0   # Agregamos a la cuenta


def chargeData():
    global data, id
    with open('products.json', encoding="utf-8") as file:
        data = json.load(file)
        id = max(data[i]["id"] for i in range(len(data)))


def getProducts():
    # Sirve para leer los datos del archivo
    return json.dumps(data, indent=4, ensure_ascii=False)


def createProduct(name, stock, price):
    # Crea un nuevo producto
    global id
    id += 1                 # Funciona como un identificador
    data.append(
        {
            'id': id,
            'name': name,
            'stock': stock,
            'price': price
        }
    )
    with open('products.json', 'w') as file:
        json.dump(data, file, indent=4)
    # print(id)
    return data[-1]        # se imprime el último elemento agregado


def searchProduct(id, clave):
    res = []                # Es la respuesta que retorna si existe o no
    if (clave == "data"):
        for i in range(len(data)):
            # print(data[i]['id'] if data[i]["id"] == id else "")
            if(data[i]["id"] == id):
                res = [True, i]     # El producto existe y regresa la posición
                break
            res = [False, ""]       # El producto no existe
    if (len(buy) >= 1 and clave == "buy"):
        for i in range(len(buy)):
            # print(data[i]['name'])
            if(buy[i]["id"] == id):
                res = [True, i]     # El producto existe y regresa la posición
                break
            res = [False, ""]       # El producto no existe
    if(len(buy) == 0 and clave == "buy"):
        res = [False, ""]       # El producto no existe

    return res


def updateProduct(id, name, stock, price):
    # Actualiza el producto dado un id, name, stock, price
    flag, pos = searchProduct(id, "data")
    if(flag):
        data[pos]['name'] = name                    # actualizamos el nombre
        data[pos]['stock'] = stock                  # actualizamos el stock
        data[pos]['price'] = price                  # actualizamos el precio
        with open('products.json', 'w') as file:
            json.dump(data, file, indent=4)
    return "Producto no encontrado :(" if(not flag) else "Producto actualizado :D"


def deleteProduct(id):
    # Elimina un producto del archivo products.json

    # Deestructuramos la lista devuelva
    flag, pos = searchProduct(id, "data")
    if(flag):
        del data[pos]                   # Eliminamos el producto
        with open('products.json', 'w') as file:
            json.dump(data, file, indent=4)

    return "Producto no encontrado :(" if(not flag) else "Producto eliminado :D"


def getProductsAdded():
    # Sirve para leer los datos del carrito
    if(len(buy) >= 1):
        # Para controlar el fallo
        return [True, json.dumps(buy, indent=4, ensure_ascii=False)]
    return [False, "Aún no a agregado ningún producto :("]


def addProduct(id, quantity):
    # Agrega un producto a la lista buy[]

    # Deestructuramos la lista devuelva
    flag, pos = searchProduct(id, "data")

    if(flag):
        if(data[pos]['stock'] - quantity >= 0):
            buy.append(
                {
                    'id': id,
                    'name': data[pos]['name'],
                    'quantity': quantity,
                    'price': data[pos]['price']
                }
            )   # Agregamos al carrito
        else:
            return "Stock insuficiente :("     # Enviamos un sms de error

    return "Producto no encontrado :(" if(not flag) else "Producto agregado :D"


def deleteProductAdded(id):
    # Deestructuramos la lista devuelva
    flag, pos = searchProduct(id, "buy")

    if(flag):
        del buy[pos]         # Agregamos al carrito
    return "Producto no encontrado :(" if(not flag) else "Producto eliminado de la compra :D"


def charge():
    global toPay
    for i in range(len(buy)):
        # Desestructuramos el diccionario
        id, name, quantity, price = buy[i].values()
        toPay += quantity * price  # Agregamos a la cuenta
        # Desestructuramos la lista devuelva
        _, pos = searchProduct(id, "data")
        # Actualizamos el stock del producto
        updateProduct(id, name, data[pos]['stock'] - quantity, price)

    if len(buy) >= 1:
        return True, "Agredece su compra! Su total neto a pagar es: S/. {:.2f} :D".format(toPay)
    else:
        return False, "Aún no ha vendido nada :("


def printDetail():
    global toPay
    print("\n Detalle de compra:\n")
    print("\t{:<45}{}\t{:^10}{:>11}\n".format(
        "Productos", "Unidades", "Precio", "Total"))
    for i in range(len(buy)):
        _, name, quantity, price = buy[i].values()
        dot = " " * (40 - len(name))
        gion = "-" * 77
        print("\t{} {}>\t{}\t {:^8.2f}{:>12.2f}  ".format(
            name, dot, quantity, price, quantity*price))
    print("\t{}".format(gion))
    print("\t{:<67}{:>10.2f}".format("Total", toPay))


def marco(name):
    marco = "*" * 100   # Repite el * cien veces, para el marco
    text = f"Welcome to {name}, tenemos todo lo que necesitas!! 🦝"
    # Se imprime el marco e incluye el nombre ingresado
    print("\n" + marco)
    print("*{:^96}*".format(text))
    print(marco)


def menu():
    cleanBuy()  # Limpiamos la cuenta
    print("1. Listar Productos")
    print("2. Agregar un producto")
    print("3. Actualizar un producto")
    print("4. Remover un producto")
    print("5. Vender")
    print("Escriba q o quit() para salir")


def menuTwo():
    print("\n1. Listar productos")
    print("2. Agregar producto al carrito")
    print("3. Listar productos agregados al carrito")
    print("4. Remover producto agregado al carrito")
    print("5. Cobrar")
    print("Escriba r o return() para regresar a home")


def inputFiles():
    name = input("\nIntroduce name of product: ")
    stock = int(input("Introduce stock of product: "))
    price = round(float(input("Introduce price of product: ")), 2)
    print("\n")
    return [name, stock, price]


def cleanBuy():
    global buy, toPay
    buy = []    # Limpia la compra
    toPay = 0    # Limpia la cuenta
