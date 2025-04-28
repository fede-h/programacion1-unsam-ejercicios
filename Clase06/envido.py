import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [[valor,palo] for valor in valores for palo in palos]

def mesa(n):
    'Simula n veces la probabilidad de envido +31'

    envidos = 0
    for i in range(n):
        envido = 0

        mano = random.sample(naipes, k = 3)
        for index in range(len(mano)):    
                if mano[index][0] >= 10:
                    mano[index] = [0, mano[index][1]]
            
        if mano[0][1] == mano[1][1] == mano[2][1]:
            puntajes = [valor for valor, palo in mano]
            envido = max(puntajes)
            puntajes.remove(max(puntajes))
            envido += max(puntajes) + 20
        elif mano[0][1] == mano[1][1]:
            envido = 20 + mano[0][0] + mano[1][0]
        elif mano[0][1] == mano[2][1]:
            envido = 20 + mano[0][0] + mano[2][0]
        elif mano[1][1] == mano[2][1]:
            envido = 20 + mano[1][0] + mano[2][0]
            
        if envido >= 31: envidos += 1
    
    return envidos/n

print(mesa(100000))
        