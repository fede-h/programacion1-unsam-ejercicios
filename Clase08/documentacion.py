def valor_absoluto(n):
    '''Devuelve la distancia al cero
    de un número n'''

    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    '''Devuelve la suma de todos los números pares
    entre 0 y l'''

    res = 0
    for e in l:
        # Resto 0 si divido por 2
        if e % 2 ==0:
            res += e

    return res

def veces(a, b):
    '''Multiplica un entero a por
    otro entero b no negativo usando sumas'''
    res = 0
    nb = b
    while nb != 0:
        res += a
        nb -= 1 # Contador decreciente
    return res

def collatz(n):
    '''Devuelve el número de pasos en la conjetura de Collatz
    hasta llegar a 1, para un entero positivo n'''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2 # Si el número es par se divide por 2
        else:
            n = 3 * n + 1  # Si es impar se multiplica por 3 y se le suma 1
        res += 1

    return res
