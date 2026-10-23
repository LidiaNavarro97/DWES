# Provoca un TypeError con "3" + 4 y un ValueError con int("2.5"). 
# Lee los mensajes completos: ¿qué información os dan (tipo de error, línea, causa)?

num1 = "3" + 4 # --> TypeError: can only concatenate str (not "int") to str
# Me da un error de que no se puede concatenar porque es string y no int

num2 = int("2.5") # --> ValueError: invalid literal for int() with base 10: '2.5'
# Me da un error de que int es invalido porque tiene decimales

