/*
	IE420 Project
	Julius Olson
*/


#include <iostream>
#include <iomanip>
#include <fstream>
#include "binomial.h"
#include "black_scholes.h"
#include "critical.h"
using namespace std;

void q2 () {
	/*
		Define option as struct
	*/
	option opt;
	opt.K = 100.0;
	opt.T = 1.0;
	opt.S0 = 100.0;
	opt.sigma = 0.2;
	opt.r = 0.05;
	opt.q = 0.04;
	opt.N = 10;
	opt.exercise = E;
	opt.option = C;

	ofstream outfile;
	binomial_res crr;
	double bs;

	/* 
		Open file for results
	*/
	outfile.open("outputs/q1.csv");
	outfile << "N,CRR,BS\n";
	
	/*
		- Calculate price using black_scholes 
		- Calculate price with CRR with different values for N
	*/
	bs = black_scholes(opt);
	for (int n=1; n<300; n++) {
		opt.N = n;
		crr = binomial(opt);
		outfile << setprecision(10) << n << "," << crr.option_price << "," << bs << "\n";
	}
	outfile.close();
}

void priceFunctionOfS0 (option &opt, ofstream &outfile) {
	binomial_res crr;
	outfile << "S0,Price,intrinsic\n";
	for (int S0 = 50; S0 < 150; ++S0) {
		opt.S0 = double(S0);
		crr = binomial(opt);
		outfile << setprecision(10) << S0 << "," << crr.option_price << "," << payoff(opt.option, opt.K, S0) << "\n";
	}
}

void findCriticalPrices(option &opt, ofstream &outfile, double lowerbound, double higherbound) {
	outfile << "t,S_star";
	for (int i = 1; i < 13; i++) {
		opt.T = ((double)i) / 12.0;
		cout << "Calulating critical price for q=" << opt.q << " and t=" << opt.T << endl;
		double critical = critical_price(lowerbound, higherbound, opt);
		cout << "Critical: " << critical << endl;
		outfile << opt.T << "," << critical << "," << endl;
	}
}

void q3() {
	cout << "Running Q2" << endl;
	option opt;
	opt.option = P;
	opt.K = 100.0;
	opt.sigma = 0.2;
	opt.r = 0.05;
	opt.q = 0.0;
	opt.S0 = 100.0;
	opt.exercise = A;

	// binomial_res crr;
	// double diff;
	// for (int i = 1; i<13; i++){
	// 	opt.T = ((double) i) / 12;
	// 	opt.N = 2;
	// 	double old = 0.0;
	// 	diff = 1.0;
		
	// 	while (diff > 0.001) {
	// 		crr = binomial(opt);
	// 		diff = abs(crr.option_price - old);
	// 		old = crr.option_price;
	// 		opt.N ++;
	// 	}
	// 	cout << "Diff: " << diff << " N: " << opt.N << " T: " << opt.T << "\n";
	// }

	binomial_res crr;
	ofstream outfile;
	
	opt.N = 2250; // Chosen to maintain accuarcy.
	for (double q = 0.0; q <= 0.04; q+= 0.04) {
		cout << "Calculating Price as function of S0 for q=" << q << " and t=1.0 ..." << endl;
		if (q == 0.0) {
			outfile.open("outputs/q2_function_of_s0_0.csv");
		} else {
			outfile.open("outputs/q2_function_of_s0_4");
		}
		
		opt.T = 1.0;
		opt.q = q;
		priceFunctionOfS0(opt, outfile);
		outfile.close();

		if (q == 0.0) {
			outfile.open("outputs/critical_price_0.csv");
		} else {
			outfile.open("outputs/critical_price_4.csv");
		}		
		findCriticalPrices(opt, outfile, 70.0, 95.0);
		outfile.close();
	}	
}

void q4() {
	cout << "Running Q4" << endl;
	
	option opt;
	ofstream outfile;

	opt.K = 100.0;
	opt.sigma = 0.2;
	opt.r = 0.05;
	opt.q = 0.04;
	opt.N = 2250;
	opt.option = C;
	opt.exercise = A;

	outfile.open("outputs/callprice_function_of_S0.csv");
	opt.T = 1.0;
	priceFunctionOfS0(opt, outfile);
	outfile.close();

	// TODO: Fix critical price for q4
	outfile.open("outputs/callprice_critical_0.csv");
	findCriticalPrices(opt, outfile, 50.0, 100.0);
}

int main() {
	//q1();
	//q3();
	q4();

	return 0;
}