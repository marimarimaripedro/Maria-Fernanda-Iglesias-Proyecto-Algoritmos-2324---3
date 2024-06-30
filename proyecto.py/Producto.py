class Producto:
    def __init__(self, nombre, clasificacion, cantidad, precio, stock):
        """
        Inicializa una nueva instancia de la clase Producto.

        Parámetros:
        nombre (str): El nombre del producto.
        clasificacion (str): La clasificación del producto.
        cantidad (int): La cantidad del producto.
        precio (float): El precio del producto.
        stock (int): El stock del producto.

        Devuelve: None
        """
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.cantidad = cantidad
        self.precio = precio
        self.stock = stock
        self.venta = 0