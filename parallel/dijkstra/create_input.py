import numpy as np
import math

N = 1000

mask = np.array([[int(i != j) for j in range(0, N)] for i in range(0, N)])
arr = np.random.randint(int(math.sqrt(N)), size=(N, N)) * mask
np.savetxt('input.txt', arr, fmt='%d')