class VentaRestaurante:
    def __init__(self, nombre, productos):
        """
        Inicializa una nueva instancia de la clase VentaRestaurante.

        Parámetros:
        nombre (str): El nombre del restaurante.
        productos (list): Una lista de productos disponibles en el restaurante.

        Devuelve: None
        
        """
        self.productos = productos
        self.nombre = nombre
