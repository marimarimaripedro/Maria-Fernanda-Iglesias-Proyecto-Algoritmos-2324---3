class Estadio:
    def __init__(self,id, nombre, ciudad, capacidad, restaurantes):
        """
        Construye todos los atributos necesarios para el objeto Estadio.

        Parámetros:
        id (int): identificador único del estadio
        nombre (str): nombre del estadio
        ciudad (str):ciudad donde se encuentra el estadio
        capacidad (int):número máximo de personas que puede albergar el estadio

        """
        self.id = id
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.restaurantes = restaurantes

    def show(self):
        """
        Imprime los detalles del estadio de manera formateada.

        """
        print (f"""ID: {self.id}, 
                   Nombre: {self.nombre},
                   Ciudad: {self.ciudad},
                   Capacidad: {self.capacidad},
                   Restaurantes: {self.restaurantes}
""")