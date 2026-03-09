def ask_option():

    opc=int(input("Ingrese la opcion deseada: "))
    return opc


def separator():

    print("* * 20")

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


def add_product():
    pass

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