class Partido:
   def __init__(self, id, numero, equipo_local, equipo_visitante, fecha_hora, grupo, estadio):
       
       """
       Inicializa una nueva instancia de la clase Partido.

       Parámetros:
       id (int): Identificador único para el partido.
       numero (int): El número del partido.
       equipo_local (Equipo): El equipo local que participa en el partido.
       equipo_visitante (Equipo): El equipo visitante que participa en el partido.
       fecha_hora (datetime): La fecha y hora del partido.
       grupo (str): El grupo al que pertenece el partido.
       estadio (Estadio): El estadio donde se llevará a cabo el partido.

       Atributos:
       id (int): Identificador único para el partido.
       numero (int): El número del partido.
       equipo_local (Equipo): El equipo local que participa en el partido.
       equipo_visitante (Equipo): El equipo visitante que participa en el partido.
       fecha_hora (datetime): La fecha y hora del partido.
       grupo (str): El grupo al que pertenece el partido.
       estadio (Estadio): El estadio donde se llevará a cabo el partido.
       asientos_comprados (list): Lista de asientos que se han vendido para el partido.
       boletos_vendidos (int): El número de entradas vendidas para el partido.
       asistencia (int): El número de espectadores que asistieron al partido.

       """

       self.id = id
       self.numero = numero
       self.equipo_local = equipo_local
       self.equipo_visitante = equipo_visitante
       self.fecha_hora = fecha_hora
       self.grupo = grupo
       self.estadio = estadio
       self.asientos_comprados = []
       self.boletos_vendidos = 0
       self.asistencia = 0 

   def show(self):
        
       """
       Imprime una representación formateada de un objeto 
       Partido como cadena.

       Parámetros:
       self (Partido): El objeto Partido que se imprimirá.

       Devuelve: None

       """
       print (f"""ID: {self.id}, 
                   Numero: {self.numero},
                   Equipo Local: {self.equipo_local.nombre},
                   Equipo Visitante: {self.equipo_visitante.nombre},
                   Fecha: {self.fecha_hora},
                   Grupo: {self.grupo},
                   Estadio: {self.estadio.nombre}
""")
        
   