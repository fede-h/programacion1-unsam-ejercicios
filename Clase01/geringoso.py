cadena = 'Boligoma'
geringoso = ''

for c in cadena:
    geringoso += c
    if c.lower() in 'aeiou':
        geringoso += 'p' + c.lower()

print(geringoso)

# Salida = Bopolipigopomapa