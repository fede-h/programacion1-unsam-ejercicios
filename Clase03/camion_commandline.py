import csv, sys

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    costo = 0

    for row in rows:
        cajones = float(row[1])
        precio_unit = float(row[2])
        costo += cajones * precio_unit

    return costo
    f.close()

if len(sys.argv) == 2:
    archivo = int(sys.argv[2])
else: archivo = 'Data/camion.csv'

print('Costo total: ', costo_camion(archivo))

# Costo total:  47671.15