import random

def generar_punto():
    'Genera un punto entre [0,1],[0,1]'

    x = random.random()
    y = random.random()
    return x, y

adentro = 0
n = 1000000

for i in range(n):
    punto = generar_punto()
    if punto[0]**2 + punto[1]**2 < 1: adentro += 1

print(4 * (adentro / n))
