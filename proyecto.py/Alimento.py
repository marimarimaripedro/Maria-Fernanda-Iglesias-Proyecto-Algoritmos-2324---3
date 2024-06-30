from Producto import Producto

class Alimento(Producto):
    """
    Clase para objetos Alimento. Hereda de la clase Producto. 
    
    """

    def __init__(self, nombre, clasificacion, cantidad, precio, stock, es_empacado):
        """
        Inicializa un nuevo objeto Alimento.

        Parámetros:
        nombre (str): El nombre del alimento.
        clasificacion (str): La clasificación del alimento.
        cantidad (int): La cantidad del alimento.
        precio (float): El precio del alimento.
        stock (int): El stock del alimento.
        es_empacado (bool): Si el alimento está empacado o no.

        Devuelve: None

        """
        super().__init__(nombre, clasificacion, cantidad, precio, stock)
        self.es_empacado = es_empacado
        
    def show(self):
        """
        Esta función imprime los detalles/info relevante del objeto Alimento.

        Parámetros:
        self (Alimento): El objeto Alimento que se imprimirá.

        Devuelve: None

        Imprime:
        Nombre: El nombre del alimento.
        Clasificación: La clasificación del alimento.
        Cantidad: La cantidad del alimento.
        Precio: El precio del alimento.
        Stock: El stock del alimento.
        Es Empacado: Si el alimento está empacado o no.

        """
        print (f"""Nombre: {self.nombre}, 
                   Clasificacion: {self.clasificacion},
                   Cantidad: {self.cantidad},
                   Precio: {self.precio},
                   Stock: {self.stock},
                   Es Empacado: {self.es_empacado}
    """)