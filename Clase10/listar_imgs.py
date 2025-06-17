import os
import sys

def archivos_png(directorio):
    '''
    Devuelve todo los archivos .png
    dentro de un directorio dado
    '''

    for root, dirs, files in os.walk(directorio):
        for name in files:
            name = os.path.join(root, name)
            if name[-4:] == '.png':
                print(name)

if __name__ == '__main__':
    if sys.argv[1]:
        archivos_png(sys.argv[1])
    else:
        print('El programa necesita una ruta de archivo')