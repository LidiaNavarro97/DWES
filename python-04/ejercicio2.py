# Sobre la lista dias de la sección de slicing, obtén con porciones: 
# los dos primeros días, 
# los dos últimos, 
# los días en posiciones pares y 
# una copia completa. 
# Comprueba que la copia es independiente modificándola.

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sabado", "domingo" ]

print("Imprimir los dos primeros días.")
print(dias[0:2])

print("------------------------------------")

print("Imprimir los dos últimos días")
print(dias[-2:])

print("------------------------------------")

print("Imprimir los días en posiciones pares.")
print(dias[1::2])

print("------------------------------------")

print("Una copia completa.")
lista_nueva_dias = dias[:]
print(lista_nueva_dias)

print("------------------------------------")

print("Comprobar que la lista es independiente borrando el ultimo dia.")
lista_nueva_dias.pop()
print()
print("Lista nueva: ")
print(lista_nueva_dias)
print("Lista antigua: ")
print(dias)


