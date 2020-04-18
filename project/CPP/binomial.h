#ifndef BINOMIAL_H
#define BINOMIAL_H
#include "options.h"
struct binomial_res {
	double option_price;
	double exec_time;
};


double risk_neutral_prob(double r, double delta, double u, double d);
binomial_res binomial(option &opt);

#endif