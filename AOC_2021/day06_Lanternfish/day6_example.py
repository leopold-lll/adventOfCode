import numpy as np

#setup iniziale
period = 80
death = list(np.zeros((period+10,), dtype=int))
alive = list(np.zeros((period+10,), dtype=int))

#read input
alive[0] = 5
death[1] = 1
death[2] = 1
death[3] = 2
death[4] = 1
print("Stato iniziale:", death[:5])

#calcolo vita, morte e miracoli
for i in range(1, period+1): #AKA 80
    death[i+7] += death[i] #7 e non 6 perché devono spawnare
    death[i+9] += death[i]
    alive[i] = death[i-1] + alive[i-1]

#mostro risultati
for i in range(1, period+1):
    print("day:", i, ", d:", death[i], ", a:", alive[i])

print(alive[18], "should be 26...")
print(alive[80], "should be 5934...")