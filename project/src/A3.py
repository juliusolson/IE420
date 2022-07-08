from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from latex import latex_table

d = [
	{"Diff": 0.000999614, "N": 982, "T": 0.0833333},
	{"Diff": 0.000999431, "N": 1298, "T": 0.166667},
	{"Diff": 0.000999672, "N": 1508, "T": 0.25},
	{"Diff": 0.000999921, "N": 1665, "T": 0.333333},
	{"Diff": 0.000999873, "N": 1789, "T": 0.416667},
	{"Diff": 0.000999644, "N": 1890, "T": 0.5},
	{"Diff": 0.00099961 ,"N": 1974, "T": 0.583333},
	{"Diff": 0.000999968, "N": 2044, "T": 0.666667},
	{"Diff": 0.000999796, "N": 2105, "T": 0.75},
	{"Diff": 0.000999964, "N": 2156, "T": 0.833333},
	{"Diff": 0.000999934, "N": 2201, "T": 0.916667},
	{"Diff": 0.000999582, "N": 2240, "T": 1},
]

# plt.plot([x["T"]*12 for x in d], [x["N"] for x in d])
# plt.show()

price_yield0 = pd.read_csv("CPP/outputs/q3_function_of_S0_0.csv")
price_yield4 = pd.read_csv("CPP/outputs/q3_function_of_S0_4.csv")
plt.plot(price_yield0["S0"], price_yield0["Price"], linewidth=1.0, label="$y=0\%%$")
plt.plot(price_yield4["S0"], price_yield4["Price"], linewidth=1.0, label="$y=4\%%$")
plt.plot(price_yield4["S0"], price_yield4["intrinsic"], linewidth=1.0, label="$payoff$")
plt.xlabel("Stock Price ($S_0$)")
plt.ylabel("Option Price ($p$)")
plt.title("Option Price as a function of $S_0$")
plt.legend()
plt.savefig("../report/images/q3_function_of_S0.png", dpi=400)
plt.show()

price_yield0 = pd.read_csv("CPP/outputs/q3_critical_0.csv")
price_yield4 =  pd.read_csv("CPP/outputs/q3_critical_4.csv")
plt.plot(price_yield0["t"], price_yield0["S_star"], linewidth=1.0, label="$y=0\%%$")
plt.plot(price_yield4["t"], price_yield4["S_star"], linewidth=1.0, label="$y=4\%%$")
plt.xlabel("$t$")
plt.ylabel("$S^*(t)$")
plt.title("Early Exercise Boundary")
plt.legend()
plt.savefig("../report/images/q3_critical.png", dpi=400)
plt.show()

latex_table(price_yield0)
latex_table(price_yield4)

q3Time = pd.read_csv("CPP/outputs/q3_time.csv")
plt.plot(q3Time["N"], q3Time["t"], linewidth=1.0, label="Exec Time")
plt.xlabel("N")
plt.ylabel("t (s)")
plt.title("Execution time for increasing number of steps (N)")
plt.legend()
plt.savefig("../report/images/q3_time.png", dpi=400)
plt.show()


q3N = pd.read_csv("CPP/outputs/q3_n.csv")
plt.plot(q3N["T"], q3N["N"], linewidth=1.0)
plt.xlabel("T")
plt.ylabel("N")
plt.title("Number of steps (N) needed to reach $10^{-3}$ accuracy")
plt.savefig("../report/images/q3_n.png", dpi=400)
plt.show()
