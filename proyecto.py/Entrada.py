class Entrada:
    def __init__(self, cliente, partido, tipo, asiento, codigo_unico):
        """
        Inicializa una nueva instancia de la clase Entrada.

        Parámetros:
        cliente (str): El nombre del cliente que compró el ticket.
        partido (str): El nombre del partido deportivo.
        tipo (str): El tipo de ticket (por ejemplo, VIP, Entrada General).
        asiento (str): El número de asiento asignado al ticket.
        codigo_unico(str): El código único asignado al ticket.

        Ademas esta: 
        usada (bool): Indica si el ticket ha sido usado para 
        comprar un asiento, que inicialmente, es False.
        
        """
        self.cliente = cliente
        self.partido = partido
        self.tipo = tipo
        self.asiento = asiento
        self.codigo_unico = codigo_unico
        self.usada = False
        
