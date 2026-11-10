# Ejercicio 1: Análisis de vinos de Jerez


# 1. Define una función que reciba como parámetro una lista de nombres de vinos.
# 2. La función debe generar un diccionario en el que:
# 3. Las claves sean los nombres de los vinos.
# 4. Los valores sean True si el nombre contiene "Sherry" y False en caso contrario.
# 5. Utiliza la función incorporada filter() de Python para obtener una segunda lista que contenga únicamente los vinos cuyo nombre incluya "Sherry".
# 6. La búsqueda no debe distinguir entre mayúsculas y minúsculas. Por ejemplo, "SHERRY", "sherry" y "ShErry" deben considerarse equivalentes.
# 7. La función debe devolver el diccionario y la lista filtrada.
# 8. Incluye una docstring que documente el propósito de cada función, sus parámetros y los valores que devuelve.

def contiene_vinos(vino):
    return "sherry" in vino.lower()

def lista_vinos(vinos):

    """ Aquí va el docstring """
    
    diccionario_vinos = {vino: contiene_vinos(vino) for vino in vinos}
    vinos_con_sherry = list(filter(contiene_vinos, vinos))

    return diccionario_vinos, vinos_con_sherry

if __name__ == '__main__':

    vinos_jerez = [
    "Sherry Classic",
    "Vino Blanco",
    "Fino SHERRY",
    "Moscatel",
    "ShErry Cream"
    ]

    diccionario_vinos, vinos_con_sherry = lista_vinos(vinos_jerez)
    print("Dicionario de vinos: ", diccionario_vinos)    
    print("Lista de vinos con 'Sherry': ", vinos_con_sherry)    
