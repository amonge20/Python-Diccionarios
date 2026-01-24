# Imagina que eres el gerente de recursos humanos de una empresa y
# necesitas gestionar la información de los empleados. Cada empleado
# tiene un nombre, salario y departamento al que pertenece. Implementa
# un programa en Python que permita agregar nuevos empleados,
# actualizar el salario de un empleado existente, mostrar la lista completa
# de empleados y calcular el promedio salarial por departamento.

# Lista vacia de empleados
empleados = {}
continuar = True

# Menu interactivo para gestionar la empresa
while continuar == True:
    print("--- GESTION DE EMPLEADOS ---")
    print("1. Agregar nuevos empleados")
    print("2. Actualizar el salario de un empleado existente")
    print("3. Mostrar la lista completa de empleados")
    print("4. Calcular el promedio salarial por departamento")
    print("5. Salir")

    opcion = int(input("Selecciona una opcion: "))
   
    # Agregar nuevos empleados
    if opcion == 1:
        nombre = input("Introduce el nombre del trabajador: ")
        salario = float(input("Introduce el salario: "))
        departamento = input("Introduce el departamento en que esta el trabajador: ")
        # Se añade en la lista de empleados
        empleados[nombre] = (salario, departamento)
        print("Empleado registrado")

    # Actualizar el salario de un empleado existente
    elif opcion == 2:
        if not empleados:
            print("No hay empleados")
        else: 
            empleado_existente = input("Introduce a un empleado existente: ")

            # Si el empleado existe
            if empleado_existente in empleados:
                salario_actualizado = float(input("Actualiza el sueldo del empleado: "))
                departamento = empleados[empleado_existente][1] # mantenemos el mismo departamento
                empleados[nombre] = (salario_actualizado, departamento) # Actualizamos el sueldo del empleado del departamento en el que esta
                print("Sueldo actualizado")
            else:
                print("El empleado no existe")    

    # Mostrar la lista completa de los empleados
    elif opcion == 3:
        if not empleados:
            print("No hay empleados")
        else: 
            for empleado, detalles in empleados.items():
                salario, departamento = detalles
                # Mostrando todos los empleados 
                print(f"Empleado {empleado} con el salario de {salario}€ en el departamento {departamento}")

    # Calcular el promedio salarial por departamento 
    elif opcion == 4:
        if not empleados:
            print("No hay empleados")
        else:
            deptos = {}
            for salario, departamento in empleados.values():
                if departamento not in deptos:
                    deptos[departamento] = []
                deptos[departamento].append(salario)

                print("Promedio salarial por departamento:")
                for depto, salarios in deptos.items():
                    promedio = sum(salarios) / len(salarios)
                    print(f"{depto}: {promedio:.2f}€")

    # Fin del programa
    else:
        print("Saliendo de la empresa...")
        continuar = False
        break