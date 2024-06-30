from Administrador import Administrador
from Cliente import Cliente
def main():
    """
    Función principal para ejecutar el servidor de venta de tickets para 
    la Eurocopa Alemania 2024. Administra las interacciones del usuario, 
    las opciones del menú y llama a las funciones adecuadas según las 
    opciones elegidas por el usuario.

    """
    admin = Administrador() # Inicializa el objeto Administrador

    while True:
        print(f"""
       
              Bienvenido al servidor de venta de tickets de la Eurocopa Alemania 2024
              Para acceder a informacion que busca 
              revise las opciones que se le presentan
              e ingrese el numero correspondiente: 
              
            ("===== MENÚ PRINCIPAL =====")

            ("1. Gestión de partidos y estadios")
            ("2. Gestión de venta de entradas")
            ("3. Gestión de asistencia a partidos")
            ("4. Gestión de restaurantes")
            ("5. Gestión de venta de restaurantes")
            ("6. Indicadores de gestión (estadísticas)")
            ("0. Salir")
              
               """)
        
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            """
            Submenú para la gestión de partidos y estadios.
            Administra las interacciones del usuario, las opciones del menú y llama a las funciones adecuadas según las opciones elegidas por el usuario.
            
            """
            while True:
                print (f"""
        
                Dentro de Gestión de partidos y estadios
                para acceder a informacion que busca 
                revise las opciones que se le presentan
                e ingrese el numero correspondiente: 
                

                ("1. Buscar todos los partidos de un país ")
                ("2. Buscar todos los partidos que se jugarán en un estadio específico ")
                ("3. Buscar todos los partidos que se jugarán en una fecha determinada ")
                ("4. Salir")
                       
                """)

                opcion2 = int(input("Ingrese una opción: "))

                if opcion2 == 1:
                # Función para buscar partidos por país
                    pais = input("Ingrese el nombre del pais: ")
                    admin.buscar_partidos_por_pais(pais)

                if opcion2 == 2:
                # Función para buscar partidos por estadio específico
                    estadio_especifico = input("Ingrese el nombre del estadio: ")
                    admin.buscar_partidos_por_estadio(estadio_especifico)

                if opcion2 == 3:
                # Función para buscar partidos por fecha específica
                    fecha_especifica = input("Ingrese las fecha deseada: ")
                    admin.buscar_partido_por_fecha(fecha_especifica)

                if opcion2 == 4:
                # Salir del submenú de gestión de partidos y estadios
                    break

        if opcion == 2:
        # Función para comprar entradas
            cliente, entrada = admin.comprar_entrada(admin.partidos)
            admin.guardarTXT()

        if opcion == 3:
        # Función para validar la asistencia a los partidos
            admin.validar_boletos(admin.clientes)
            admin.guardarTXT()

        
        if opcion == 4:
            """
            Submenú para la gestión de restaurantes.
            Administra las interacciones del usuario, las opciones del menú 
            y llama a las funciones adecuadas según las opciones elegidas 
            por el usuario.
            
            """
            try:
                if entrada.tipo == 2:

                    while True:
                        print (f"""
                
                        Dentro de Gestión de Restaurantes
                        para acceder a informacion que busca 
                        revise las opciones que se le presentan
                        e ingrese el numero correspondiente: 
                        

                        ("1. Buscar productos por nombre")
                        ("2. Buscar productos por tipo ")
                        ("3. Buscar productos por precio")
                        ("4. Salir")
                            
                        """)

                        opcion2 = (input("Ingrese una opción: "))

                        opcion2 = admin.validarOp(opcion2, 4,"Ingrese una opción: ")

                        if opcion2 == 1:
                        # Función para buscar productos por nombre
                            admin.buscar_producto_nombre(entrada.partido.estadio)

                        if opcion2 == 2:
                        # Función para buscar productos por tipo
                            admin.buscar_producto_tipo(entrada.partido.estadio)

                        if opcion2 == 3:
                        # Función para buscar productos por precio
                            admin.buscar_producto_precio(entrada.partido.estadio)

                        if opcion2 == 4:
                        # Salir del submenú de gestión de restaurantes
                            break
                    
                else:
                    print("NO ES UN CLIENTE VIP")
            except:
                print("DEBE INGRESAR AL ESTADIO PARA ACCEDER AL RESTAURANTE")
                admin.guardarTXT()
        
        if opcion == 5:
        # Función para vender comidas y bebidas en los restaurantes
            admin.venta_restaurantes( entrada.partido.estadio, cliente)
            admin.guardarTXT()

        if opcion == 6:
        # Función para ver estadísticas
            admin.indicadores_gestion(admin.partidos, admin.estadios)
            admin.guardarTXT()

main()