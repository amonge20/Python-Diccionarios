# Eres un gerente de proyectos y necesitas un programa para administrar
# las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
# una descripción y un responsable asignado. Implementa un programa en
# Python que utilice un diccionario para almacenar la información de las
# tareas. El programa debe permitir agregar nuevas tareas, asignar
# responsables a las tareas existentes, actualizar las descripciones de las
# tareas y mostrar la lista completa de tareas y responsables. 

# Lista vacia
proyectos = {}

# Se mantiene por defecto true
continuar = True

# Menu interactivo para gestionar el proyecto siendo el gerente
while continuar == True:
    print("--- ADMINISTRACIÓN DE PROYECTOS ---")
    print("1. Añadir tarea, descripcion y responsable")
    print("2. Asignar tarea existente a un responsable")
    print("3. Actualizar la tarea existente")
    print("4. Mostrar las tareas actuales")
    print("5. Salir")

    numero_seleccionado = int(input("Por favor selecciona un numero: "))

    # Añadimos nueva tarea, descripción y responsable
    if numero_seleccionado == 1:
        tarea_nueva = input("Introduce una tarea: ")
        nueva_descripcion = input("Introduce descripción: ")
        nuevo_responsable = input("Introduce el nombre del responsable: ")

        # Se añade la nueva tarea, junto la descripcion más el responsable de esa tarea
        proyectos[tarea_nueva] = {
            "descripcion": nueva_descripcion,
            "responsable": nuevo_responsable
        }

    # Asignar una tarea existente a un responsable
    elif numero_seleccionado == 2:
        tarea = input("Introduce una tarea existente: ")
        responsable = input("Introduce a un responsable existente para esta tarea: ")

        # Si la tarea no existe
        if tarea not in proyectos:
            print("La tarea no existe")

        # Si el responsable no existe
        elif responsable not in [d["responsable"] for d in proyectos.values()]:
            print("El responsable no existe")

        # Se le asigna la tarea existente a otro responsable existente
        else:
            proyectos[tarea]["responsable"] = responsable
            print("Tarea asignada a ",responsable)

    # Actualizar la tarea existente
    elif numero_seleccionado == 3:
        tarea = input("Introduce una tarea existente: ")

        # Si la tarea no existe
        if tarea not in proyectos:
            print("La tarea no existe")

        # Introduce la nueva descripcion de la tarea existente
        else:
            nueva_descripcion = input("Introduce la nueva descripción: ")
            proyectos[tarea]["descripcion"] = nueva_descripcion
            print("Descripcion de la tarea existente actualizada")

    # Mostrar la lista completa de tareas y responsables
    elif numero_seleccionado == 4:
        for tarea, detalles in proyectos.items():
             print(f"{tarea} - Descripción: {detalles['descripcion']}, Responsable: {detalles['responsable']}")

    # Fin del programa
    else:
        continuar = False
        break