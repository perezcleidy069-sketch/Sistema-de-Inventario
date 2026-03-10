from inventory import productos

def ask_option():

    opc=int(input("Ingrese la opcion deseada: "))
    return opc


def separator():

    print("***********************************")

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
        if i ['nombre'].lower()== nombre_producto.lower():
            return True
    return False

def add_product():
    nombre=input("Ingrese el nombre del producto: ")
    if verificar_existencia(productos, nombre):
        print("Producto ya existe")
            
    else: 
        cantidad= int(input("Ingrese la cantidad del producto: "))
        precio=int(input("Ingrese el precio del producto: "))
        producto= {
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio
            }
        productos.append(producto)
        


def show_product():
    for producto in productos:
        print("nombre: "+producto["nombre"]+ "| precio: "+str(producto["precio"])+ "| cantidad: "+ str(producto["cantidad"]))

def obtner_indice(productos, nombre_producto):
    cantidad=len(productos)
    for i in range(0, cantidad):
        nombre=productos[i] ["nombre"]
        if nombre.lower()== nombre_producto.lower():
            return i
        return -1
    
def update_product():
    nombre=input ("Ingrese el nombre del producto a actualizar: ")
    if verificar_existencia(productos, nombre):
        opcion = int(input("1. Para agregar cantidades\n 2. Para quitar cantidad\n Ingrese su opción: "))
        if opcion == 1 or opcion == 2:
            indice= obtner_indice(productos, nombre)
            nueva_cantidad=int(input("INgrese la cantidad: "))
            if opcion == 1 and nueva_cantidad > 0:
                productos[indice]["cantidad"]+=nueva_cantidad
                productos.append()
            elif opcion==2 and nueva_cantidad> 0:
                productos[indice]["cantidad"]-=nueva_cantidad
            else:
                print("La cantidad debe ser positiva")
        else:
            print("Opción no valida")
    else:
        print("Producto no existe")

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
    