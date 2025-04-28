#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El primer error era de tipo SEMÁNICO y estaba ubicado en if expresion[i] == 'a'.
#    Lo corregí cambiando "... == 'a'" por "... in 'aA", comprendiendo también la A (mayúscula)
# El segundo error era de tiempo de ejecución, en la lógica del "if" y el "return False". Evaluaba solo la primer letra y después devolvía un FALSE.
#Codigo corregido:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in 'aA':
            return True
            break
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


# %%
# Ejercicio 3.2
# Errores SINTACTICOS:
#   faltaban los dos puntos despues de definir tiene_a
#   dos puntos después de while i<n
#   = en vez de == en expresion[i] = 'a'
#   dos puntos al final de ... == 'a' 
#   return "Falso" en vez de return False en el final de la función
# Error SEMANTICO al contemplar solo 'a' y no la 'A'
#   se corrigió agregando otra condición de igualdad

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

tiene_a('LA novela 1984 de George Orwell')



# %%
# En esta función había un error de tipo de variable
# Si se le daba un número, no podía procesarlo como string
# Solucioné este problema forzando la variable "expresión"
# Con la función str(expresion)

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


#tiene_uno('UNSAM 2020')
#tiene_uno('La novela 1984 de George Orwell')
tiene_uno(98401)

#%% 
# En esta función hay un error semántico
# La función suma no retorna una variable c calculada
# Se soluciona agragando "return c" al final de la función

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma {a} + {b} da {c}")

# %%
# En la función leer_camion había un error de variable
# La variable registro  = {} se daclaraba afuera de la iteración por fila
# Hacía que el valor registro siempre se agregue con su último valor
# La solución fue definir registro = {} adentro de las iteraciones
# Así se limpia la variable y no se pisa con la iteración anterior

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = (fila[0])
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
# %%
