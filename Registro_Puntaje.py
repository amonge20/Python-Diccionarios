# Implementa un programa en Python que permita registrar y mantener un
# seguimiento de los puntajes de un juego. El programa debe permitir a los
# jugadores ingresar sus nombres y puntajes, almacenarlos en un
# diccionario y proporcionar funcionalidades para mostrar el puntaje más
# alto, el promedio de puntajes y la cantidad total de jugadores.

registro_puntajes = {}

# Se mantiene por defecto true
continuar = True

# Menu interactivo para añadir jugadores segun su puntaje
while continuar == True:
    print("--- MAQUINA RECREATIVA DE ARCADE ---")
    print("1. Registrar jugador")
    print("2. Puntaje más alto")
    print("3. Promedio del puntaje")
    print("4. Cantidad total de jugadores")
    print("5. Salir")

    opcion = int(input("Selecciona un numero: "))

    # Añadir jugadores
    if opcion == 1:
        jugador = input("Nombre del jugador: ")
        puntuacion = int(input("Puntuacion: "))
        registro_puntajes[jugador] = puntuacion
        print("Jugador registrado")

    # Puntaje más alto
    elif opcion == 2:
        if registro_puntajes:  # Verifica que haya jugadores
            jugador_mas_alto = max(registro_puntajes, key=registro_puntajes.get)
            maxima_puntuacion = registro_puntajes[jugador_mas_alto]
            print(f"El jugador con mayor puntaje es {jugador_mas_alto} con {maxima_puntuacion}")
        else:
            print("No hay jugadores registrados todavía.")

    # Promedio del puntaje
    elif opcion == 3:
        if registro_puntajes:
            promedio_puntuacion = sum(registro_puntajes.values()) / len(registro_puntajes)
            print(f"El promedio de puntajes es: {promedio_puntuacion:.2f}")
        else:
            print("No hay puntajes registrados todavía.")
            print("")
    # Cantidad de jugadores
    elif opcion == 4:
        print(f"Cantidad total de jugadores: {len(registro_puntajes)}")
        for jugador, puntaje in registro_puntajes.items():
            print(f"Jugador {jugador} con puntuación {puntaje}")
        print("")

    # Fin del juego
    else:
        continuar = False
        break