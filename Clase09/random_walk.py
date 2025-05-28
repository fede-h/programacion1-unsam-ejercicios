import numpy as np
import matplotlib.pyplot as plt
from random import random

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
mas_alejada = [0]
menos_alejada = [100000]

plt.subplot(2, 1, 1)

for i in range(12):
    walk = randomwalk(N)
    
    plt.plot(walk, 
    color=tuple([random() for i in range(4)]),
    linewidth=0.5)

    if max(np.abs(walk)) > max(np.abs(mas_alejada)):
        mas_alejada = walk
    if min(np.abs(walk)) < min(np.abs(menos_alejada)):
        menos_alejada = walk

plt.title('12 caminatas al azar')
plt.xticks([])
plt.yticks([-500, 0, 500])
plt.ylim(-750, 750)

plt.subplot(2,2,3)
plt.plot(mas_alejada, linewidth=1)
plt.title('Caminata más alejada')
plt.xticks([])
plt.yticks([-500, 0, 500])
plt.ylim(-750, 750)

plt.subplot(2,2,4)
plt.plot(mas_alejada, linewidth=1)
plt.title('Menos alejada')
plt.xticks([])
plt.yticks([-500, 0, 500])
plt.ylim(-750, 750)

plt.show()