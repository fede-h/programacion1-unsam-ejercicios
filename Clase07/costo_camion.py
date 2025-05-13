import informe_funciones

def costo_camion(nombre_archivo):
    'Devuelve el costo total del cargamento de un camión'

    camion = informe_funciones.leer_camion(nombre_archivo)
    costo_total = 0
    
    for fruta in camion:
        costo_total += fruta['cajones'] * fruta['precio']

    return costo_total

print(costo_camion('ejercicios_python/Data/camion.csv'))