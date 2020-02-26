from math import exp

S0 = 1.3
r = 0.016
q = 0.01

F0 = 1.30151

T = 6/12

f_zeroval = S0 * exp((r-q) * T)

print(f_zeroval)

prof = S0 * exp((r-q)*T) * 1000000 - F0*1000000
print(prof)