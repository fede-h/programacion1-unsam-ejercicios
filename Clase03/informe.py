import csv


def leer_precios(nombre_archivo):
    'Arma un diccionario con nombres y precios de frutas'
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)

    diccionario = {}

    try:
        for row in rows: 
            diccionario[row[0]] = row[1]
            #print(row)
    except IndexError:
        pass
    
    return diccionario
    f.close()

def leer_camion(nombre_archivo):
    '''Abre un archivo y devuelve una lista de dicts'''
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            try:
                lote = {'nombre':row[0],
                        'cajones': int(row[1]),
                        'precio': float(row[2])}
                camion.append(lote)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return(camion)


precios_venta = leer_precios('Data/precios.csv')

precios_camion = leer_camion('Data/camion.csv')

costo_camion = 0
for fruta in precios_camion:
    costo_camion += fruta['cajones'] * fruta['precio']

recaudacion_venta = 0
for venta in precios_camion:
    #print(venta) {'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}
    #print(venta['nombre']) Lima
    indice = venta['nombre']
    recaudacion_venta += venta['cajones'] * float(precios_venta[indice])

print(f'Costo del camión: {costo_camion}')
print(f'Recaudación de la venta: {recaudacion_venta}')
print(f'Margen de la venta: {recaudacion_venta - costo_camion}')
