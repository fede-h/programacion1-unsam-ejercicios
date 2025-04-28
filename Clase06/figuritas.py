import numpy as np
from random import randint
import matplotlib.pyplot as plt

def crear_album(figus_total):
    'Crea un álbum vacio'

    album = np.zeros(figus_total, dtype= np.int64)
    
    return album

def album_incompleto(album):
    'Recibe un álbum y determina si está incompleto'

    return 0 in album

def comprar_figus(figus_total):
    'Selecciona una figurita al azar del total posible'

    figu = randint(0, figus_total-1)

    return figu

def comprar_paquete(figus_total, n = 5):
    'Simula un paquete de n figus'

    paquete = [randint(0, figus_total-1) for i in range(n)]

    return paquete

def cuantas_figus(figus_total):
    'Simula la cantidad de compras individuales para llenar el album'

    album = crear_album(figus_total)
    compras = 0

    while album_incompleto(album):
        figu = comprar_figus(figus_total)
        album[(figu)] += 1
        compras += 1

    return compras

def cuantos_paquetes(figus_total):
    'Simula la cantidad de compras de paquetes para llenar el album'

    album = crear_album(figus_total)
    compras = 0

    while album_incompleto(album):
        paquete = comprar_paquete(figus_total)
        for figu in paquete:    
            album[(figu)] += 1
        compras += 1

    return compras

def experimento_figus(n_repeticiones, figus_total, funcion = cuantos_paquetes):
    'Realiza el experimento de llenado n veces'

    intentos = []
    for i in range(n_repeticiones):
        compras = funcion(figus_total)
        intentos.append(compras)

    return (np.mean(intentos), intentos)

def experimento_figus_equipo(n_repeticiones, figus_total, n_albums):
    'Realizado el experimento de llenado para un grupo'

    intentos = []

    for i in range(n_repeticiones):

        album = np.zeros((n_albums, figus_total), dtype= np.int64)
        compras = 0

        while album_incompleto(album):
            paquete = comprar_paquete(figus_total)
            for figu in paquete:
                for i in range(n_albums):
                    if album[i, figu] == 0:
                        album[i, figu] += 1
            compras += 1
        intentos.append(compras)
    
    return(np.mean(intentos), intentos, album)


def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5
equipo = 5

figure, axis = plt.subplots(1, 2, figsize=(12, 5))

axis[0].axhline(y=figus_total, color='r', linestyle='--', alpha=0.5)
axis[0].plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
axis[0].set_xlabel("Cantidad de paquetes comprados.")
axis[0].set_ylabel("Cantidad de figuritas pegadas.")
axis[0].set_title("La curva de llenado se desacelera al final")

intentos = np.array(experimento_figus(100, 640)[1])
probabilidad_850 = ((intentos <= 850).sum())/(np.size(intentos))

print(f'Promedio de paquetes necesarios: {experimento_figus(100, 640)[0]}')
print(f'Probabilidad de llenar el album comprando 850 paquetes o menos: {probabilidad_850*100:.0f}%')
print(f'Chance de 90% de completar el album para {int(np.quantile(intentos, 0.9))} paquetes')
print(f'Promedio de paquetes necesarios para un equipo de {equipo}: {experimento_figus_equipo(100, 625, equipo)[0]:.0f}')

axis[1].hist(intentos, bins=10)
axis[1].set_xlabel("Paquetes comprados")
axis[1].set_ylabel("Cantidad")
axis[1].set_title("Histograma de paquetes necesarios para completar el album")



plt.tight_layout()
plt.show()