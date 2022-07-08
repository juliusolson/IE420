/*
	IE420 Project
	Julius Olson
	Critical Price
*/

#include <cmath>
#include "options.h"
#include "binomial.h"
#include "critical.h"
#include <iostream>
#include <iomanip>

using namespace std;

criticalRes criticalPrice(option &opt, double lowerbound, double higherbound) {
	double step, diff, price;
	criticalRes res;

	/*
		For call options - start with low S0 increase until diff < 0.005.
		Then decrease step size and repeat until within accuracy.
		Finds lowest S0 that satisfies the condition that the difference between option price
		and intrinsic value is less than 0.005
	*/
	if (opt.option == C) {
		step = 1.0;
		opt.S0 = lowerbound;
		while (opt.S0 < higherbound) {
			price = binomial(opt).option_price;
			diff = abs(price - payoff(opt.option, opt.K, opt.S0));
			if (diff < 0.005) {
				if (step == 0.0001) {
					// Sufficient accuracy achieved => break
					break;
				}
				opt.S0 -= step;
				step /= 10.0;
			}
			else {
				opt.S0 += step;
			}
		}
		res.criticalPrice = opt.S0;
		res.diff = diff;
		return res;
	}

	/*
		For put options - Start with high S0 and decrease until diff < 0.005
		Then decrease step size and repeat until within accuracy.
		Finds highest S0 that satisfies the condition that the difference between option price
		and intrinsic value is less than 0.005
	*/
	if (opt.option == P) {
		step = 1.0;
		opt.S0 = higherbound;
		while (opt.S0 > lowerbound) {
			price = binomial(opt).option_price;
			diff = abs(price - payoff(opt.option, opt.K, opt.S0));
			if (diff < 0.005) {
				if (step == 0.0001) {
					// Sufficient accuracy achieved => break
					break;
				}
				opt.S0 += step;
				step /= 10.0;
			} else {
				opt.S0 -= step;
			}
		}
		res.criticalPrice = opt.S0;
		res.diff = diff;
		return res;
	}

	cout << "Wrong option type" << endl;
	return res;	
}