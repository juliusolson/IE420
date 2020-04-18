from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("CPP/outputs/q1.csv")

values = df.values
arr = np.array(values)

plt.plot(arr[:, 0], arr[:, 1], linewidth=1.0, label="CRR")
plt.plot(arr[:, 0], arr[:, 2], linewidth=1.0, label="Black-Scholes")
plt.show()