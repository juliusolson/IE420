"""
Julius Olson
IE 420 Project
CRR Binomial model
"""


"""
Input
============================
Option:   Option Type (C, P)
K: 		  Strike
T:		  Time to maturity
S0:		  Initial stock price
sigma:	  Volatility
r:		  Continuous Compounding risk free rate 
q:        Continuous Compounding dividend yield
N:		  Number of steps
Exercise: (A, E) (American, European)

Output: (price, computational time)
"""

from math import sqrt, factorial, exp
import numpy as np
from option_utils import put_payoff, call_payoff
import time

def comb(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))

def risk_neutral_prob(r, delta, u, d):
	return (exp(r*delta) - d) / (u-d)

def binomial(Option, K, T, S0, sigma, r, q, N, Exercise):
	start = time.time()

	delta = T / N

	u = exp(sigma * sqrt(delta))
	d = exp(-sigma * sqrt(delta))
	p = risk_neutral_prob(r-q, delta, u, d)

	sN = np.array([ (u**j)*(d**(N-j))*S0 for j in range(N+1)]) 

	if Option == "P":
		f = put_payoff
	elif Option == "C":
		f = call_payoff
	else: raise TypeError

	fN = f(K, sN)
	f0 = exp(-r * T) * sum(comb(N, j) * (p**j) * (1-p)**(N-j) * fN[j] for j in range(len(fN)))
	
	end = time.time()

	return f0, end-start




	
