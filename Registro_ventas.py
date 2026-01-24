# Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
# de tus productos. Cada producto tiene un nombre y una cantidad
# vendida. Implementa un programa en Python que utilice un diccionario
# para almacenar la información de las ventas. El programa debe permitir
# registrar las ventas de productos, actualizar la cantidad vendida de un
# producto existente y calcular el total de ventas diarias.

# Lista vacia de la tienda (despues se añadira los productos de la tienda)
tienda = {}

continuar = True

while continuar:
    print("\n--- TIENDA DE FRUTAS Y VERDURAS ---")
    print("1. Registrar ventas de productos")
    print("2. Actualizar cantidad vendida de un producto")
    print("3. Calcular total de ventas")
    print("4. Ver productos registrados")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    # 1️⃣ Registrar ventas
    if opcion == "1":
        producto = input("Nombre del producto: ").lower()
        cantidad = int(input("Cantidad vendida: "))

        if producto in tienda:
            tienda[producto] += cantidad
        else:
            tienda[producto] = cantidad

        print(f"Venta registrada. {producto}: {tienda[producto]}")

    # 2️⃣ Actualizar producto existente
    elif opcion == "2":
        producto = input("Producto a actualizar: ").lower()

        if producto in tienda:
            nueva_cantidad = int(input("Nueva cantidad vendida: "))
            tienda[producto] = nueva_cantidad
            print("Cantidad actualizada.")
        else:
            print("Ese producto no existe en el registro.")

    # 3️⃣ Calcular total
    elif opcion == "3":
        total = sum(tienda.values())
        print(f"Total de ventas del día: {total}")

    # 4️⃣ Mostrar productos
    elif opcion == "4":
        if tienda:
            print("Ventas registradas:")
            for p, c in tienda.items():
                print(f"{p}: {c}")
        else:
            print("No hay ventas registradas.")

    # 5️⃣ Salir
    elif opcion == "5":
        continuar = False
        print("Saliendo del sistema...")

    else:
        print("Opción inválida.")