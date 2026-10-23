# Experimenta con len, upper e in sobre la cadena "Desarrollo Web en Entorno Servidor": 
# ¿cuántos caracteres tiene? 
# ¿Está "web" dentro? 
# ¿Y con "web" in cadena.lower()? 
# Explica la diferencia entre las dos últimas comprobaciones.

cadena = "Desarrollo Web en Entorno Servidor"

print("Caracteres: ", len(cadena)) # --> Tiene 34 caracteres
print("web" in cadena.upper()) # --> False, porque la estoy poniendo en mayúsculas
print("web" in cadena.lower()) # --> True, porque está en minúsculas
