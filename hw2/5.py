import numpy as np
from scipy.optimize import fsolve

def P(y):
	P = 1.5 * np.exp(-0.5*y) + 1.5 * np.exp(-y) + 101.5 *np.exp(-1.5*y)
	return 100 - P


def main():
	guess = np.array([0.03])
	z = fsolve(P, guess)
	print(f"Yield = {z}")

main()
