import numpy as np
from matplotlib import pyplot as plt

S = np.arange(250, 350, 1)
K1 = 315 
K2 = 317.5
P1 = 5.60
P2 = 5.40

PL = np.maximum(K2-S, np.zeros(S.shape)) - np.maximum(K1-S, np.zeros(S.shape)) + 0.2 

print(np.sum(PL < 0))
plt.plot(S, PL)
plt.show()