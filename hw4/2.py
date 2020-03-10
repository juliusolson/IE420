from math import exp

S0 = 1.3050
r = 0.008
q = 0.012

K = 1.3
T = 1
c = 0.048
p = 0.03


# Parity

L = c + exp(-r * T) * K
R = p + S0 * exp(-q * T)

print(f"L: {L}, R: {R}")

# At T=0 - Buy put and GBP, sell call

loan = -(c - p - S0)
print(loan)

# At T=1
loan = loan * exp(r * T)
inc = K * exp(q * T)
below_strike = inc - loan

print(loan)
print(f"Get: {below_strike}")
