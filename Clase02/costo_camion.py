import csv

f = open('Data/camion.csv', 'rt')
rows = csv.reader(f)
headers = next(rows)

costo = 0

for row in rows:
    cajones = float(row[1])
    precio_unit = float(row[2])
    costo += cajones * precio_unit

f.close()

print('Costo total: ', costo)

# Costo total:  47671.15