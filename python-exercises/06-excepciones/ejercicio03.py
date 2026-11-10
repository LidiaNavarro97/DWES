# Añade validación con raise a aplicar_descuento: 
# además del porcentaje, el precio debe ser positivo. 
# Escribe después las llamadas que provoquen cada error y captúralas por separado.

# aplicar_descuento con validación mediante raise, y llamadas que provocan cada error.


def aplicar_descuento(precio: float, porcentaje: float) -> float:
    """
    Devuelve el precio una vez aplicado el descuento.
    """
    # el precio tiene que ser positivo
    if precio <= 0:
        raise ValueError("El precio debe ser positivo")

    # el porcentaje tiene que estar entre 0 y 100
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")

    # Si todo es válido, calculamos el precio final
    return precio * (1 - porcentaje / 100)


# Llamada correcta, para comprobar que sigue funcionando
print("Precio final:", aplicar_descuento(50, 20))

# Llamada que provoca el error del precio, capturada por separado
try:
    aplicar_descuento(-10, 20)
except ValueError as error:
    print("Error de precio:", error)

# Llamada que provoca el error del porcentaje, capturada por separado
try:
    aplicar_descuento(50, 150)
except ValueError as error:
    print("Error de porcentaje:", error)