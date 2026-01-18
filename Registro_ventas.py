# Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
# de tus productos. Cada producto tiene un nombre y una cantidad
# vendida. Implementa un programa en Python que utilice un diccionario
# para almacenar la información de las ventas. El programa debe permitir
# registrar las ventas de productos, actualizar la cantidad vendida de un
# producto existente y calcular el total de ventas diarias.

tienda = {}

productos = {'manzanas': 5, 'naranjas': 3, 'platanos': 8}

# Registrar ventas de productos
for producto, cantidad in productos.items():
    if producto in tienda:
        tienda[producto] += cantidad
    else:
        tienda[producto] = cantidad
print("Ventas registradas:", tienda)

# Actualizar cantidad vendida de un producto existente
producto_a_actualizar = 'naranjas'
nueva_cantidad = 7
if producto_a_actualizar in tienda:
    tienda[producto_a_actualizar] = nueva_cantidad
    print(f"Cantidad actualizada de {producto_a_actualizar}: {tienda[producto_a_actualizar]}")
else:
    print(f"El producto {producto_a_actualizar} no existe en el registro de ventas.")

# Calcular el total de ventas diarias
total_ventas = sum(tienda.values())
print("Total de ventas diarias:", total_ventas)