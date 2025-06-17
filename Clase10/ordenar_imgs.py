import os
import sys
import shutil
from datetime import datetime

def dir_check(dir_destino):
    '''Crea la carpeta dir_destino
    si no existe
    '''

    # Se tiene en cuenta la existencia del directorio,
    # su inexistencia o una ruta inválida
    try:
        os.mkdir(dir_destino)
        print(f'Dirección {dir_destino} no encontrada, creando la carpeta')
    except FileExistsError:
        pass
    except FileNotFoundError:
        print('Ubicación destino no encontrada')
        sys.exit()


def procesar_nombre(fname):
    '''Recibe un formato de nombre archivo_AAAAmmdd.png
    y devuelve nombrearchivo y 
    el datetime.datetime(AAAA, mm, dd)
    '''

    # Se tiene en cuenta un espacio menos
    # para el _ antes de la fecha
    nombre = fname[0:-13] + fname[-4:]

    anio = int(fname[-12:-8])
    mes = int(fname[-8:-6])
    dia = int(fname[-6:-4])
    fecha = datetime(anio, mes, dia)

    # Devuelve (string, datetime.datetime)
    return nombre, fecha

def procesar(dir_origen, dir_destino):
    '''Procesa los nombres y actualiza las fechas para todos
    los .png en directorios y subdirectorios de dir_origen,
    mueve todos esos archivos a dir_destino
    y borra las carpetas vacias de dir_origen
    '''

    # Recorro todas las direcciones dentro de dir_origen
    for root, dirs, files in os.walk(dir_origen):
        for name in files:
            fname = name
            name = os.path.join(root, name)

            # Identifico un archivo png, los otros son ignorados
            if name[-4:] == '.png': 
                try:
                    # Nuevo nombre y fechas para fname
                    stats = procesar_nombre(fname)
                    new_name = os.path.join(root, stats[0])
                    os.rename(name, new_name)

                    # Cambio de datetime a timestamp para utime
                    atime = int(datetime.timestamp(stats[1]))
                    mtime = atime
                    # Modifico tiempo de última mod. y acceso
                    os.utime(new_name, times=(atime, mtime))

                    # Muevo el archivo procesado con nuevo nombre y 
                    # fechas a dir_destino
                    shutil.move(new_name,
                                os.path.join(dir_destino, stats[0]))

                # ValueError en caso de que procesar()
                # no pueda formatear el nombre de archivo
                except ValueError: 
                    print(f'No se pudo procesar {name}: Formato incorrecto')

    # Limpieza de todas las carpetas vacias
    folders = []
    for root, dirs, files in os.walk(dir_origen):
        for name in dirs:
            folders.append(os.path.join(root, name))
    # La lista se invierte para mostrar subdirectorios anidados antes
    # de esta forma se puede eliminar su parent folder si está vacio
    folders = list(reversed(folders))
    
    # Borro los directorios vacios
    # si no está vacio cae en OSError
    for name in folders:
        try:
            os.rmdir(name)
        except OSError:
            pass

if __name__ == '__main__':

    # Chequeo que se especifiquen direcciones y las guardo
    if len(sys.argv) == 3:
        dir_origen = sys.argv[1]
        dir_destino = sys.argv[2]
    else: 
        print('Se necesita una dirección de origen y una de destino')
        sys.exit()

    dir_check(dir_destino)
    # Procesamiento de carpetas
    procesar(dir_origen, dir_destino)
