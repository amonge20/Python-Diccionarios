# Eres un gerente de proyectos y necesitas un programa para administrar
# las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
# una descripción y un responsable asignado. Implementa un programa en
# Python que utilice un diccionario para almacenar la información de las
# tareas. El programa debe permitir agregar nuevas tareas, asignar
# responsables a las tareas existentes, actualizar las descripciones de las
# tareas y mostrar la lista completa de tareas y responsables. 

proyectos = {}

# Agregar nuevas tareas
Agregar_tareas = {'Tarea 1': {'descripcion': 'Diseñar el logo', 'responsable': 'Ana'},
                  'Tarea 2': {'descripcion': 'Desarrollar la web', 'responsable': 'Luis'},
                  'Tarea 3': {'descripcion': 'Crear contenido', 'responsable': 'Marta'}
                  }

# Registrar tareas en el diccionario de proyectos
for tarea, detalles in Agregar_tareas.items():
    proyectos[tarea] = detalles
print("Tareas registradas:", proyectos)

# Asignar responsables a las tareas existentes
tarea_a_asignar = 'Tarea 2'
nuevo_responsable = 'Carlos'
if tarea_a_asignar in proyectos:
    proyectos[tarea_a_asignar]['responsable'] = nuevo_responsable
    print(f"Responsable actualizado de {tarea_a_asignar}: {proyectos[tarea_a_asignar]['responsable']}")
else:
    print(f"La tarea {tarea_a_asignar} no existe en el registro de proyectos.")

# Actualizar descripciones de las tareas
tarea_a_actualizar = 'Tarea 1'
nueva_descripcion = 'Diseñar el logo corporativo'
if tarea_a_actualizar in proyectos:
    proyectos[tarea_a_actualizar]['descripcion'] = nueva_descripcion
    print(f"Descripción actualizada de {tarea_a_actualizar}: {proyectos[tarea_a_actualizar]['descripcion']}")
else:
    print(f"La tarea {tarea_a_actualizar} no existe en el registro de proyectos.")
    
# Mostrar la lista completa de tareas y responsables
print("Lista completa de tareas y responsables:")
for tarea, detalles in proyectos.items():
    print(f"{tarea}: Descripción: {detalles['descripcion']}, Responsable: {detalles['responsable']}")