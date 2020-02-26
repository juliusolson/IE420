from math import exp

r = 0.016
S0 = 180
c = 0.51


D0 = 0.51*exp(-r/12) + 0.51 * exp(-r * (4/12))
F0 = (S0-D0)*exp(r*(6/12))

print(F0)

St = 160
t = 2
T = 6
K = F0

Dt = 0.51 * exp(-r*(2/12))
Ft = (St-Dt)*exp(-r*(T-t)/12)

Vt = exp(-r*(T-t)/12)*(Ft-K)

print(Ft)
print(Vt)