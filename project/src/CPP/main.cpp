/*
	IE420 Project
	Julius Olson
	Main
*/


#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream>
#include "binomial.h"
#include "black_scholes.h"
#include "critical.h"
using namespace std;

void q2 () {
	cout << "Running Q2..." << endl;
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

	ofstream outfile, timeFile;
	binomial_res crr;
	double bs;

	/* 
		Open file for results
	*/
	outfile.open("outputs/q2.csv");
	outfile << "N,CRR,BS\n";
	timeFile.open("outputs/q2_time.csv");
	timeFile << "N,t" << endl;
	/*
		- Calculate price using black_scholes 
		- Calculate price with CRR with different values for N
	*/
	bs = black_scholes(opt);
	double diff = 1.0;
	opt.N = 2;
	while (diff > 1e-3) {
		if (opt.N % 100 == 0) {
			cout << opt.N << ", " << diff << endl;
		}
		crr = binomial(opt);
		outfile << setprecision(10) << opt.N << "," << crr.option_price << "," << bs << endl;
		timeFile << setprecision(10) << opt.N << "," << crr.exec_time << endl;
		diff = abs(crr.option_price - bs);
		++opt.N;
	}
	outfile.close();
	timeFile.close();
}

/*
	Calculate the option price using the CRR binomial model as a function of initial stock price(S0)
*/
void priceFunctionOfS0 (option &opt, ofstream &outfile) {
	cout << "Calculating Price as function of S0 for q=" << opt.q << " and t=" << opt.T << endl;
	binomial_res crr;
	outfile << "S0,Price,intrinsic\n";
	for (int S0 = 50; S0 < 170; ++S0) {
		opt.S0 = double(S0);
		crr = binomial(opt);
		outfile << setprecision(10) << S0 << "," << crr.option_price << "," << payoff(opt.option, opt.K, S0) << "\n";
	}
}

/*
	Find the critical price for an option with maturities from 1 month to a year.
*/
void findCriticalPrices(option &opt, ofstream &outfile, double lowerbound, double higherbound) {
	outfile << "t,S_star,diff" << endl;
	for (int i = 1; i < 13; ++i) {
		opt.T = ((double)i) / 12.0;
		cout << "Calulating critical price for q=" << opt.q << " and t=" << opt.T << endl;
		criticalRes critical = criticalPrice(opt, lowerbound, higherbound);
		cout << "Critical: " << critical.criticalPrice << endl;
		outfile << i << "," << critical.criticalPrice << "," << critical.diff << endl;
	}
}

/*
	Find the number of steps (N) required for reaching a absolute error less than 1e-3
*/
void findNSatisfyingAccuracy(option &opt, ofstream &timefile, ofstream &outFile) {
	timefile << "N,t" << endl;
	outFile << "T,N" << endl;

	binomial_res crr;
	opt.N = 2;
	double diff;
	for (int i = 1; i<13; i++){
		opt.T = ((double) i) / 12;
		double old = 0.0;
		diff = 1.0;
		while (diff > 0.001) {
			crr = binomial(opt);
			diff = abs(crr.option_price - old);
			old = crr.option_price;
			timefile << opt.N << "," << crr.exec_time << endl;
			++opt.N;
		}
		cout << "Diff: " << diff << " N: " << opt.N << " T: " << opt.T << "\n";
		outFile << i << "," << opt.N << endl;
	}
}

void q3() {
	cout << "Running Q3" << endl;
	option opt;
	opt.option = P;
	opt.K = 100.0;
	opt.sigma = 0.2;
	opt.r = 0.05;
	opt.q = 0.0;
	opt.S0 = 100.0;
	opt.exercise = A;

	ofstream timeFile;
	ofstream outfile;

	outfile.open("outputs/q3_n.csv");
	timeFile.open("outputs/q3_time.csv");
	findNSatisfyingAccuracy(opt, timeFile, outfile);
	timeFile.close();
	outfile.close();


	
	opt.N = 2250; // Chosen to maintain accuarcy.
	for (double q = 0.0; q <= 0.04; q+= 0.04) {
		if (q == 0.0) {
			outfile.open("outputs/q3_function_of_S0_0.csv");
		} else {
			outfile.open("outputs/q3_function_of_S0_4.csv");
		}
		
		opt.T = 1.0;
		opt.q = q;
		priceFunctionOfS0(opt, outfile);
		outfile.close();

		
		if (q == 0.0) {
			outfile.open("outputs/q3_critical_0.csv");
		} else {
			outfile.open("outputs/q3_critical_4.csv");
		}		

		// Find critical prices using lower and upper bound as identified on the plot
		findCriticalPrices(opt, outfile, 60.0, 95.0);
		outfile.close();
		
	}	
}

void q4() {
	cout << "Running Q4" << endl;
	
	option opt;
	ofstream outfile;

	opt.K = 100.0;
	opt.S0 = 100.0;
	opt.sigma = 0.2;
	opt.r = 0.05;
	opt.q = 0.04;
	opt.N = 3800;
	opt.option = C;
	opt.exercise = A;

	ofstream timeFile;
	outfile.open("outputs/q4_n.csv");
	timeFile.open("outputs/q4_time.csv");
	findNSatisfyingAccuracy(opt, timeFile, outfile);
	timeFile.close();
	outfile.close();

	opt.N = 2250;
	for (double q = 0.04; q<=0.08; q+=0.04) {
		opt.q = q; 
		if (q == 0.04) {
			outfile.open("outputs/q4_function_of_S0_4.csv");
		} else {
			outfile.open("outputs/q4_function_of_S0_8.csv");
		}
		opt.T = 1.0;
		priceFunctionOfS0(opt, outfile);
		outfile.close();


		if (q == 0.04) {
			outfile.open("outputs/q4_critical_4.csv");
		} else {
			outfile.open("outputs/q4_critical_8.csv");
		}
		findCriticalPrices(opt, outfile, 100.0, 160.0);
		outfile.close();
	}
	
}

int main(int argc, char *argv[]) {
	if (argc < 2) {
		cout << "Please provide question number to run as argument" << endl;
		return 0;
	}
	
	int arg = atoi(argv[1]);

	switch (arg) {
	case 2:
		q2();
		break;
	case 3:
		q3();
		break;
	case 4:
		q4();
		break;
	}
	return 0;
}
