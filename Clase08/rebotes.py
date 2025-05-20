import sys

def rebotar(altura = 100, n = 10):
    '''Imprime una secuencia de rebotes
    desde la altura inicial, n veces'''

    for i in range (n):
        altura = altura * (3/5)
        print(f'{i+1}: {round(altura, 4)}')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        altura = int(sys.argv[1])
        rebotar(altura)
    elif len(sys.argv) > 2:
        altura = int(sys.argv[1])
        n = int(sys.argv[2])
        rebotar(altura, n)
    else: 
        altura = 100
        n = 10
        rebotar(altura, n)
