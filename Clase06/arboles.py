import os
import matplotlib.pyplot as plt
from csv import reader
import numpy as np

def leer_arboles(nombre_archivo):
    'Devuelve una lista de dicts'

    file = open(nombre_archivo)
    filas = reader(file)
    encabezados = next(filas)

    arboleda = []
    for fila in filas:
        arboleda.append(dict(zip(encabezados, fila)))
    
    return arboleda

def medidas_de_especies(arboleda, especies):
    'Devuelve un diccionario con las medidas de las especies'

    if isinstance(especies, str):
        especies = [especies]

    medidas_de_especies = np.array([
    [int(arbol['altura_tot']), 
    int(arbol['diametro']),
    especies.index(arbol['nombre_com'])]
    for arbol in arboleda 
    for especie in especies
    if arbol['nombre_com'] == especie])

    return medidas_de_especies

def scatter_hd(lista_de_pares):
    'Realiza un scatterplot entre altura y diámetro'

    h = lista_de_pares[:, 0]
    d = lista_de_pares[:, 1]
    s = lista_de_pares[:, 2]

    plt.scatter(d, h, alpha = 0.3, c = s)
    plt.xlabel('Diámetro [cm]')
    plt.ylabel('Alto [m]')
    plt.title(f'Relación diámetro-alto de arboles')
    plt.show()

nombre_archivo = os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)

altos = [int(arbol['altura_tot']) for arbol in arboleda]

# plt.hist(altos, bins = 20)

medidas_jacaranda = medidas_de_especies(arboleda, ['Eucalipto', 'Palo borracho rosado', 'Jacarandá'])

scatter_hd(medidas_jacaranda)