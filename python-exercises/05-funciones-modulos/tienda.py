# Añade a catalogo.py la función productos_agotados(catalogo) 
# y haz que tienda.py ordene el catálogo por precio con sorted y una lambda. 
# Añade el guard de __name__ a ambos archivos y comprobad qué se ejecuta en cada caso.


#importo la funcion de catalogo
from catalogo import catalogo, productos_agotados


def ordenar_por_precio(catalogo):
    """Devuelve una lista nueva ordenada de menor a mayor precio."""
    # sorted crea una lista nueva, no modifica la orginial

    return sorted(catalogo, key=lambda producto: producto["precio"])


# Este bloque solo se ejecuta si lanzo este archivo archivo directamente
# si desde otro archivo hago "import tieda", no se ejecuta

if __name__ == "__main__":

    print("Ejecutando tienda.py directamente")

    for producto in ordenar_por_precio(catalogo):  # Recorremos ya ordenados
        print(producto["nombre"], "-", producto["precio"], "€")
        
    print("Agotados:", productos_agotados(catalogo))