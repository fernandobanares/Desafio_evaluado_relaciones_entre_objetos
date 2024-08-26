from producto import Producto

class Tienda:
    def __init__(self, nombre: str, costo_delivery: int):
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self._productos = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_delivery(self):
        return self._costo_delivery

    def ingresar_producto(self, nombre: str, precio: int, stock: int = 0):
        for producto in self._productos:
            if producto.nombre == nombre:
                producto.stock += stock
                return
        nuevo_producto = Producto(nombre, precio, stock)
        self._productos.append(nuevo_producto)

    def listar_productos(self):
        listado = ""
        for producto in self._productos:
            listado += f"{producto.nombre} - ${producto.precio}\n"
        return listado

    def realizar_venta(self, nombre_producto: str, cantidad: int):
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    return f"Venta realizada: {cantidad} {nombre_producto}(s)"
                else:
                    cantidad_vendida = producto.stock
                    producto.stock = 0
                    return f"Venta parcial: {cantidad_vendida} {nombre_producto}(s) - Stock agotado"
        return "Producto no disponible"


class Restaurante(Tienda):
    def ingresar_producto(self, nombre: str, precio: int, stock: int = 0):
        Tienda.ingresar_producto(self, nombre, precio, 0)


    def realizar_venta(self, nombre_producto: str, cantidad: int):
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                return f"Venta realizada: {cantidad} {nombre_producto}(s)"
        return "Producto no disponible"

class Supermercado(Tienda):
    def listar_productos(self):
        listado = ""
        for producto in self._productos:
            stock_info = f"{producto.stock}"
            if producto.stock < 10:
                stock_info += " - Pocos productos disponibles"
            listado += f"{producto.nombre} - ${producto.precio} - Stock: {stock_info}\n"
        return listado


class Farmacia(Tienda):
    def listar_productos(self):
        listado = ""
        for producto in self._productos:
            precio_info = f"{producto.precio}"
            if producto.precio > 15000:
                precio_info += " - Envío gratis al solicitar este producto"
            listado += f"{producto.nombre} - ${precio_info}\n"
        return listado

    def realizar_venta(self, nombre_producto: str, cantidad: int):
        if cantidad > 3:
            return "No se puede vender más de 3 unidades por venta"
        return Tienda.realizar_venta(self, nombre_producto, cantidad)
