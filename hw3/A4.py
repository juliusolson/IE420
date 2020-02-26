from math import exp

r_borrow = 0.017
r_deposit = 0.015
q = 0.01
S0 = 1.3
T = 1

# Short arbitrage F - (S0e^(r_borrow-q)T)
F_max = S0 * exp((r_borrow-q)*T)

# Long arbitrage (S0e^(r_deposit-q)T) - F
F_min = S0 *exp((r_deposit-q)*T)

print(f"Fmin: {F_min}, Fmax: {F_max}")