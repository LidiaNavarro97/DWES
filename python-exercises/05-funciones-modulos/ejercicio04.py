# Investiga en el intérprete: 
# import random, luego help(random.randint) y help(random.choice). 
# Úsalos para simular 100 tiradas de un dado y 
# contar cuántos seises salen con un diccionario contador.

import random

# Cada cara del dado empieza con 0 apariciones
contador = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for tirada in range(100):
    # Número entre 1 y 6, ambos incluidos
    cara = random.randint(1, 6)
    # Sumamos 1 al contador de esa cara
    contador[cara] += 1

print("Resultado de las 100 tiradas:", contador)
print("Seises:", contador[6])