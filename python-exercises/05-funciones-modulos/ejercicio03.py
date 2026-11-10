# Crea el módulo estadistica.py con una función media(lista) 
# y otra limites(lista) que devuelva la tupla (minimo, maximo). 
# Desde un programa de prueba, importa el módulo, 
# calcula la media y usa los límites para obtener el rango (máximo menos mínimo).


# Importo el módulo
import estadistica

notas = [7.5, 4.0, 9.0, 6.5, 8.0]

# Calculamos la media llamando a la función del módulo
promedio = estadistica.media(notas)
print("Media:", promedio)

# limites() devuelve una tupla, q la divido en dos
minimo, maximo = estadistica.limites(notas)
print("Mínimo:", minimo)
print("Máximo:", maximo)

# El rango es el máximo menos el mínimo
rango = maximo - minimo
print("Rango:", rango)