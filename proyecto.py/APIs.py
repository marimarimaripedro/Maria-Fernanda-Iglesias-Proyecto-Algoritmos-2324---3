
from Estadio import Estadio
from Partido import Partido 
from Equipo import Equipo
from Bebida import *
from Alimento import *
from VentaRestaurante import *
import requests
def registrar_estadios():

    """
    Esta función recupera datos sobre estadios de una API externa
    y crea una lista de objetos Estadio.

    Parámetros:
    Ninguno

    Devuelve:
    lista: Una lista de objetos Estadio, cada uno representando un estadio.

    """
    # Enviar una solicitud GET al punto final de la API para obtener datos de estadios
    response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")

    print (response.json())

    # Inicializar una lista vacía para almacenar objetos Estadio
    estadios = []

    for i in response.json():
        restaurantes = []
        for r in i["restaurants"]:
            productos = []
            for p in r["products"]:
                if p["adicional"] == "alcoholic" or p["adicional"] == "non-alcoholic":
                    producto = Bebida(p['name'], "Bebida",p["quantity"], float(p["price"]), int(p["stock"]), p["adicional"])
                else:
                    producto = Alimento(p['name'], "Alimento",p["quantity"], float(p["price"]), int(p["stock"]), p["adicional"])
                productos.append(producto)
            restaurante = VentaRestaurante(r["name"], productos)
            restaurantes.append(restaurante)
        estadios.append(Estadio(i["id"], i["name"],i["city"], i["capacity"], restaurantes))

    return estadios

def registrar_partidos(equipos, estadios):
    """
    Esta función recupera datos de partidos de una API externa,
    crea una lista de objetos Partido y asocia cada partido con 
    sus respectivos equipos locales / visitantes, y estadio.

    Parámetros:
    equipos (list): Una lista de objetos Equipo que representan los equipos.
    estadios (list): Una lista de objetos Estadio que representan los estadios.

    Devuelve:
    list: Una lista de objetos Partido, cada uno representando un partido.

    """
    # Enviar una solicitud GET al punto final de la API para obtener datos de partidos
    response_1 = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")

    print (response_1.json())

    # Inicializar una lista vacía para almacenar objetos Partido
    partidos = []

    for i in response_1.json():
        home = 0
        for e in equipos:           
            if e.id == i["home"]["id"]:
                home = e
        away = 0
        for e in equipos:           
            if e.id == i["away"]["id"]:
                away = e
        estadio = 0
        for e in estadios:
            if e.id == i["stadium_id"]:
                estadio = e
        partidos.append(Partido(i["id"],i["number"], home,away,i["date"], i["group"], estadio))

    return partidos 

def registrar_equipos():
    """
    Esta función recupera datos de equipos de una API externa,
    crea una lista de objetos Equipo y la devuelve.

    Parámetros:
    Ninguno

    Devuelve:
    list: Una lista de objetos Equipo, cada uno representando un equipo.

    """
    # Enviar una solicitud GET al punto final de la API para obtener datos de equipos
    response_2 = requests.get(" https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")

    print (response_2.json())

     # Inicializar una lista vacía para almacenar objetos Equipo
    equipos = []

    for i in response_2.json():
        equipos.append(Equipo(i["id"], i["code"], i["name"], i["group"]))

    return equipos

estadios = registrar_estadios()
equipos = registrar_equipos()
partidos = registrar_partidos(equipos, estadios) 