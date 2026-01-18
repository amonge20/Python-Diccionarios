# Implementa un programa en Python que permita registrar y mantener un
# seguimiento de los puntajes de un juego. El programa debe permitir a los
# jugadores ingresar sus nombres y puntajes, almacenarlos en un
# diccionario y proporcionar funcionalidades para mostrar el puntaje más
# alto, el promedio de puntajes y la cantidad total de jugadores.

puntajes = {}

# Registro de puntajes de jugadores
registro_puntajes = {'Jugador1': 150, 'Jugador2': 200, 'Jugador3': 180}
for jugador, puntaje in registro_puntajes.items():
    puntajes[jugador] = puntaje
print("Puntajes registrados:", puntajes)

# Funcionalidad para mostrar el puntaje más alto
puntaje_mas_alto = max(puntajes.values())
jugador_mas_alto = max(puntajes, key=puntajes.get)
print(f"Puntaje más alto: {puntaje_mas_alto} por {jugador_mas_alto}")

# Funcionalidad para calcular el promedio de puntajes
promedio_puntajes = sum(puntajes.values()) / len(puntajes)
print(f"Promedio de puntajes: {promedio_puntajes}")

# Funcionalidad para mostrar la cantidad total de jugadores
total_jugadores = len(puntajes)
print(f"Cantidad total de jugadores: {total_jugadores}")