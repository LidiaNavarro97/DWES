# La ficha de producto de la parte PHP mostraba nombre, precio, unidades y disponible. 
# Replica esa salida en Python con una f-string y el formato :.2f para el precio.

nombre = input("Dime un nombre: ")
precio = float(input("Dime un precio: "))
unidades = int(input("Dime las unidades: "))
disponible = bool(input("¿Está disponible?: (si/no) "))

print(f"Nombre: {nombre} - Precio: {precio}€ - Unidades: {unidades:.2f} uds - Disponible: {disponible}")