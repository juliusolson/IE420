from math import log, exp

y = 0.03
P = exp(-0.5 * y) + exp(-y) + 101 * exp(-1.5*y)

r05 = log(99/100) / -0.5
r1 = log(97.5/100) / -1
r15 = log((P - (exp(-0.5*r05) + exp(-r1)))/101) / -1.5

P_star = 1.2 * exp(-0.5*r05) + 1.2 * exp(-r1) + 101.2*exp(-1.5*r15)

print(f"""
y: {y}
P: {P}
r05: {r05}
r1: {r1}
r15: {r15}
P_star: {P_star}
""")