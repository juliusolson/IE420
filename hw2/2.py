from matplotlib import pyplot as plt
import numpy as np

S_T = np.linspace(100, 300, 800)
K = 198
S_0 = 200
P_0 = 5

PL = np.zeros(S_T.shape)
for i, s in enumerate(S_T):
	if s<198:
		PL[i] = 1000 * (K-S_0) - 1000 * P_0
	else:
		PL[i] = 1000 * (S_T[i]-S_0) - 1000 * P_0

z = np.zeros(S_T.shape)

plt.plot(S_T, PL)
plt.plot(S_T, z)
plt.plot(205, 0, '*')
plt.show()