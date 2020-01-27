import numpy as np
import matplotlib.pyplot as plt

P_ask = 9.25
K = 315
S = np.linspace(200, 400, 200)
PL = np.zeros(S.shape)
for i in range(S.shape[0]):
	PL[i] = max(S[i]-K, 0)

PL -=P_ask


zeros = np.zeros(S.shape)
x = 315+9.25
y = 0.0

plt.plot(S, PL, linewidth=1.0, label="Profit & Loss")
plt.plot(S, zeros, linewidth=1.0)
plt.plot(x,y, "*", label="S = 324.25, P&L = 0.0")
plt.legend()
plt.xlabel("Stock price")
plt.ylabel("P&L")
plt.savefig("pl.png", dpi=300)
plt.show()
