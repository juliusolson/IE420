{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import exp, log\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "def repl_portfolio(fu, fd, u, d, S0, r, delta):\n",
    "    Delta = (fu-fd) / (S0(u-d))\n",
    "    Psi = (d*fu - u*fd) /(exp(r*delta) * (u-d))\n",
    "    return Delta, Psi\n",
    "\n",
    "def no_arb_val(Delta, Psi, S0):\n",
    "    return Delta * S0 - Psi\n",
    "\n",
    "def risk_neutral_prob(r, delta, u, d):\n",
    "    return (exp(r*delta)-d) / (u-d)\n",
    "\n",
    "def risk_neutral_value(p_star, fu, fd, r, delta):\n",
    "    return exp(-r*delta) * (p_star * fu + (1-p_star) * fd)\n",
    "\n",
    "def put_payoff(K, S):\n",
    "    return max(K-S, 0)\n",
    "\n",
    "def delta_hedge(fu, fd, u, d, S0):\n",
    "    return (fu-fd) / (S0 * (u-d))\n",
    "\n",
    "def lookback_call_payoff(K, S_max):\n",
    "    return max(0, S_max - K)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P_star: 0.5125313021485024\n",
      "Value: 5.224131634995086\n",
      "Delta0: -43.902745422390126\n",
      "Delta_td -79.99999999999999\n"
     ]
    }
   ],
   "source": [
    "# 1\n",
    "\n",
    "S0 = 50\n",
    "u = 1.2\n",
    "d = 0.8\n",
    "r = 0.01\n",
    "K = 50\n",
    "\n",
    "# Risk neutral prob\n",
    "p_star = risk_neutral_prob(r, 1/2, u, d)\n",
    "print(\"P_star:\", p_star)\n",
    "\n",
    "# Payoff\n",
    "fuu = put_payoff(K, (u**2) * S0)\n",
    "fdd = put_payoff(K, (d **2) * S0)\n",
    "fud = put_payoff(K, (u*d) * S0)\n",
    "\n",
    "fu = risk_neutral_value(p_star, fuu, fud, r, 1/2)\n",
    "fd = risk_neutral_value(p_star, fud, fdd, r, 1/2)\n",
    "f0 = risk_neutral_value(p_star, fu, fd, r, 1/2)\n",
    "\n",
    "# Value of option\n",
    "print(\"Value:\", f0)\n",
    "\n",
    "# initial delta hedge\n",
    "Delta0 = delta_hedge(fu, fd, u, d, S0)\n",
    "print(\"Delta0:\", Delta0 * 100)\n",
    "\n",
    "# Adjust hedge\n",
    "Delta_tu = delta_hedge(fuu, fud, u, d, S0)\n",
    "Delta_td = delta_hedge(fud, fdd, u, d, S0)\n",
    "print(\"Delta_td\", Delta_td * 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.5125156380289756 121.00000000000001 110.00000000000001 115.34893890504634 104.86267173186032 109.96179922743895\n",
      "Value: 109.96179922743895 Delta: 52.431335865930095\n"
     ]
    }
   ],
   "source": [
    "# 2\n",
    "\n",
    "S0 = 100\n",
    "delta = 3/12\n",
    "u = 1.1\n",
    "d = 0.9 \n",
    "r = 0.01\n",
    "K = 95\n",
    "\n",
    "# Backward induction\n",
    "p_star = risk_neutral_prob(r, delta, u, d)\n",
    "fuu = max(S0, u*S0, (u**2)*S0)\n",
    "fud = max(S0, u*S0, u*d*S0)\n",
    "fdd = max(S0, d*S0, (d**2)*S0)\n",
    "fu = risk_neutral_value(p_star, fuu, fud, r, delta)\n",
    "fd = risk_neutral_value(p_star, fud, fdd, r, delta)\n",
    "\n",
    "# Value\n",
    "f0 = risk_neutral_value(p_star, fu, fd, r, delta)\n",
    "\n",
    "# Delta hedge\n",
    "Delta = delta_hedge(fu, fd, u, d, S0)\n",
    "\n",
    "print(p_star, fuu, fud, fu, fd, f0)\n",
    "\n",
    "print(\"Value:\", f0, \"Delta:\", 100 * Delta)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3\n",
    "\n",
    "# Stock index\n",
    "S0 = 2500\n",
    "u, d  = 1.15, 0.85\n",
    "r = 0.01\n",
    "q = 0.03\n",
    "\n",
    "# Compute Value of 6 month at-the-money American Call option\n",
    "\n",
    "# When Exercise? \n",
    "\n",
    "# Value of equivalent European Call? \n",
    "\n",
    "# How much pay for right to exercise early?"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
