# diccionario de grupos
grupos = {
    "chirigotas": {
        "Los Yesterday": {
            "preliminares": [9.1, 9.3, 9.0, 9.2],
            "cuartos": [9.4, 9.2, 9.1, 9.3],
            "semifinal": [9.6, 9.5, 9.4, 9.5],
            "final": [9.7, 9.6, 9.8, 9.7]
        },
        "Er Chele Vara": {
            "preliminares": [8.5, 8.6, 8.7, 8.9],
            "cuartos": [8.9, 8.8, 8.6, 8.7]
        }
    },
    "comparsas": {
        "Los Ángeles Caídos": {
            "preliminares": [9.5, 9.6, 9.7, 9.8],
            "cuartos": [9.7, 9.6, 9.8, 9.9],
            "semifinal": [9.8, 9.9, 9.8, 9.9],
            "final": [9.9, 9.9, 9.8, 9.8]
        },
        "Los Millonarios": {
            "preliminares": [9.3, 9.4, 9.5, 9.6],
            "cuartos": [9.6, 9.5, 9.7, 9.8],
            "semifinal": [9.7, 9.6, 9.7, 9.8]
        }
    },
    "coros": {
        "La Trinidad": {
            "preliminares": [9.0, 9.1, 9.2, 9.3],
            "cuartos": [9.3, 9.4, 9.5, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.8],
            "final": [9.7, 9.8, 9.9, 9.8]
        },
        "El Batallón Fletilla": {
            "preliminares": [8.8, 8.9, 9.0, 9.1],
            "cuartos": [9.0, 9.1, 9.2, 9.3],
            "semifinal": [9.2, 9.3, 9.4, 9.5]
        }
    },
    "cuartetos": {
        "Tres notas Musicales": {
            "preliminares": [9.2, 9.3, 9.1, 9.4],
            "cuartos": [9.4, 9.5, 9.3, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.6],
            "final": [9.7, 9.8, 9.6, 9.7]
        },
        "Ser o no Ser": {
            "preliminares": [8.7, 8.8, 8.9, 8.6],
            "cuartos": [8.9, 9.0, 8.8, 8.9]
        }
    }
}

# CASO 1. Calcular las medias de todas las agrupaciones

# 1. Reecorre todas las modalidades y agrupaciones
#for modalidades, agrupaciones in grupos.items():

# 2. Calcula la media de las puntuaciones de cada fase en la que haya participado la agrupacion
def media(lista): #media de una fase
    """ suma de los elementos dividido entre cuantos hay"""
    return sum(lista) / len(lista)

def redondea(puntuacion): # lo hago para q me ayude para luego
    """ redondea una puntuacion a dos decimales"""    
    return round(puntuacion, 2)

# media de las puntuaciones de una fase
# extra son las notas adicionales, que sino se las doy pues salen vacias
def media_fase(puntuaciones, extra=()): 
    todas = list(puntuaciones) + list(extra) #las convierto en listas y las junto en una lista nueva
    redondeadas = list(map(redondea, todas)) # aplica redondea a cada nota de todas y luego lo convierto en lista
    return media(redondeadas) #calculo la media de las ntas ya redondeadas y lo devuelvo

# 3. Calcula la media general de la agrupacion a partir de las medias de sus fases
# dando el mismo peso a cada fase
def media_general(fases):
    medias = []
    for puntuaciones in fases.values():
        medias.append(media_fase(puntuaciones))
    return media(medias)    
