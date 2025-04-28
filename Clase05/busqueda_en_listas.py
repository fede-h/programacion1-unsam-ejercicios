def buscar_u_elemento(lista, elemento):
    'Recibe una lista y un elemento y devuelve la última aparición del elemento'

    pos = -1
    for x, y in enumerate(lista):
        if y == elemento:
            pos = x
    return pos

def buscar_n_elemento(lista, elemento):
    'Recibe una lista y cuenta el número de veces que aparece el elemento'

    count = 0
    for x in lista:
        if x == elemento: count += 1
    return count

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el primer elemento
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def minimo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el primer elemento
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m
