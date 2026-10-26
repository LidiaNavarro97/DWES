# Escribe un programa que cuente palabras: 
# pide frases hasta que se introduzca una línea vacía y 
# acumula en un diccionario cuántas veces aparece cada palabra 
# (ayuda: frase.split() y palabras.get(palabra, 0))

TODO

palabras = {}

frase = input("Escribe una frase: ")

while frase != "":
    frase_separada = frase.split()

    for palabra in frase_separada:
        palabras[palabra] = palabras.get(palabra, 0) + 1

    frase = input("Escribe una frase: ")

print(palabras)
