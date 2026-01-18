# Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
# estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
# una lista de fechas en las que asistió a clases. Implementa un programa
# en Python que utilice un diccionario para almacenar la información de las
# asistencias. El programa debe permitir registrar la asistencia de los
# estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
# estudiantes y las fechas en las que asistieron.

asistencias = {}

# Asistencia de los estudiantes
registro_asistencias = {'Alice': ['2024-01-10', '2024-01-12'], 'Bob': ['2024-01-11'], 'Charlie': ['2024-01-10', '2024-01-11', '2024-01-12']}

# Registrar asistencia de los estudiantes
for estudiante, fechas in registro_asistencias.items():
    asistencias[estudiante] = fechas
print("Asistencias registradas:", asistencias)
# Agregar nuevas fechas de asistencia
estudiante_a_actualizar = 'Bob'
nueva_fecha = '2024-01-12'
if estudiante_a_actualizar in asistencias:
    asistencias[estudiante_a_actualizar].append(nueva_fecha)
    print(f"Fechas de asistencia actualizadas de {estudiante_a_actualizar}: {asistencias[estudiante_a_actualizar]}")
else:
    print(f"El estudiante {estudiante_a_actualizar} no existe en el registro de asistencias.")
# Mostrar la lista de estudiantes y las fechas en las que asistieron
print("Lista completa de asistencias:")
for estudiante, fechas in asistencias.items():
    print(f"{estudiante}: Fechas de asistencia: {', '.join(fechas)}")
    