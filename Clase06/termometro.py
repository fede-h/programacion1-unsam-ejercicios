import random
import numpy as np

def medir_temp(n, valor_real = 37.5):
    'Devuelve mediciones con error'

    vector = np.empty(n, dtype = np.float64)
    mediciones = []

    for i in range(n):
        medicion = valor_real + random.normalvariate(0, 0.2)
        vector[i] = medicion
        mediciones.append(medicion)

    np.save('Data/temperaturas', vector)
    return mediciones

def resumen_temp(n):
    'Devuelve un resumen estadísico de los valores medidos'

    mediciones = medir_temp(n, 40)
    mean = sum(mediciones) / len(mediciones)
    mediciones.sort()
    if len(mediciones) % 2 != 0:
        index = int(0.5 * ( len(mediciones) - 1 ))
        median = mediciones[index]
    else: 
        index = (int(0.5 * (len(mediciones))), int(0.5 * (len(mediciones) - 2)))
        median = (mediciones[index[0]] + mediciones[index[1]]) / 2

    return {'max' : max(mediciones), 
            'min' : min(mediciones), 
            'mean' : mean, 
            'median' : median}

medir_temp(999)

print(resumen_temp(1000))
