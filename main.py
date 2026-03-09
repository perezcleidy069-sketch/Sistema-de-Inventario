from inventory import*

def escribir_archivo(inventory):
    with open("inventory.py", "a") as archivo:
        archivo.write(inventory+"\n")

def ask_option():

    opc=int(input("Ingrese la opcion deseada: "))
    return opc


def separator():

    print("=*20")

def show_menu():
    separator()
    print("Bienvenido a la TIENDA LA LOLITA")
    separator()
    MENU=""""
    1. Agregar productos
    2. Mostrar productos
    3. Actualizar cantidad de un producto
    4. Eliminar productos
    5. Calcular inventario
    6. Salir"""
    print(MENU)
    separator()

def verificar_existencia(productos, nombre_producto):
    for i in productos:
        nombre= i["nombre"]
        if nombre.lower()== nombre_producto.lower():
            return True
    return False

def add_product():
    nombre=input("Ingrese el nombre del producto: ")
    if verificar_existencia(productos, nombre):
        print("Producto ya existe")
    else:
        cantidad= int(input("Ingrese la cantidad del producto: "))
        precio=float(input("Ingrese el precio del producto: "))
        producto= {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        productos.apped(producto)
        escribir_archivo()
        


def show_product():
    pass

def update_product():
    pass

def delete_product():
    pass

def calculate_inventary():
    pass

while True:
    show_menu()
    try:
        opc=ask_option()
    except Exception:
        print("Hubo un error con su opcion")
        
    if opc == 1:
        add_product()
    elif opc== 2:
        show_product()
    elif opc == 3:
        update_product()
    elif opc == 4:
        delete_product()
    elif opc== 5:
        calculate_inventary()
    elif opc== 6:
        print("Adios, fue un gusto para nosotros que usted nos prefiriera :)")
    else:
        print("Ingresó la opcion incorrecta")  
    break