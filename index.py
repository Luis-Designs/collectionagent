# Titulo: Mini Cobrador
# Proposito: Vender y Almacenar productos!
# Autor: Luis Designs
# Fecha: Hoy

import functions as f

# Inicio
name = "Bad Boys 🦝"
f.marco(name)

f.chargeData()  # Cargamos los datos del archivo products.json

while(True):
    print("\n")
    f.menu()                # Nos imprime el primer menu
    opt = input("\nChoose one option: ")
    if(opt == "1"):
        # Listamos todos los productos
        print("\n", f.getProducts())
    if(opt == "2"):
        name, stock, price = f.inputFiles()
        print(f.createProduct(name, stock, price))
    if(opt == "3"):
        print("\n", f.getProducts())
        id = int(input("\n Ingrese el id del producto a actualizar: "))
        control, _ = f.searchProduct(id, "data")
        if(control):
            name, stock, price = f.inputFiles()
            print(f.updateProduct(id, name, stock, price))
        else:
            print("id incorrecto :C \n")
    if(opt == "4"):
        print("\n", f.getProducts())
        id = int(input("\n Ingrese el id del producto a eliminar: "))
        control, _ = f.searchProduct(id, "data")
        if(control):
            confirm = input("\n Are you sure? Yes(y) or No(n): ")
            if(confirm == "Yes" or confirm == "y"):
                print("\n", f.deleteProduct(id))
        else:
            print("id incorrecto :C \n")
    if(opt == "5"):
        flag = True
        while(flag):
            f.menuTwo()
            opt = input("\nChoose one option: ")
            if(opt == "1"):
                print("\n", f.getProducts())
            if(opt == "2"):
                print("\n", f.getProducts())
                id = int(input("\n Ingrese el id del producto a vender: "))
                control, _ = f.searchProduct(id, "data")
                if(control):
                    quantity = int(
                        input("\n Ingrese la cantidad del producto a vender: "))
                    print("\n", f.addProduct(id, quantity))
                else:
                    print("\nid incorrecto :C \n")

            if(opt == "3"):
                _, res = f.getProductsAdded()
                print("\n", res)
            if(opt == "4"):
                control, res = f.getProductsAdded()
                if(control):
                    print("\n", res)
                    id = int(input("\n Ingrese el id del producto a retirar: "))
                    print("\n", f.deleteProductAdded(id))
                else:
                    print("\n", res)
            if(opt == "5"):
                control, res = f.charge()
                if(not control):
                    print("\n", res)
                else:
                    print(f"\n{name}. ", res)
                    confirm = input(
                        "\nDo you want to see the detail? Yes(y) or No(n): ")
                    if(confirm == "Yes" or confirm == "y"):
                        f.printDetail()
                flag = False  # Nos permite cerrar este bucle
            if(opt == "r" or opt == "return()"):
                flag = False  # Nos permite cerrar este bucle
    if(opt == "q" or opt == "quit()"):
        quit()  # Nos permite cerrar el programa
