# Crea una lista con las compras de un proyecto: 
# añade, sustituye y elimina elementos usando cada método visto 
# (append, insert, remove, pop, del). 
# Muestra la lista tras cada operación

frutas = ["manzanas","peras","platanos","fresas"]

print("Catalogo frutas:")
print(frutas)

print("--------------------------")

print("Añadir una fruta nueva.")
frutas.append("uvas")
print(frutas)

print("--------------------------")

print("Insertar una fruta nueva en una posición: ")
frutas.insert(0,"naranjas")
print(frutas)

print("--------------------------")

print("Borrar una fruta elegida. ")
frutas.remove("platanos")
print(frutas)

print("--------------------------")

print("Te borra el ultimo elemento y te lo devuelve.")
frutas.pop()
print(frutas)

print("--------------------------")

print("Eliminar una fruta en una posición específica.")
del frutas[0]
print(frutas)

