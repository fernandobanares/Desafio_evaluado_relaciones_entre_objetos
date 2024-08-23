from tienda import Restaurante, Supermercado, Farmacia

def crear_tienda():
    print("Bienvenido al sistema de creación de tiendas.")
    tipo = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): ").strip().capitalize()
    nombre = input("Ingrese el nombre de la tienda: ").strip()
    costo_delivery = int(input("Ingrese el costo de delivery: "))

    if tipo == "Restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo == "Supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo == "Farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return None

def ingresar_productos(tienda):
    while True:
        nombre = input("Ingrese el nombre del producto (o 'salir' para finalizar): ").strip()
        if nombre.lower() == 'salir':
            break
        precio = int(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))

        tienda.ingresar_producto(nombre, precio, stock)
        print(f"Producto '{nombre}' agregado exitosamente.")

def listar_productos(tienda):
    print("\nLista de productos:")
    print(tienda.listar_productos())

def realizar_venta(tienda):
    nombre_producto = input("Ingrese el nombre del producto a vender: ").strip()
    cantidad = int(input("Ingrese la cantidad a vender: "))
    mensaje = tienda.realizar_venta(nombre_producto, cantidad)
    print(mensaje)

def menu_principal(tienda):
    while True:
        print("\nSeleccione una opción:")
        print("1. Listar productos")
        print("2. Realizar una venta")
        print("3. Salir")
        opcion = input("Ingrese su opción: ").strip()

        if opcion == "1":
            listar_productos(tienda)
        elif opcion == "2":
            realizar_venta(tienda)
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    tienda = None
    while tienda is None:
        tienda = crear_tienda()
    
    ingresar_productos(tienda)
    menu_principal(tienda)

