"""
Julius Olson
IE 420 Project

"""

from black_scholes import black_scholes
from crr import binomial
from matplotlib import pyplot as plt
import numpy as np

def main():
	option1 = {
		"Option": "C",
		"K": 100.0,
		"T": 1.0,
		"S0": 100.0,
		"sigma": 0.2,
		"r": 0.05,
		"q": 0.04,
		"N": 1.0,
		"Exercise": "E",
	}
	
	bs = black_scholes(**option1)
	f0 = []
	N = list(range(1, 101))
	for n in N:
		option1["N"] = n
		f0.append(binomial(**option1)[0])

	f0 = np.array(f0)
	print(np.abs(f0-bs))

	# plt.plot(N, [bs] * len(N), linewidth=1.0, label="Black-Scholes")
	# plt.plot(N, f0, linewidth=1.0, label="CRR")
	# plt.show()


	option2 = {
		"Option": "P",
		"K": 100.0,
		"sigma": 0.2,
		"r": 0.05,
		"q": 0,
		"Exercise": "A",
	}


if __name__ == "__main__":
	main()