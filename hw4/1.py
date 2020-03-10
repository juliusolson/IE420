from math import exp

S0 = 90
c1 = 1.1
t1 = 1/12
T = 2/12
c = 5.2
K = 90
r = 0.009

D0 = c1 * exp(-r * t1)

p = c + exp(-r * T) * K - (S0 - D0)

print(f"D_0: {D0}")
print("Put price = ", p)
