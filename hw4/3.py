import numpy as np
from matplotlib import pyplot as plt

K2 = 700
K1 = 680
p2 = 38
p1 = 52

S = np.arange(660, 710, 1)

PL = np.zeros(S.shape)

for i in range(S.shape[0]):
	PL[i] = max(S[i]-K2, 0) - max(S[i] - K1, 0) + 14

plt.plot(S, PL)
plt.show()
