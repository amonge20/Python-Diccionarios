# Supongamos que tienes los resultados de una elección con los nombres
# de los candidatos y la cantidad de votos obtenidos por cada uno.
# Implementa un programa en Python que permita registrar los votos,
# mostrar la lista completa de candidatos y sus votos, encontrar al
# candidato ganador (con más votos) y calcular el porcentaje de votos que
# obtuvo cada candidato.

# Guardamos los candidatos junto con sus votos
candidatos = {}
continuar = True

# Menu interactivo para los candidatos
while continuar:
    print("\n --- ELECCIONES ---")
    print("1. Registrar votos de un candidato")
    print("2. Mostrar lista de candidatos y votos")
    print("3. Mostrar candidato ganador")
    print("4. Calcular porcentaje de votos")
    print("5. Salir")

    opcion = input("Selecciona una opcion: ")

    # Registrar el voto
    if opcion == "1":
        nombre = input("Nombre del candidato: ").strip()
        votos = int(input("Cantidad de votos obtenidos: "))

        if nombre in candidatos:
            candidatos[nombre] += votos  # sumamos votos si ya existe
        else:
            candidatos[nombre] = votos
        print(f"Votos registrados para {nombre}.")
    
    # Mostrar lista completa
    elif opcion == "2":
        if not candidatos:
            print("No hay candidatos registrados.")
        else:
            print("Candidatos y sus votos:")
            for candidato, votos in candidatos.items():
                print(f"{candidato}: {votos} votos")
    
    # Mostrar candidato ganador
    elif opcion == "3":
        if not candidatos:
            print("No hay candidatos registrados.")
        else:
            ganador = max(candidatos, key=candidatos.get)
            votos_ganador = candidatos[ganador]
            print(f"El candidato ganador es {ganador} con {votos_ganador} votos.")
    
    # Calcular porcentaje de votos
    elif opcion == "4":
        if not candidatos:
            print("No hay candidatos registrados.")
        else:
            total_votos = sum(candidatos.values())
            print(f"Total de votos: {total_votos}")
            print("Porcentaje de votos por candidato:")
            for candidato, votos in candidatos.items():
                porcentaje = (votos / total_votos) * 100
                print(f"{candidato}: {porcentaje:.2f}%")
    
    # Salir de las elecciones
    elif opcion == "5":
        print("Saliendo del sistema de elecciones...")
        continuar = False
    
    else:
        print("Opcion no disponible. Intentelo de nuevo")