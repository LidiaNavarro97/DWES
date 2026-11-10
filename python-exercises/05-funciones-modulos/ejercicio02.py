# Escribe pedir_dato(mensaje, defecto) que pida un valor por teclado y 
# devuelva el valor tecleado o defecto si se pulsa Intro (pista: comparar con "").

def pedir_dato(mensaje: str, defecto: str) -> str:
    """
    Pide un valor por teclado.
    """
    # Mostramos el mensaje y guardamos lo que teclea el usuario
    valor = input(mensaje)

    if valor == "":
        return defecto

    # Si escribió algo, devolvemos ese valor
    return valor


# Pruebo la funcion
nombre = pedir_dato("Tu nombre (Intro para 'Anónimo'): ", "Anónimo")
print("Hola,", nombre)