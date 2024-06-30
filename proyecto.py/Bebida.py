from Producto import Producto

class Bebida(Producto):
    """
    Clase para objetos Bebida. Hereda de la clase Producto. 
    
    """
    def __init__(self, nombre, clasificacion, cantidad, precio, stock, es_alcoholica):
        """
        Inicializa una nueva instancia de la clase Bebida.

        Parámetros:
        nombre (str): El nombre de la bebida.
        clasificacion (str): La clasificación de la bebida.
        cantidad (int): La cantidad de la bebida.
        precio (float): El precio de la bebida.
        stock (int): El stock de la bebida.
        es_alcoholica (bool): Indica si la bebida es alcohólica.

        Devuelve: None

        """
        super().__init__(nombre, clasificacion, cantidad, precio, stock)
        self.es_alcoholica = es_alcoholica
        
    def show(self):
        """
        Imprime los detalles de la bebida.

        Parámetros: None (excepto self)

        Devuelve: None

        """
        print (f"""Nombre: {self.nombre}, 
                   Clasificacion: {self.clasificacion},
                   Cantidad: {self.cantidad},
                   Precio: {self.precio},
                   Stock: {self.stock},
                   Es Alcoholica: {self.es_alcoholica}
""")