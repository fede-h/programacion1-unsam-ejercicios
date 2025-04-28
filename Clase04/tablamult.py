def tablamult(longitud):
    'Devuelve una tabla de multiplicar'
    
    longitud += 1

    print('    ', end='')
    for i in range (longitud):
        print(f'{i:>4d}', end='')
    print('\n' + '-' * ((longitud+1)*4 +1))

    for i in range (longitud):
        multiplo = 0
        descripcion = str(i) + ':'
        if i != 0:
            print(f'\n{descripcion:<4s}', end='')
        else: print(f'{descripcion:<4s}', end='')

        for q in range (longitud):
            print(f'{multiplo:>4d}', end='')
            multiplo += i
    print('\n')

tablamult(9)
