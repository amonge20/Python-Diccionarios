# Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
# estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
# una lista de fechas en las que asistió a clases. Implementa un programa
# en Python que utilice un diccionario para almacenar la información de las
# asistencias. El programa debe permitir registrar la asistencia de los
# estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
# estudiantes y las fechas en las que asistieron.

asistencias= {}
estudiantes = {"Aitor","Didac","Alex","Guille","Isaac"}

for estudiante in estudiantes:
    asistencias[estudiante] = []

# Se mantiene por defecto true
continuar = True

# Menu interactivo para controlar la asistencia de los alumnos
while continuar == True:
    print("--- CONTROL DE ASISTENCIA ---")
    print("1. Registrar asistencia del estudiante")
    print("2. Agregar nueva fecha de asistencia")
    print("3. Mostrar la lista de los estudiantes y de las fechas que asistieron")
    print("4. Salir")

    opcion = int(input("Selecciona una opcion:"))
    
    # Registrar asistencia del estudiante
    if opcion == 1:
        for estudiante in estudiantes:
            fecha = input(f"Introduce la fecha que asistió {estudiante} (YYYY-MM-DD): ")
            asistencias[estudiante].append(fecha)

    # Agregar nueva fecha de asistencia
    elif opcion == 2:
        estudiante = input("Nombre del estudiante: ")

        if estudiante in asistencias:
            fechActualizada = input(f"Introduce nueva fecha para {estudiante}: ")
            asistencias[estudiante].append(fechActualizada)
        else:
            print("Ese estudiante no existe")
    
    # Mostrar la lista de todos los estudiantes, tambien segun las fechas de asistencias
    elif opcion == 3:
        print("\n--- REGISTRO ---")
        for estudiante, fechas in asistencias.items():
            print(f"{estudiante}: {', '.join(fechas)}")
    
    # Salir del programa
    else:
        # Se acaba el programa
        continuar = False
        break