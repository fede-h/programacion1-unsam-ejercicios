import math

print(' --- Calculo de esfera ---\n')

radio = float(input('...Inserte el radio de su esfera! : '))

volumen = (4/3)*math.pi*(radio**3)
print('Volumen: '+ str(round(volumen, 3)))

# ...Inserte el radio de su esfera! : 6
# Volumen: 904.779