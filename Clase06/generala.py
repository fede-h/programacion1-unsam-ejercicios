import random

def tirar(N = 5):
    'Devuelve una lista con N dados'

    lista = [
        random.randint(1, 6) for i in
        range(N)
    ]

    return lista

def es_generala(tirada):
    'Evalua si una lista de dados es generala'

    if len(set(tirada)) == 1: return True
    else: return False

def prob_generala(N):
    'Devuelve probabilidades de generala en 3 turnos, evaluadas N veces'

    generala = 0

    for i in range(N):
        tirada = tirar()    # primer tirada
        if es_generala(tirada): generala += 1

        else:               # segunda tirada
            for i in range(2):
                frecuencias = {}
                for dado in tirada:
                    if dado not in frecuencias:
                        frecuencias[dado] = 1
                    elif dado in frecuencias:
                        frecuencias[dado] = frecuencias[dado]+1
                frecuencias_invertida = {}
                for key, value in frecuencias.items():
                    frecuencias_invertida[value] = key
                tirada = [frecuencias_invertida.get(max(frecuencias_invertida)) for i in range(max(frecuencias_invertida))]
                restante = tirar(5 - len(tirada))
                tirada += restante
                if es_generala(tirada): generala += 1

    return generala/N


# N = 100000
# G = sum([es_generala(tirar()) for i in range(N)])
# prob = G/N
# frecuencia_generala = N/G

# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
# print(f'Se puede estimar que sale una generala servida cada {frecuencia_generala:.0f} tiradas')

print(prob_generala(100000))