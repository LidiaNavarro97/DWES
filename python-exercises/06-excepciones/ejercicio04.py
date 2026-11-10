# Con el catálogo de la página 4, escribe buscar_producto(catalogo, nombre) 
# que devuelva el diccionario o lance ValueError("Producto no encontrado"). 
# Captura el error en el programa principal y muéstralo amablemente.

# Búsqueda de un producto en el catálogo, con ValueError si no existe.

catalogo = [
    {"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
    {"nombre": "Lápiz", "precio": 0.8, "stock": 0},
    {"nombre": "Mochila", "precio": 18.9, "stock": 3},
]


def buscar_producto(catalogo: list[dict], nombre: str) -> dict:
    """
    Busca un producto por su nombre y devuelve su diccionario.
    """
    # Recorremos el catálogo producto a producto
    for producto in catalogo:
        # Si el nombre coincide, devolvemos el producto y la función termina
        if producto["nombre"] == nombre:
            return producto

    # Si el bucle termina sin encontrarlo, lanzamos el error
    raise ValueError("Producto no encontrado")


# Programa principal
nombre = input("¿Qué producto buscas? ")

try:
    producto = buscar_producto(catalogo, nombre)
    print(f"{producto['nombre']}: {producto['precio']} € ({producto['stock']} en stock)")
    
except ValueError as error:
    # Mostramos el error
    print(f"Lo sentimos, no tenemos «{nombre}» en el catálogo. ({error})")