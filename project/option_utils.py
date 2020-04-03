"""
Julius Olson
IE 420 Project
Option utils
"""

def put_payoff(K, S):
	return (K-S) * (K-S > 0)

def call_payoff(K, S):
	return (S-K) * (S-K > 0)
