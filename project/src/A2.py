from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("CPP/outputs/q2.csv")


plt.plot(df["N"], df["CRR"], linewidth=1.0, label="CRR")
plt.plot(df["N"], df["BS"], linewidth=1.0, label="Black-Scholes")
plt.title("Convergence of the CRR binomial model")
plt.xlabel("Steps ($N$)")
plt.ylabel("Price ($C$)")
plt.legend()
plt.savefig("../report/images/convergence.png", dpi=400)
plt.show()

q3Time = pd.read_csv("CPP/outputs/q2_time.csv")
plt.plot(q3Time["N"], q3Time["t"], linewidth=1.0, label="Exec Time")
plt.xlabel("N")
plt.ylabel("t (s)")
plt.title("Execution time for increasing number of steps (N)")
plt.legend()
plt.savefig("../report/images/q2_time.png", dpi=400)
plt.show()