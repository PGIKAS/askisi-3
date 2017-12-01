import numpy as np
from scipy.misc import imread, imsave
import sys



image = imread(sys.argv[1]).astype(np.float32)
if len(sys.argv) == 12:
    F = 3
elif len(sys.argv) == 28:
    F = 5
else:
    exit(0)

#dhmiourgw to filtro
filtro = [[0 for i in range(F)] for j in range(F)]

k=3
for i in range(F):
    for j in range(F):
        filtro[i][j] = float(sys.argv[k])
        k = k+1

f = int(F/2)
#kanw padd sthn eikona
filteredImage = np.zeros(image.shape)
paddedImage = np.pad(image,f,'constant')

M = filteredImage.shape[0]
N = filteredImage.shape[1]

#efarmozw to filtro
for i in range(M):
    for j in range(N):
        for k in range(-f, f+1, 1):
            for l in range(-f,f+1, 1):
                filteredImage[i][j] = filteredImage[i][j] + paddedImage[i+k+f][j+l+f]*filtro[k+f][l+f]


imsave(sys.argv[2], filteredImage)
