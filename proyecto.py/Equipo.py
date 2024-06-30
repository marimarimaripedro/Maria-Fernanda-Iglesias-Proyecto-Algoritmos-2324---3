class Equipo:
    def __init__(self, id, codigo_fifa, nombre, grupo):
        """
        Inicializa una nueva instancia de la clase Equipo.

        Parámetros:
        id (int): Identificador único para el equipo.
        codigo_fifa (str): Código FIFA del equipo.
        nombre (str): Nombre del equipo.
        grupo (str): Grupo al que pertenece el equipo.

        Devuelve:
        None. 

        """
        self.id = id
        self.codigo_fifa = codigo_fifa
        self.nombre = nombre
        self.grupo = grupo

    def show(self):
        """
        Este método imprime los detalles del objeto Equipo.

        Parámetros:
        self (Equipo): El objeto Equipo que se imprimirá.

        Devuelve:
        None. Imprime los detalles del objeto Equipo. 

        """
        print (f"""ID: {self.id}, 
                   Codigo: {self.codigo_fifa},
                   Nombre: {self.nombre},
                   Grupo: {self.grupo}
""")