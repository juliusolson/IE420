
#include <cmath>
#include "options.h"
#include "binomial.h"
#include <iostream>
#include <iomanip>

using namespace std;
double critical_price(double lowerbound, double higherbound, option &opt) {
	double diff, critical, step, S0;
	diff = 0.0;
	step = 1.0;
	
	while (step > 1e-4) {
		for (S0=lowerbound; S0<higherbound; S0+=step) {
			//cout << lowerbound << ", " << higherbound << ", " << step << ", " << S0 << ", "  << diff << endl;
			opt.S0 = S0;
			diff = abs(binomial(opt).option_price - payoff(opt.option, opt.K, S0));
			if (diff > 0.005 || abs(S0 - (higherbound - step)) < 1e-10 ) {
				lowerbound = S0-step;
				higherbound = S0;
				step /= 10;
				critical = lowerbound;
				break;
			}
		}
	}
	
	return critical;
}