"""
Julius Olson
IE 420 Project

Black-Scholes
"""

from scipy.stats import norm
from math import log, sqrt, exp

def N_cdf(x):
	return norm(0, 1).cdf(x)

def black_scholes(Option, K, T, S0, sigma, r, q, N, Exercise):
	d1 = (log(S0 / K) + (r-q + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
	d2 = d1 - sigma * sqrt(T)

	if Option == "C":
		return S0 * exp(-q*T) * N_cdf(d1) - K*exp(-r*T) * N_cdf(d2)
	elif Option == "P":
		return -S0 * exp(-q*T) * N_cdf(-d1) + K*exp(-r*T) * N_cdf(-d2)
	else:
		raise TypeError
