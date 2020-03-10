from math import exp

S0 = 20
u = 1.2
d = 0.8

T = 6 / 12
r = 0.01

fu = max(400 - (u * S0)**2, 0)
fd = max(400 - (d * S0)**2, 0)

print(f"fu: {fu}, fd: {fd}")

delta = (fu - fd) / (S0 * (u - d))
psi = (d * fu - u * fd) / ( exp(r * T) * (u - d))

print(f"Delta: {delta}, psi: {psi}")

f0 = delta * S0 - psi

print(f"Price should be: {f0}")


