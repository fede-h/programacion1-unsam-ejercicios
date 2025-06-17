#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

#%% ejercicio 7.7
import fileparse
import lote
import formato_tabla

def leer_camion(nombre_archivo):
    with open('../Data/camion.csv') as lineas:
        camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]

    return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote.nombre] - lote.precio
        t = (lote.nombre, lote.cajones, lote.precio, cambio)
        lista.append(t)
    return lista


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    
#%%
def f_principal(argumentos):
    informe_camion(argumentos[1], argumentos[2])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    






