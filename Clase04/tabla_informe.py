def leer_precios(nombre_archivo):
    import csv
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
    import csv
    'Abre un archivo y devuelve una lista de dicts'
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

def hacer_informe(precios, camion):
    'Devuelve una lista de tuplas'
    informe = []
    for venta in camion:
        nombre = venta['nombre']
        cajones = int(venta['cajones'])
        precio = float(venta['precio'])
        cambio = float(precios[venta['nombre']]) - precio
        lista = (nombre, cajones, precio, cambio)
        informe.append(lista)
    return informe


precios = leer_precios('Data/precios.csv')
camion = leer_camion('Data/camion.csv')
informe = hacer_informe(precios, camion)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
pesos = '$'

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

print('---------- '*len(headers))


for nombre, cajones, precio, cambio in informe:
    precio = '$' + str(precio)
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.6s} {cambio:>10.2f}')
