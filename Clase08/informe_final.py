import csv
from fileparse import parse_csv

def f_principal(programa, archivo1, archivo2):
    return informe_camion(archivo1, archivo2)

def leer_camion(nombre_archivo):

    camion = parse_csv(nombre_archivo, types=[str, int, float])

    return camion

def leer_precios(nombre_archivo):

    precios = dict(parse_csv(nombre_archivo, types=[str, float], has_headers=False))
    
    return precios

def informe_camion(archivo_camion, archivo_precios):
    informe = []
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        informe.append(t)

    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3 and sys.argv[1][-3:] == 'csv' and sys.argv[2][-3:] == 'csv':
        archivo1 = sys.argv[1]
        archivo2 = sys.argv[2]
        f_principal(None, archivo1, archivo2)
    else: raise SyntaxError('Se necesitan dos archivos csv')
