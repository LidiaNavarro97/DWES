# Predice el tipo de excepción de cada expresión antes de probarla en el intérprete: 
# int("3.5"), [1, 2][5], {}["x"], "a" + 1, 1 / 0, float("1,5") 
# (esta última tiene trampa: pensad en el separador decimal).

int("3.5") # ValueError
[1, 2][5] # IndexError
{}["x"] # KeyError
"a" + 1 # TypeError
1 / 0 # ZeroDivisionError
float("1,5") # ValueError