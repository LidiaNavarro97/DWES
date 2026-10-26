# Escribe un programa que pida una nota entera (0-10) 
# y muestre la calificación con elif: 
# Insuficiente (< 5), 
# Suficiente (5-6), 
# Bien (7), 
# Notable (8-9) y 
# Sobresaliente (10). 
# Añade después el mismo reparto con expresiones condicionales 
# en una sola línea, para comparar legibilidad.

nota_entera = int(input("Introduce una nota del 0 al 10: "))

#if nota_entera < 5 :
#    print("Insuficiente")
#elif 5 <= nota_entera <= 6: 
#    print("Suficiente")
#elif nota_entera == 7:
#    print("Bien")
#elif 8 <= nota_entera <= 9:
#    print("Notable")
#elif nota_entera == 10:
#    print("Sobresaliente")

print("Insuficiente") if nota_entera < 5 else print("Suficiente") if 5 <= nota_entera <= 6 else print("Bien") if nota_entera == 7 else print("Notable") if 8 <= nota_entera <= 9 else print("Sobresaliente") if nota_entera == 10 else print("Nota invalida")
