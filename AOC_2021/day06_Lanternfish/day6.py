from collections import Counter
import numpy as np

def show_alive(alive, x):
    print("Alive Lanternfish after", x, "days:", alive[x])

#setup iniziale
period = 256
death = np.zeros((period+10,), dtype=np.int64)
alive = np.zeros((period+10,), dtype=np.int64)

#read input
# input = [3,4,3,1,2] #example
input = [1,1,1,2,1,5,1,1,2,1,4,1,4,1,1,1,1,1,1,4,1,1,1,1,4,1,1,5,1,3,1,2,1,1,1,2,1,1,1,4,1,1,3,1,5,1,1,1,1,3,5,5,2,1,1,1,2,1,1,1,1,1,1,1,1,5,4,1,1,1,1,1,3,1,1,2,4,4,1,1,1,1,1,1,3,1,1,1,1,5,1,3,1,5,1,2,1,1,5,1,1,1,5,3,3,1,4,1,3,1,3,1,1,1,1,3,1,4,1,1,1,1,1,2,1,1,1,4,2,1,1,5,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,5,1,1,1,1,3,1,1,1,1,1,3,4,1,2,1,3,2,1,1,2,1,1,1,1,4,1,1,1,1,4,1,1,1,1,1,2,1,1,4,1,1,1,5,3,2,2,1,1,3,1,5,1,5,1,1,1,1,1,5,1,4,1,2,1,1,1,1,2,1,3,1,1,1,1,1,1,2,1,1,1,3,1,4,3,1,4,1,3,2,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,2,1,5,1,1,1,1,2,1,1,1,3,5,1,1,1,1,5,1,1,2,1,2,4,2,2,1,1,1,5,2,1,1,5,1,1,1,1,5,1,1,1,2,1] #test
alive[0] = len(input)

count = Counter(input)
for k,v  in count.items():
    death[k] = v
print("Stato iniziale:", death[:10])


#calcolo vita, morte e miracoli
for i in range(1, period+1): #AKA 80
    death[i+7] += death[i] #7 e non 6 perché devono spawnare
    death[i+9] += death[i]
    alive[i] = death[i-1] + alive[i-1]

#mostro risultati
# for i in range(1, period+1):
#     print("day:", i, ", d:", death[i], ", a:", alive[i])

show_alive(alive, 18)
show_alive(alive, 80)
show_alive(alive, 256)
