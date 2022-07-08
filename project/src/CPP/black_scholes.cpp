/*
	IE420 Project
	Julius Olson
	Black & Scholes
*/

#include <cmath>
#include "binomial.h"


double n_cdf(double x) {
	return 0.5 * erfc(-x * sqrt(0.5));
}

double black_scholes(option &opt) {
	double d1, d2;

	d1 = (log(opt.S0 / opt.K) + (opt.r - opt.q + 0.5 * pow(opt.sigma, 2)) * opt.T) / (opt.sigma * sqrt(opt.T));
	d2 = d1 - opt.sigma * sqrt(opt.T);

	if (opt.option == C) {
		return opt.S0 * exp(-opt.q * opt.T) * n_cdf(d1) - opt.K * exp(-opt.r * opt.T) * n_cdf(d2);
	} else {
		return -opt.S0 * exp(-opt.q * opt.T) * n_cdf(d1) + opt.K * exp(-opt.r * opt.T) * n_cdf(d2);
	}
}