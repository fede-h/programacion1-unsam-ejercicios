
def buscar_precio(fruta):
    'Devuelve el valor de la fruta solicitada'
    f = open('Data/precios.csv')

    existe = False

    for line in f: 
        row = line.split(',')
        if row[0] == fruta:
            print(f'El precio de un cajon de {fruta} es: {row[1]}')
            existe = True
    
    if not existe:
        print(f'{fruta} no figura en el listado de precios')
    f.close()

buscar_precio('Naranja')
buscar_precio('Kale')

# El precio de un cajon de Naranja es: 106.28
# Kale no figura en el listado de precios