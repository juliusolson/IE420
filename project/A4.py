from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("CPP/outputs/callprice_function_of_S0.csv")
print(df.columns)
plt.plot(df["S0"], df["Price"])
plt.show()


