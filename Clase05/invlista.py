def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida = [e] + invertida  #agrego el elemento e al principio de la lista invertida
    return invertida

print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
