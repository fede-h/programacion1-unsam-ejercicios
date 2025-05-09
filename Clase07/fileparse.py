import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        registros = []

        if has_headers:     # Si tiene headers, crea diciconarios
            
            # Lee los encabezados del archivo
            encabezados = next(filas)

            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    try:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    except ValueError:
                        types = None

                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)

        else:
            for fila in filas:
                if not fila: continue
                if types:
                    try:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    except ValueError:
                        print('\nError de conversión, parseando el archivo sin types\n')
                        types = None

                registro = tuple(fila)
                registros.append(registro)

    return registros
