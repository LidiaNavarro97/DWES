import pprint

def redondear_puntuacion(puntuacion):
    """
    Redondear una puntuacion numerica a dos decimales
    """
    return round(puntuacion, 2)

def calcular_media_puntuaciones(puntuaciones):
    """
    Calcular la media de una lista de puntuaciones.
    """
    puntuaciones_redondeadas = list(map(redondear_puntuacion, puntuaciones))
    return sum(puntuaciones_redondeadas) / len(puntuaciones_redondeadas)


def calcula_media_puntuaciones(grupos, *puntuaciones_extra, ag=None, fase=None):

    if fase is not None and ag is None:
        raise ValueError("Debes indicar una agrupacion para consultar una fase")

    if puntuaciones_extra and (ag is None or fase is None):
        raise ValueError("Las puntuaciones extra requieren agrupacion y fase")
    
    resultado = {}

    for modalidad, agrupaciones in grupos.items():
        #print(f"=== MODALIDAD {modalidad} ===\n")
        for nombre, fases in agrupaciones.items():
            if ag is not None and nombre != ag:
                continue

            if fase is None:
                medias_fases = []
                for nombre_fase, puntuaciones in fases.items():
                    #print(f"=== FASE {nombre_fase} ===\n")
                    media_fase = calcular_media_puntuaciones(puntuaciones)
                    medias_fases.append(media_fase)
                    #print(f"MEDIA DE LA FASE {nombre_fase}: {media_fase}")
                media = sum(medias_fases) / len(medias_fases)
                #print(f"MEDIA DE LAS FASES {media}")
            else:
                # Crear una lista nueva para no modificar la original
                puntuaciones = fases[fase] + list(puntuaciones_extra)
                media = calcular_media_puntuaciones(puntuaciones)    

            if modalidad not in resultado:
                resultado[modalidad] = {}
            resultado[modalidad][nombre] = round(media, 2)
    
    return resultado                











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


# ------------------ EN CLASE ---------------------

print(" =======RESULTADOS DEL CONCURSO======= \n")


print("\nCASO A -> CALCULAR MEDIA DE LAS AGRUPACIONES\n")
pprint.pprint(calcula_media_puntuaciones(grupos))

print("\nCASO B -> MEDIA GENERAL DE UNA AGRUPACION\n")
pprint.pprint(calcula_media_puntuaciones(grupos, ag="Los Yesterday"))

print("\nCASO C -> CALCULAR LA MEDIA DE UNA FASE CONCRETA\n")
pprint.pprint(calcula_media_puntuaciones(grupos, ag="Los Yesterday", fase="final"))

print("\nCASO D -> INCORPORAR PUNTUACIONES ADICIONALES MEDIANTE *ARGS \n")
pprint.pprint(calcula_media_puntuaciones(grupos, 9.876, 9.944, ag="Los Yesterday", fase="final"))

