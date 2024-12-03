import numpy as np
from scipy.ndimage import convolve

# read input
fin = open("in.txt", 'r')  # "in.txt" "inEx.txt"

# read algorithm
line = fin.readline().strip("\n")
alg = [ 0 if c=="." else 1 for c in line ]
alg[0] = 1
_ = fin.readline() #burn a line

# read map
lines = []
for l in fin.readlines():
    lines.append([ 0 if c=="." else 1 for c in l.strip("\n") ])
mat = np.array(lines, dtype=np.int32)
# mat = np.array([[0, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 0]], dtype=np.int32)

#Define kernel[s]
kernel = np.array([[256, 128, 64],[32, 16, 8],[4, 2, 1]], dtype=np.int32)
kernelOpp = np.array([[1, 2, 4],[8, 16, 32],[64, 128, 256]], dtype=np.int32)
#TODO: how to execute 2 1D convolution instead of 1 2D conv???
# kernel1D_1 = [1, 2, 4]
# kernel1D_2 = [64, 8, 1]

def mapping(v):
    return alg[v]

for i in range(2): #rounds
    mat = np.pad(mat, (1,1))
    mat = convolve(mat, kernelOpp, mode='constant', cval=0)
    mat = np.vectorize(mapping)(mat) #alg[v]
    print(mat, "\n")

pixelAlive = np.sum(mat)
print("pixelAlive:", pixelAlive)
#5686 < x < 5813




