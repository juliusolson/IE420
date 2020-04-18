from matplotlib import pyplot as plt
import numpy as np
import pandas as pd



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

plt.plot([x["T"]*12 for x in d], [x["N"] for x in d])
plt.show()


df = pd.read_csv("CPP/outputs/q2_function_of_s0.csv")
print(df.columns)
plt.plot(df["S0"], df["Price"])
plt.plot(df["S0"], df["Price"] - (100-df["S0"]))
plt.show()


