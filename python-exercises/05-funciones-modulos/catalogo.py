# Añade a catalogo.py la función productos_agotados(catalogo) 
# y haz que tienda.py ordene el catálogo por precio con sorted y una lambda. 
# Añade el guard de __name__ a ambos archivos y comprobad qué se ejecuta en cada caso.

catalogo = [
    {"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
    {"nombre": "Lápiz", "precio": 0.8, "stock": 0},
    {"nombre": "Mochila", "precio": 18.9, "stock": 3},
]


def productos_agotados(catalogo):
    """Devuelve una lista con los productos cuyo stock es 0."""
    agotados = []  # Aqui guardo los productos agotados
    for producto in catalogo:  # recorro cada producto del catálogo
        if producto["stock"] == 0:  #sino queda stock, lo añado a la list
            agotados.append(producto)  
    return agotados  


# Este bloque solo se ejecuta si lanzo este archivo archivo directamente
# si desde otro archivo hago "import catalogo", no se ejecuta
if __name__ == "__main__":
    
    print("Ejecutando catalogo.py directamente")
    print("Agotados:", productos_agotados(catalogo))