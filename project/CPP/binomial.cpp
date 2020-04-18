/*
	IE420 Project
	Julius Olson
*/

#include <iostream>
#include <cmath>
#include "binomial.h"
#include "options.h"

double risk_neutral_prob(double r, double delta, double u, double d) { 
	return (exp(r * delta) - d) / (u-d); 
}

/*
	Binomial: CRR pricing algorithm
	Input: option struct
	Output: option price and execution time
*/

binomial_res binomial(option &opt) {
	binomial_res res;
	clock_t start, end;

	start = clock();
	double delta, u, d, p;

	delta = opt.T / (double) opt.N;

	// Crr - Calculate u and d using volatility
	u = exp(opt.sigma * sqrt(delta));
	d = exp(-opt.sigma * sqrt(delta));
	p = risk_neutral_prob(opt.r-opt.q, delta, u, d);

	/* 
		Payoff at maturity
	*/
	double f[opt.N+1];
	for (int j=0; j<opt.N+1; j++) {
		f[j] = pow(u, j) * pow(d, opt.N-j) * opt.S0;
		f[j] = payoff(opt.option, opt.K, f[j]);
	}

	/*
		Backwards induction
	*/
	for (int i=opt.N; i>0; --i) {
		for (int j=0; j<i; ++j) {
			f[j] = exp(-opt.r * delta) * ((p * f[j+1]) + (1-p) * f[j]);

			if (opt.exercise == A) {
				double early_exercise = pow(u, j) * pow(d, i - j - 1) * opt.S0;
				early_exercise = payoff(opt.option, opt.K, early_exercise);
				// if (opt.option == P) {
				// 	early_exercise = MAX(opt.K - early_exercise, 0.0);
				// } else {
				// 	early_exercise = MAX(early_exercise - opt.K, 0.0);
				// }
				if (early_exercise > f[j]) {
					f[j] = early_exercise;
				}
			}
		}
	}
	end = clock();
	res.option_price = f[0];
	res.exec_time = (end-start) / (double) CLOCKS_PER_SEC;
	return res;
}