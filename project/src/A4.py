from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from latex import latex_table


price_yield0 = pd.read_csv("CPP/outputs/q4_function_of_S0_4.csv")
price_yield4 = pd.read_csv("CPP/outputs/q4_function_of_S0_8.csv")
plt.plot(price_yield0["S0"], price_yield0["Price"], linewidth=1.0, label="$y=0\%%$")
plt.plot(price_yield4["S0"], price_yield4["Price"], linewidth=1.0, label="$y=4\%%$")
plt.plot(price_yield4["S0"], price_yield4["intrinsic"], linewidth=1.0, label="payoff")
plt.xlabel("Stock Price ($S_0$)")
plt.ylabel("Option Price ($c$)")
plt.title("Option Price as a function of $S_0$")
plt.legend()
plt.savefig("../report/images/q4_function_of_S0.png", dpi=400)
plt.show()

price_yield0 = pd.read_csv("CPP/outputs/q4_critical_4.csv")
price_yield4 =  pd.read_csv("CPP/outputs/q4_critical_8.csv")
plt.plot(price_yield0["t"], price_yield0["S_star"], linewidth=1.0, label="$y=0\%%$")
plt.plot(price_yield4["t"], price_yield4["S_star"], linewidth=1.0, label="$y=4\%%$")
plt.xlabel("$t$")
plt.ylabel("$S^*(t)$")
plt.title("Early Exercise Boundary")
plt.legend()
plt.savefig("../report/images/q4_critical.png", dpi=400)
plt.show()

latex_table(price_yield0)
latex_table(price_yield4)

q4Time = pd.read_csv("CPP/outputs/q4_time.csv")
plt.plot(q4Time["N"], q4Time["t"], linewidth=1.0, label="Exec Time")
plt.xlabel("N")
plt.ylabel("t (s)")
plt.title("Execution time for increasing number of steps (N)")
plt.legend()
plt.savefig("../report/images/q4_time.png", dpi=400)
plt.show()


q4N = pd.read_csv("CPP/outputs/q4_n.csv")
plt.plot(q4N["T"], q4N["N"], linewidth=1.0)
plt.xlabel("T")
plt.ylabel("N")
plt.title("Number of steps (N) needed to reach $10^{-3}$ accuracy")
plt.savefig("../report/images/q4_n.png", dpi=400)
plt.show()
