class Cliente:
    def __init__(self, nombre, cedula, edad):
        """
        Inicializa una nueva instancia de Cliente.

        Parámetros:
        nombre (str): El nombre del cliente.
        cedula (str): El número de identificación del cliente.
        edad (int): La edad del cliente.

        Devuelve: None

        """
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.entradas = []