"""Módulo con funciones estadísticas sencillas."""


def media(lista: list[float]) -> float:
    """
    Devuelve la media de una lista de números.
    """
    # Sumamos todos los valores con un bucle
    suma = 0
    for numero in lista:
        suma += numero

    # Dividimos la suma entre la cantidad de elementos
    return suma / len(lista)


def limites(lista: list[float]) -> tuple[float, float]:
    """
    Devuelve el mínimo y el máximo de una lista de números.
    """
    # Empezamos suponiendo que el primero es a la vez el mínimo y el máximo
    minimo = lista[0]
    maximo = lista[0]

    # Recorremos la lista y vamos actualizando el mínimo y el máximo
    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero

    # Devolvemos las dos cosas juntas, en una tupla
    return (minimo, maximo)