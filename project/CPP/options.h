# ifndef OPTIONS_H

# define OPTIONS_H

enum exercise_type {
	A,
	E
};
enum option_type {
	P,
	C
};

struct option {
	double K;
	double S0;
	double sigma;
	double r;
	double q;
	int N;
	double T;
	option_type option;
	exercise_type exercise;
};

double payoff(option_type t, double K, double S);

#endif