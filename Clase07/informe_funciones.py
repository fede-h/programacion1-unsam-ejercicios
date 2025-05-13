import csv
from fileparse import parse_csv
#%%
def leer_camion(nombre_archivo):

    camion = parse_csv(nombre_archivo, types=[str, int, float])

    return camion
#%%
def leer_precios(nombre_archivo):

    precios = dict(parse_csv(nombre_archivo, types=[str, float], has_headers=False))
    
    return precios
#%%
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

print(leer_camion('ejercicios_python/Data/camion.csv'))