class Producto():
    def __init__(self, nombre: str, precio: int, stock: int=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = max(0, stock)
        
    @property
    def nombre(self):
        return self._nombre
   
    @property
    def precio(self):
        return self._precio
        
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, valor):
        self._stock = max(0, valor)


