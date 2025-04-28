from pprint import pprint


def leer_parque(nombre_archivo, parque):
    'Devuelve una lista de dicts'
    from csv import reader
    file = open(nombre_archivo)
    filas = reader(file)
    encabezados = next(filas)

    lista = []
    #for fila in filas:
    for fila in filas:
        if fila[-7] == parque.upper():
            lista.append(dict(zip(encabezados, fila)))
    
    return lista


def especies(lista_arboles):
    'Devuelve las especies de la lista'
    conjunto = set([])

    for arbol in lista_arboles:
        if arbol['nombre_com'] not in conjunto:
            conjunto.add(arbol['nombre_com'])
    
    return conjunto


def contar_ejemplares(lista_arboles):
    'Devuelve frecuencias de arboles'
    from collections import Counter

    tenencias = Counter()
    for arbol in lista_arboles:
        tenencias[arbol['nombre_com']] += 1
    
    return tenencias


def obtener_alturas(lista_arboles, especie):
    'Devuelve una lista con las alturas para la especie'
    alturas = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
    
    return alturas


def obtener_inclinaciones(lista_arboles, especie):
    'Devuelve una lista con las inclinaciones para la especie'
    inclinaciones = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(float(arbol['inclinacio']))
    
    return inclinaciones


def especimen_mas_inclinado(lista_arboles):
    'Devuelve el espécimen más inclinado'
    
    mas_inclinado = ['especie', 0]
    for arbol in lista_arboles:
        if int(arbol['inclinacio']) > mas_inclinado[1]:
            mas_inclinado = [arbol['nombre_com'], int(arbol['inclinacio'])]
        else: pass
    
    return tuple(mas_inclinado)


def especie_promedio_mas_inclinada(lista_arboles):
    'Devuelve la esp. prom. más inclinada de la lista'
    inclinaciones = {}
    promedios = {}

    for arbol in lista_arboles:
        try:
            inclinaciones[arbol['nombre_com']].append(int(arbol['inclinacio']))
        except KeyError:
            inclinaciones[arbol['nombre_com']] = [(int(arbol['inclinacio']))]

    for k, v in inclinaciones.items():
        promedios[k] = round((sum(v) / len(v)), 2)
    
    especie_mas_inclinada = max(promedios, key=promedios.get)
    
    return (especie_mas_inclinada, promedios[especie_mas_inclinada])


listota = leer_parque('Data/arbolado-en-espacios-verdes.csv', 'general paz')

#listita = especies(listota)

# print('General Paz: '+ str(contar_ejemplares(leer_parque('ejercicios_python/Data/arbolado-en-espacios-verdes.csv','general paz')).most_common(5))+'\n')
# print('Los Andes: '+ str(contar_ejemplares(leer_parque('ejercicios_python/Data/arbolado-en-espacios-verdes.csv','andes, los')).most_common(5))+'\n')
# print('Centenario: '+ str(contar_ejemplares(leer_parque('ejercicios_python/Data/arbolado-en-espacios-verdes.csv','centenario')).most_common(5))+'\n')

# h_gral_paz = obtener_alturas(listota, 'Jacarandá')
# h_los_andes = obtener_alturas(leer_parque('ejercicios_python/Data/arbolado-en-espacios-verdes.csv','andes, los'), 'Jacarandá')
# h_centenario = obtener_alturas(leer_parque('ejercicios_python/Data/arbolado-en-espacios-verdes.csv','centenario'), 'Jacarandá')
# print(f'Gral. Paz\nMax: {max(h_gral_paz)}, Prom: {round(sum(h_gral_paz)/len(h_gral_paz), 2)}')
# print(f'Los Andes\nMax: {max(h_los_andes)}, Prom: {round(sum(h_los_andes)/len(h_los_andes), 2)}')
# print(f'Centenario\nMax: {max(h_centenario)}, Prom: {round(sum(h_centenario)/len(h_centenario), 2)}')

#print(obtener_inclinaciones(listota, 'Jacarandá'))

#print(especimen_mas_inclinado(listota))

#print(especie_promedio_mas_inclinada(leer_parque('ejercicios_python/Data/arbolado-en-espacios-verdes.csv', 'andes, los')))