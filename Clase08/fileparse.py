import csv

def parse_csv(nombre_archivo, select = None, 
              types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, 
    determinando el parámetro select, 
    que debe ser una lista de nombres de las columnas a considerar.
    '''

    if select and not has_headers:      # Manejo de errores si se pasan columnas pero no hay encabezados
        raise RuntimeError("Para seleccionar, necesito encabezados.")

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

            for i, fila in enumerate(filas):
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    try:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Fila {i+1}: No pude convertir {fila}')
                            print(f'Fila {i+1}: Motivo: {e}\n')

                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
                
        else:
            for i, fila in enumerate(filas):
                if not fila: continue
                if types:
                    try:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Fila {i+1}: No pude convertir {fila}')
                            print(f'Fila {i+1}: Motivo: {e}\n')

                registro = tuple(fila)
                registros.append(registro)

    return registros

# camion = parse_csv('ejercicios_python/Data/missing.csv', types = [str,int,float])
