#import numpy as np
#from scipy.optimize import minimize
#def portfolio_var(w, cov):
#    w = w.reshape(1,2)
#    return np.sum(np.dot(w.T, w) * cov)


#r = np.array([[0.02, 0.015]])
#sigma = np.array([[0.03, 0.02]])
#rho = np.array([[1, 0.3], [0.3, 1]])
#cov = np.dot(sigma.T, sigma) * rho
#print(cov)
#w_init = np.array([[0.2, 0.8]])
#cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x)-1.0})
#w_mvp = minimize(portfolio_var, w_init,method='SLSQP', args=cov, constraints=cons)

from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from numpy.linalg import inv,pinv
from scipy.optimize import minimize

# USER INPUT
#V = np.matrix('123 37.5 70 30; 37.5 122 72 13.5; 70 72 321 -32; 30 13.5 -32 52')/100  # covariance
#R = np.matrix('14; 12; 15; 7')/100
#rf = 3/100

 
R = np.array([[0.02, 0.015]])
sigma = np.array([[0.03, 0.02]])
rho = np.array([[1, 0.3], [0.3, 1]])
V = np.dot(sigma.T, sigma) * rho
print(V)
w0= [0.5, 0.5]
def calculate_portfolio_var(w,V):
	print(w)
	w = np.matrix(w)
	print(w)
	return (w*V*w.T)[0,0]

cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x)-1.0})
res= minimize(calculate_portfolio_var, w0, args=V, method='SLSQP',constraints=cons)
