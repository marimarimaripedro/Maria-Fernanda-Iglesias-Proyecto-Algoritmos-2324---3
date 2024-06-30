from APIs import *
from Partido import Partido
from Equipo import Equipo
from Estadio import Estadio
from Cliente import Cliente
from Entrada import Entrada
from Alimento import Alimento
from Bebida import Bebida
from Producto import Producto
import random
import pickle

class Administrador:
    def __init__(self):
        """
        Inicializa la clase Admin.

        Carga los datos de los archivos si están disponibles, de lo contrario, registra nuevos datos.
        Inicializa variables para gastos_vip, clientes_vip, clientes, y asistencia.

        Atributos:
        equipos (list): Lista de objetos Equipo.
        estadios (list): Lista de objetos Estadio.
        partidos (list): Lista de objetos Partido.
        gastos_vip (float): Cantidad total gastada por clientes VIP en un evento.
        clientes_vip (int): Número de clientes VIP.
        clientes (list): Lista de objetos Cliente.
        asistencia (dict): Diccionario para almacenar la asistencia de cada evento.

        """
        self.leerTXT()
        if self.equipos == None:        
            self.equipos = registrar_equipos()
            self.estadios = registrar_estadios()
            self.partidos = registrar_partidos(self.equipos, self.estadios)
            self.gastos_vip = 0
            self.clientes_vip = 0
            self.clientes = []
            self.asistencia = {}

    def agregar_partido(self, equipo_local, equipo_visitante, fecha_hora, estadio):
        """ 
        Esta funcion añade un nuevo partido a la lista de partidos.

        Parámetros:
        equipo_local (Equipo): El equipo local que participa en el partido.
        equipo_visitante (Equipo): El equipo visitante que participa en el partido.
        fecha_hora (datetime): La fecha y hora del partido.
        estadio (Estadio): El estadio donde se llevará a cabo el partido.

        No devuelve nada.

        """
        partido = Partido(equipo_local, equipo_visitante, fecha_hora, estadio)
        self.partidos.append(partido)

    def mostrar_partidos(self):
        """ 
        Esta funcion imprime todos los partidos registrados con sus 
        respectivas equipos locales y visitantes, así como la fecha y hora.

        Parámetros:
        self (Administrador): La instancia de la clase Administrador.

        Devuelve: None

        """
        for partido in self.partidos:
            print(f"{partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} - {partido.fecha_hora}")

    def buscar_partidos_por_pais(self, pais):
        """
        Esta funcion busca y devuelve una lista de partidos en los que 
        participa un equipo con el nombre dado.

        Parámetros:
        self (Administrador): La instancia de la clase Administrador.
        pais (str): El nombre del país del equipo que busca.

        Devuelve:
        list: Una lista de objetos Partido que coinciden con el país dado.

        """
        partidos_encontrados = []
        for partido in self.partidos:
            if partido.equipo_local.codigo_fifa == pais or partido.equipo_visitante.codigo_fifa == pais:
                partidos_encontrados.append(partido)
                partido.show()
        return partidos_encontrados

    def buscar_partidos_por_estadio(self, estadio):
        """
        Esta funcion busca y devuelve una lista de partidos en los que 
        participa un equipo en un estadio dado.

        Parámetros:
        self (Administrador): La instancia de la clase Administrador.
        estadio (str): El nombre del estadio donde se buscarán los partidos.

        Devuelve:
        list: Una lista de objetos Partido que coinciden con el estadio dado.

        """
        partidos_encontrados = []
        for partido in self.partidos:
            if partido.estadio.nombre == estadio:
                partidos_encontrados.append(partido)
                partido.show()
        return partidos_encontrados

    def buscar_partido_por_fecha(self, fecha):
        """
        Esta funcion busca y devuelve una lista de partidos que se 
        llevaron a cabo en una fecha específica.

        Parámetros:
        self (Administrador): La instancia de la clase Administrador.
        fecha (str): La fecha en formato AAAA-MM-DD que se busca.

        Devuelve:
        list: Una lista de objetos Partido que coinciden con la fecha dada.
        """
        partidos_fecha = []
        for partido in self.partidos:
            if partido.fecha_hora == fecha:
                partidos_fecha.append(partido)
                partido.show()
        return partidos_fecha

    def buscador_de_partidos(self) :
        """
        Esta función proporciona una interfaz de búsqueda para que 
        los usuarios encuentren partidos según diferentes criterios.

        Parámetros:
        self (Administrador): La instancia de la clase Administrador.

        Devuelve:None 
        """
        print(" 1. Buscar partidos por país: ")
        print(" 2. Buscar partidos por estadio: ")
        print(" 3. Buscar partidos por fecha: ")

        opcion = input ("Ingrese la opción que desee (1, 2, o 3): ")
        opcion = self.validarOp(opcion, 3, "Ingrese la opción que desee (1, 2, o 3): ")
        
        if opcion == "1" :
            pais = input("Ingrese el nombre del país que busca: ")
            pais = self.validarSTR(pais,"Ingrese el nombre del país que busca: ")
            busqueda_partidos = self.buscar_partidos_por_pais(pais)

            print("Los partidos de ", pais.capitalize() )

            for partido in busqueda_partidos :
                partido.show()

        elif opcion == "2" :
            estadio = input ("Ingrese el nombre del estadio que busca: ")
            estadio = self.validarSTR(estadio,"Ingrese el nombre del estadio que busca: ")
            busqueda_partidos = self.buscar_partidos_por_estadio(estadio)


            print("Los partidos en", estadio)

            for partido in busqueda_partidos :
                partido.show()

        elif opcion == "3" :
            fecha = input("Ingrese la fecha que busca (AAAA-MM-DD): ")
            fecha= self.validarSTR(fecha,"Ingrese la fecha que busca (AAAA-MM-DD): ")
            busqueda_partidos = self.buscar_partido_por_fecha(fecha)

            print ("Los partidos el", fecha )

            for partido in busqueda_partidos :

                partido.show()


    def numero_vampiro(self, cedula):
        """
        Esta funcion comprueba si un número de cédula dado es un número vampiro.

        Un número vampiro es aquel que puede expresarse como el producto de dos 
        o más enteros positivos distintos, cada uno de los cuales es un factor del número.

        Parámetros:
        cedula (int): El número de cédula que se va a comprobar.

        Devuelve:
        bool: True si el número de cédula es un número vampiro, False en caso contrario.

        """
        digitos = []
        for i in str(cedula):
            digitos.append((i))
        divisores = []
        for i in range(1, cedula):
            if cedula % i == 0:
                divisores.append(i)
        nums = []
        for i in divisores: 
            vampiro = True
            limite = len(str(cedula))/2
            contador = 1
            for x in str(i):
                if not x in digitos or contador > limite:
                    vampiro = False
                    break
                contador +=1
            if vampiro:
                nums.append(i)

        for n in range(len(nums) - 1):
            for x in range(n, len(nums)):
                if nums[n] * nums[x] == cedula:
                    return True
        return False
    
    def comprar_entrada(self,partidos):
        """
        Este método permite a un usuario comprar una entrada para un partido específico.

        Parámetros:
        self (Admin): La instancia de la clase.
        partidos (list): Una lista de todos los partidos.

        Devuelve:
        Entrada: Una instancia de la clase Entrada que representa la entrada comprada.

        """
        nombre = input("Ingrese su nombre: ")
        nombre = self.validarSTR(nombre,"Ingrese su nombre: ")
        
        cedula = input("Ingrese su cedula: ")
        cedula = self.validarInt(cedula,"Ingrese su cedula")

        edad = input("Ingrese su edad: ")
        edad = self.validarInt(edad,"Ingrese su edad")

        for i in partidos:
            i.show()
        partido = input("Ingrese numero del partido: ")
        partido = self.validarInt(partido,"Ingrese numero del partido")
        for i in partidos:
            if i.numero == partido:
                partido = i 
                break

        tipo = input("Ingrese el tipo de entrada (1 para general, 2 para VIP): ")
        tipo = self.validarOp(tipo, 2,"Ingrese el tipo de entrada (1 para general, 2 para VIP): ")
        if tipo == 1:
            precio = 35
            c = partido.estadio.capacidad[0]
        elif tipo == 2:
            precio = 75
            c = partido.estadio.capacidad[1]
        aux = 1
        fila = ""
        for i in range(c):
            if aux != 20:
                fila += " " + str(i)
            else:
                print(fila)
                fila = ""
            aux += 1
        if fila != "":
            print(fila)

        asiento = input("Ingrese el numero de asiento: ")
        asiento = self.validarInt(asiento,"Ingrese numero de asiento")
        if self.numero_vampiro(cedula):
            descuento = precio * 0.5
        else:
            descuento = precio * 0
        codigo_unico = 0
        iva = precio * 0.16

        print(f"""
            Asiento: {asiento}

            Su precio  es de {precio}
              
            Su IVA es: {iva}

            Su descuento es: {descuento}

            Su total es: {precio - descuento + iva}
 
        """)
        pagar = input(" Diga si desea proceder con el pago de su entrada: (s/n)")
        pagar = self.validarSyN(pagar," Diga si desea proceder con el pago de su entrada: (s/n)")
        if pagar == "s":
            partido.asientos_comprados.append(asiento)
            if tipo == 2:
                self.gastos_vip += precio - descuento + iva
                self.clientes_vip += 1
            print("Pago Exitoso")
            cliente = Cliente(nombre, cedula, edad)
            self.clientes.append(cliente)
            entrada = Entrada(cliente, partido, tipo, asiento, random.randint(1111111, 9999999))
            cliente.entradas.append(entrada)
            print("EL CODIGO DE SU BOLETO ES: " + str(entrada.codigo_unico))
            entrada.partido.boletos_vendidos += 1
        if pagar == "n":
            print("Pago no realizado")

        return cliente, entrada
    
    def asistencia_partidos (self):
        """
        Esta funcion Inicia el diccionario de asistencia para almacenar la asistencia de cada partido.

        El diccionario de asistencia se estructura de la siguiente manera:

        - Las claves son instancias de la clase Partido.
        - Los valores son diccionarios, donde las claves 
          son instancias de la clase Cliente y los valores 
          son el número de entradas compradas.

        """
        self.asistencia = {}

    def registrar_asistencia(self, partido, cliente):
        """
        Esta funcion registra la asistencia de un cliente a un partido específico.

        Parámetros:
        self (Admin): La instancia de la clase.
        partido (Partido): El partido específico donde se registra la asistencia.
        cliente (Cliente): El cliente cuya asistencia se está registrando.

        Devuelve: None

        """
        if partido in self.asistencia:
            if cliente in self.asistencia[partido]:
                self.asistencia[partido][cliente] += 1
            else:
                self.asistencia[partido][cliente] = 1
        else:
            self.asistencia[partido] = {cliente: 1}

    def mostrar_asistencia(self):
        """
        Esta funcion muestra la asistencia de cada cliente en cada partido 
        específico.

        La asistencia se almacena en un diccionario donde las claves
        son instancias de la clase Partido y los valores son diccionarios, 
        donde las claves son instancias de la clase Cliente y los valores 
        son la cantidad de entradas compradas.

        """
        for partido, clientes in self.asistencia.items():
            print(f"Partido: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre}")
            for cliente, cantidad_entradas in clientes.items():
                print(f"Cliente: {cliente.nombre} - Cantidad de boletos: {cantidad_entradas}")

    def validar_boletos(self, clientes):
        """
        Esta funcion valida un boleto marcándolo como usado y va incrementando 
        la asistencia del partido correspondiente.

        Parámetros:
        self (Admin): La instancia de la clase.
        clientes (list): Una lista de todos los clientes.

        Devuelve: None

        """
        cedula = input("Ingrese su cedula: ")
        cedula = self.validarInt(cedula,"Ingrese su cedula: ")
        codigo = input("Ingrese su codigo: ")
        codigo = self.validarInt(codigo,"Ingrese su codigo: ")
        for i in clientes:
            if i.cedula == cedula:
                print("CLIENTE ENCONTRADO")
                cliente = i 
        try:           
            for i in cliente.entradas:
                print(i.codigo_unico)
                if i.codigo_unico == codigo and i.usada == False:
                    i.usada = True
                    i.partido.asistencia += 1 
                    print("Su boleto ha sido validado")
                    self.registrar_asistencia(i.partido,cliente)
                    return True
            print("Su boleto no ha sido validado o ya fue usado")
        except:
            print("CLIENTE NO REGISTRADO")
    def buscar_producto_nombre (self,estadio):
        """
        Esta funcion busca un producto en los restaurantes del estadio 
        por su nombre.

        Parámetros:
        self (Admin): La instancia de la clase.
        estadio (Estadio): El estadio donde se realiza la búsqueda.

        Devuelve:
        bool: True si el producto se encuentra y se muestra, 
        False en caso contrario.

        """
        nombre = input("Ingrese el nombre del producto: ")
        #nombre = self.validarSTR(nombre,"Ingrese el nombre del producto: ")
        
        for i in estadio.restaurantes:
            for x in i.productos:
                if x.nombre == nombre:
                    x.show()
                    
                    return True
        
        print("EL PRODUCTO NO SE ENCUENTRA EN NINGUN RESTAURANTE DEL ESTADIO. LO SENTIMOS")
    def buscar_producto_tipo(self,estadio):
        """
        Esta función busca productos en los restaurantes del estadio según su tipo.

        Parámetros:
        self (Admin): La instancia de la clase.
        estadio (Estadio): El estadio donde se realizará la búsqueda.

        Devuelve:
        bool: True si el producto se encuentra y se muestra, 
        False en caso contrario.

        """
        nombre = input("Ingrese el tipo de producto: ")
        nombre = self.validarSTR(nombre,"Ingrese el tipo de producto: ")
                                 
        for i in estadio.restaurantes:
            for x in i.productos:
                if x.clasificacion == nombre:
                    x.show()
                    

    def buscar_producto_precio(self, estadio):
        """
        Esta funcion busca los productos en los restaurantes del estadio 
        según su precio.

        Parameters:
        self (Admin): La instancia de la clase.
        estadio (Estadio): El estadio donde se realizará la búsqueda.

        Returns:
        bool: True si el producto se encuentra y se muestra, 
        False en caso contrario.

        """
        minimo = input("Ingrese el precio minimo: ")
        minimo = self.validarInt(minimo,"Ingrese el precio minimo: ")
        maximo = input("Ingrese el precio maximo: ")
        maximo = self.validarInt(maximo,"Ingrese el precio maximo: ")
        for i in estadio.restaurantes:
            for x in i.productos:
                if x.precio >= minimo and x.precio <= maximo:
                    x.show()
                    
                
    def venta_restaurantes(self, estadio, cliente):
        """
        Este método maneja el proceso de comprar productos en un restaurante.

        Parámetros:
        self (Admin): La instancia de la clase.
        estadio (Estadio): El estadio donde se encuentra el restaurante.
        cliente (Cliente): El cliente que realiza la compra.

        Devuelve: None

        """
        print ("Bienvenido al restaurante. Seleccione uno para continuar")
        for i in estadio.restaurantes: 
            print(i.nombre)
        restaurante = input("Restaurante al que desea acceder: ")
        #restaurante = self.validarSTR(restaurante,"Restaurante al que desea acceder: ")
        for i in estadio.restaurantes:
            if i.nombre == restaurante:
                restaurante = i 
        for i in restaurante.productos:
            if i.clasificacion == "Bebida":
                if cliente.edad < 18 and i.es_alcoholica == True:
                    continue
            i.show()
        venta_producto = input("Producto que desea comprar: ")
        #venta_producto = self.validarSTR(venta_producto,"Producto que desea comprar: ")
        for i in restaurante.productos:
            if i.nombre == venta_producto:
                venta_producto = i
                break
        cantidad_producto = input("Ingrese la cantidad de productos que desea comprar: ")
        cantidad_producto = self.validarInt(cantidad_producto,"Ingrese la cantidad de productos que desea comprar: ")
        proceder_con_compra = input("Desea proceder con compra (s/n): ")
        proceder_con_compra = self.validarSyN(proceder_con_compra,"Ingrese la cantidad de productos que desea comprar: ")
        if proceder_con_compra == "s":
            venta_producto.stock -= cantidad_producto 
            if self.es_numero_perfecto(cliente.cedula):
                descuento = venta_producto.precio * 0.15
            else:
                descuento = venta_producto.precio * 0
            iva = venta_producto.precio * 0.16
            precio_total = venta_producto.precio + iva - descuento
            self.gastos_vip += precio_total
            venta_producto.venta += cantidad_producto

            print(f"""
                   Producto: {venta_producto.nombre}, 
                   Cantidad: {cantidad_producto},
                   Precio: {venta_producto.precio},
                   IVA: {iva},
                   Descuento: {descuento},
                   Precio Total: {precio_total}
                  """)

    def es_numero_perfecto(self, numero):
        """
        Esta funcion omprueba si un número dado es un número perfecto.

        Un número perfecto es aquel número positivo que se iguala a la suma de 
        sus divisores, excluyendo a el mismo.

        Parámetros:
        self (Admin): La instancia de la clase.
        numero (int): El número que se va a comprobar.

        Devuelve:
        bool: True si el número es perfecto, 
        False en caso contrario.

        """
        numero = int(numero)
        suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
        return suma_divisores == numero
    
    def indicadores_gestion(self, partidos, estadios ):
        """
        Este método maneja los indicadores de gestión para el 
        estadio deportivo, donde el usuario va a poder seleccionar 
        aquella opcion que le permita acceder a lainformación que 
        desee dentro de las estadisticas disponibles.

        Parámetros:
        self (Admin): La instancia de la clase.

        Devuelve: None

        """
        print("""   Ingresa 1 para estadistica del promedio de gasto de un cliente VIP en un partido
                    Ingresa 2 para tabla con info de partidos y estadisticas
                    Ingresa 3 para estadistica del partido con mayor asistencia
                    Ingresa 4 para estadistica del partido con mayor boletos vendidos
                    Ingresa 5 para estadistica del Top 3 productos más vendidos en el restaurante.
                    Ingresa 6 para estadistica del Top 3 de clientes que más compraron boletos 
                  """)
              
        opcion = input("Ingresa el numero de la estadistica que deseas ver: ")
        opcion = self.validarInt(opcion,"Ingresa el numero de la estadistica que deseas ver: ")
        if opcion == 1:
            if self.clientes_vip != 0:
                print(f"El promedio de gasto de un cliente VIP en un partido es: {self.gastos_vip / self.clientes_vip}")
            else:
                print("No hay clientes VIP")
        if opcion == 2:
            ordenada = []
            for p in partidos:
                mayor = p 
                for y in partidos:
                    if mayor in ordenada:
                        mayor = y
                    if y.asistencia > mayor.asistencia and y not in ordenada:
                        mayor = y
                ordenada.append(mayor)
            print("-------------------------------------------------------------------------")
            
            for i in ordenada:
                print(f"Partido: {i.equipo_local.nombre} vs {i.equipo_visitante.nombre}")
                print(f"Asistencia: {i.asistencia}")
                print(f"Boletos vendidos: {i.boletos_vendidos}")
                print(f" i.asistencia / i.boletos_vendidos")
                print("-------------------------------------------------------------------------")
            
        if opcion == 3:
            mayor = partidos[0]
            for i in partidos:
                if i.asistencia > mayor.asistencia:
                    mayor = i
            print(f"El partido con mayor asistencia es:{mayor.equipo_local.nombre} vs {mayor.equipo_visitante.nombre}")

        if opcion == 4:
        
            mayor = partidos[0]
            for i in partidos:
                if i.boletos_vendidos > mayor.boletos_vendidos:
                    mayor = i

            print(f"El partido con mayor boletos vendidos es: {mayor.equipo_local.nombre} vs {mayor.equipo_visitante.nombre}")

        if opcion == 5:
            productos = []
            for i in estadios:
                for x in i.restaurantes:
                    for y in x.productos:
                        productos.append(y)

            ordenada = []

            for i in productos:
                mayor = i 
                for y in productos:
                    if y.venta > mayor.venta and y not in ordenada:
                         mayor = y
                ordenada.append(mayor)

            print(f"El Top 3 productos más vendidos en el restaurante son: 1. {ordenada[0].nombre}, 2. {ordenada[1].nombre} y 3. {ordenada[2].nombre}")

        if opcion == 6:
            if len(self.clientes) >= 3:
                ordenada = []

                for i in self.clientes:
                    mayor = i 
                    for y in self.clientes:
                        if len(y.entradas) > len(mayor.entradas) and y not in ordenada:
                            mayor = y
                    ordenada.append(mayor)

                print(f"El Top 3 de clientes que más compraron boletos es: 1. {ordenada[0].nombre}, 2. {ordenada[1].nombre} y 3. {ordenada[2].nombre}")
            else:
                print("No hay suficientes clientes")
    def validarSTR(self, palabra, mensaje):
        """
        Valida si la entrada de cadena es alfabética.

        Parámetros:
        palabra (str): La cadena de entrada a validar.
        mensaje (str): El mensaje que se mostrará si la entrada no es válida.

        Devuelve:
        str: La cadena de entrada validada si es alfabética.

        Lanza: None

        """
        while not palabra.isalpha():
            palabra = input(mensaje)
        return palabra
    
    def validarInt(self, num, mensaje):
        """
        Valida si la entrada de cadena es numérica.

        Parámetros:
        num (str): La cadena de entrada a validar.
        mensaje (str): El mensaje que se mostrará si la entrada no es válida.

        Devuelve:
        int: La entrada numérica validada.

        Lanza:None

        """
        while not num.isnumeric():
            num = input(mensaje)
        return int(num)
    
    def validarOp(self, opcion, max, mensaje):
        """
        Valida si la entrada de cadena es numérica y se encuentra dentro de un 
        rango especificado.

        Parámetros:
        opcion (str): La cadena de entrada a validar.
        max (int): El valor máximo permitido para la entrada.
        mensaje (str): El mensaje que se mostrará si la entrada no es válida.

        Devuelve:
        int: La entrada validada como un entero.

        Lanza:None

        """
        while not opcion.isnumeric() or int(opcion) > max:
            opcion = input(mensaje)
        return int(opcion)
    
    def validarSyN(self, opcion, mensaje):
        """
        Valida si la entrada de cadena es 's' o 'n'.

        Parámetros:
        opcion (str): La cadena de entrada a validar.
        mensaje (str): El mensaje va mostrar si la entrada no es válida.

        Devuelve:
        str: La cadena de entrada validada.

        Lanza:None

        """
        while not opcion.isalpha() or opcion != "s" and opcion != "n":
            opcion = input(mensaje)
        return opcion
    def leerTXT(self):
        """
        Este método se utiliza para cargar datos desde archivos de texto.

        El método intenta abrir y leer los archivos 'equipos.txt', 
        'estadios.txt','partidos.txt', y 'usuarios.txt'. Si los archivos 
        existen y son legibles, los datos se cargan en los atributos 
        correspondientes de la clase.

        Si cualquiera de los archivos no existe o no es legible, los atributos 
        de la clase se establecen en None.

        Parámetros: Ninguno

        Devuelve: Ninguno

        """
        try:
            with open("equipos.txt", "rb") as f:
                self.equipos = pickle.load(f)
            with open("estadios.txt", "rb") as f:
                self.estadios = pickle.load(f)
            with open("partidos.txt", "rb") as f:
                self.partidos = pickle.load(f)
            with open("usuarios.txt", "rb") as f:
                self.clientes = pickle.load(f)
        except:
            self.equipos = None
            self.estadios = None
            self.partidos = None
            self.clientes = None
    def guardarTXT(self):
        """
        Este método se utiliza para guardar datos en archivos de texto.

        El método intenta abrir y escribir en los archivos 'equipos.txt', 
        'estadios.txt', 'partidos.txt' y 'usuarios.txt'. Si los archivos 
        existen y son escribibles, los datos de los atributos correspondientes 
        de la clase se guardan.

        Si cualquiera de los archivos no existe o no es escribible, se lanza 
        una excepción y se detiene la ejecución del método.

        Parámetros: Ninguno

        Devuelve: Ninguno
        
        """
        with open("equipos.txt", "wb") as f:
            pickle.dump(self.equipos, f)
        with open("estadios.txt", "wb") as f:
            pickle.dump(self.estadios, f)
        with open("partidos.txt", "wb") as f:
            pickle.dump(self.partidos, f)
        with open("usuarios.txt", "wb") as f:
            pickle.dump(self.clientes, f)