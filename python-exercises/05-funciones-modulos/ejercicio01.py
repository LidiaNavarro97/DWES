# Reescribe como función, con docstring y anotaciones de tipos, 
# la solución del ejercicio 4 de la página anterior (producto más caro del catálogo). 
# Comprueba que help() muestra vuestro docstring.

catalogo = [
    {"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
    {"nombre": "Lápiz", "precio": 0.8, "stock": 0},
    {"nombre": "Mochila", "precio": 18.9, "stock": 3},
]


def producto_mas_caro(catalogo: list[dict]) -> dict | None:
    """
    Devuelve el producto más caro de un catálogo.
    Recorre la lista y se queda con el producto de mayor precio.
    """
    # Si no hay productos, no hay ninguno que sea el más caro
    if len(catalogo) == 0:
        return None

    # Empezamos suponiendo que el primero es el más caro
    mas_caro = catalogo[0]

    # Recorremos el resto de productos
    for producto in catalogo:
        # Si encontramos uno con precio mayor, pasa a ser el más caro
        if producto["precio"] > mas_caro["precio"]:
            mas_caro = producto

    # Devolvemos el producto ganador
    return mas_caro


# Probamos la función
resultado = producto_mas_caro(catalogo)
print("Producto más caro:", resultado["nombre"])
print("Precio:", resultado["precio"])

# Comprobamos que help() muestra el docstring
help(producto_mas_caro)