/*
	IE420 Project
	Julius Olson
	Options utils
*/

#include "options.h"
#define MAX(x, y) (x > y ? x : y);

double payoff(option_type t, double K, double S) {
	if (t == P) {
		return MAX(K-S, 0);
	}
	return MAX(S-K, 0)
}