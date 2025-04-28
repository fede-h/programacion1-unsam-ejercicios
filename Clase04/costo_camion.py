# costo_camion.py

def costo_camion(nombre_archivo):
    import csv
    file = open(nombre_archivo)
    filas = csv.reader(file)
    encabezados = next(filas)
    costo_total = 0
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total

print(costo_camion('Data/camion.csv'))