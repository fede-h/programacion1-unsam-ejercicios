def diccionario(palabras):
    '''Crea un diccionario en geringoso'''
    diccionario = {}
    for palabra in palabras:
        geringoso = ''
        for letra in palabra:
            geringoso += letra
            if letra.lower() in 'aeiou':
                geringoso += 'p' + letra.lower()
        diccionario[palabra] = geringoso

    print('Diccionario geringoso: ')
    for k, v in diccionario.items():
        print(f'{k} = {v}')

diccionario(['banana', 'manzana', 'mandarina'])

# Diccionario geringoso: 
# banana = bapanapanapa
# manzana = mapanzapanapa
# mandarina = mapandaparipinapa