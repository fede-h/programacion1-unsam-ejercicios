from csv import reader


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

    medidas_de_especies = {especie : 
    ([(float(arbol['altura_tot']), float(arbol['diametro']))
    for arbol in arboleda 
    if arbol['nombre_com'] == especie])
    for especie in especies}

    return medidas_de_especies

arboleda = leer_arboles('Data/arbolado-en-espacios-verdes.csv')

altos_jacaranda = [float(arbol['altura_tot']) 
for arbol in arboleda 
if arbol['nombre_com'] == 'Jacarandá']

tronco_jacaranda = [(float(arbol['altura_tot']), float(arbol['diametro'])) 
for arbol in arboleda 
if arbol['nombre_com'] == 'Jacarandá']

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

medidas_para_especie = {especie : ([(float(arbol['altura_tot']), float(arbol['diametro']))
    for arbol in arboleda if arbol['nombre_com'] == especie]) for especie in especies}
