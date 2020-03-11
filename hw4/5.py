from math import exp

S0 = 100
d = 0.8
u = 1.1
r = 0.01
T = 3/12
K = 95

p_star = (exp(r * T) - d) / (u - d)

print(f"p* : {p_star}")

fu = max(K - u * S0, 0)
fd = max(K - d * S0, 0)

f0 = exp(-r * T) * (p_star * fu + (1-p_star) * fd)

print(f"Risk free price: {f0}")

Delta = (fu - fd) / (S0 * (u-d))
print(f"Delta: {Delta}")