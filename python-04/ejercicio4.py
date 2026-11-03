# A partir del catalogo de ejemplo, muestra: 
# la lista de nombres con stock agotado, 
# el precio medio y el producto más caro 
# (con max y un bucle, sin funciones todavía).

catalogo = [
{"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
{"nombre": "Lápiz", "precio": 0.8, "stock": 0},
{"nombre": "Mochila", "precio": 18.9, "stock": 3},
]


# Lista de nombres con stock agotado
agotados = []

for producto in catalogo:
    if producto["stock"] == 0:
        agotados.append(producto["nombre"])

print("Productos agotados:", agotados)


# Calcular el precio medio
suma_precios = 0

for producto in catalogo:
    suma_precios += producto["precio"]

precio_medio = suma_precios / len(catalogo)

print("Precio medio:", precio_medio)


# Encontrar el producto más caro con max()
precios = []

for producto in catalogo:
    precios.append(producto["precio"])

precio_maximo = max(precios)

for producto in catalogo:
    if producto["precio"] == precio_maximo:
        print("Producto más caro:", producto["nombre"])
        print("Precio:", producto["precio"])