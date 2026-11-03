# Escribe un programa que pida base y altura de una habitación 
# y muestre su superficie con dos decimales usando una f-string.

base = float(input("Escriba la base de la habitacion: "))
altura = float(input("Escriba la altura de la habitacion: "))

superficie = round(base * altura, 2) 

print(f"La superficie de la habitacion seria: {superficie}")