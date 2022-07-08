/*
	IE420 Project
	Julius Olson
	Critical Price
*/
#ifndef CRITICAL_H

#define CRITICAL_H
#include "options.h"
struct criticalRes {
	double criticalPrice;
	double diff;
};
criticalRes criticalPrice(option &opt, double lowerbound, double higherbound);
#endif