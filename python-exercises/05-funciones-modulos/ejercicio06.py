# Escribe maximo(*numeros), que devuelva el mayor de los argumentos recibidos y
# lance ValueError("No ha llegado ningún número") si la llaman sin argumentos. 
# Comprueba después que maximo(*[3, 1, 4]) se comporta igual que 
# maximo(3, 1, 4) y explica por qué.


def maximo(*numeros):
    """Devuelve el mayor de los números recibidos."""
    
    if len(numeros) == 0: # sino ha llegado ningún argumento lanzo el error
        raise ValueError("No ha llegado ningún número")  

    mayor = numeros[0]  # supongo que el primero es el mayor
    for numero in numeros:  
        if numero > mayor:  # Si encontramos uno más grande
            mayor = numero  # pasa a ser el nuevo mayor
    return mayor  # Devolvemos el mayor encontrado


# Solo se ejecuta si lanzo este archivo directamente
if __name__ == "__main__":

    print(maximo(3, 1, 4))  # Llamada con argumentos sueltos
    print(maximo(*[3, 1, 4]))  # Llamada desempaquetando una lista con *

    # compruebo que ambas llamadas dan el mismo resultado
    print("Son iguales???", maximo(3, 1, 4) == maximo(*[3, 1, 4]))

    # Probamos la llamada sin argumentos que debe lanzar ValueError
    try:
        maximo()
    except ValueError as error:
        print("Error capturado:", error)