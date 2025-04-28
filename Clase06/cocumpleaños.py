import random

def cocumpleaños(n = 10000):
    'Devuelve la posibilidad de un mismo cumpleaños entre 30 personas'

    repetidos = 0
    for i in range(n):
        cumples = []
        for i in range(30):
            cumples.append(random.randint(1,365))
        if len(set(cumples)) != len(cumples):
            repetidos += 1
    
    return repetidos/n

def probabilidad(grupo, n):

    repetidos = 0
    for i in range(n):
        cumples = []
        for i in range(grupo):
            cumples.append(random.randint(1,365))
        if len(set(cumples)) != len(cumples):
            repetidos += 1
    
    return repetidos/n


print(cocumpleaños())
print(probabilidad(23, 100000))
