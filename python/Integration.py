#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import math
import sympy as sp
import random
from sympy import Symbol, integrate, exp, oo
from scipy.integrate import quad
from scipy import integrate

N=50
if '-N' in sys.argv:
        p = sys.argv.index('-N')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            N = Nt

def f(x):
    return x**4+x**3+x**2+x

def trapezoid(f,a,b,N):
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

#exact
i, err = quad(f,0,1)
print(i)

#trapazoid
t = trapezoid(lambda x : x**4+x**3+x**2+x,0,1,N)
print(t)

#gauss
f = lambda x: x**4+x**3+x**2+x
g, err = integrate.quadrature(f, 0, 1)
print(g)

#random number between min and max values
def get_rand_number(min_value, max_value):
    range = max_value - min_value
    choice = random.uniform(0,1)
    return min_value + range*choice

#monte carlo
def crude_monte_carlo(Nsample=5000):
    lower_bound = 0
    upper_bound = 1
    Nsample = 5000
    sum_of_samples = 0
    for i in range(Nsample):
        x = get_rand_number(lower_bound, upper_bound)
        sum_of_samples += f(x)
    
    return (upper_bound - lower_bound) * float(sum_of_samples/Nsample)

m = crude_monte_carlo(lambda x : x**4+x**3+x**2+x)
print(m)

if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nsample = Nt

# Integration limits for the Trapezoidal rule
a = 0; b = 1
# define x as a symbol to be used by sympy
x = Symbol('x')
# find result from sympy
exact = i
# set up the arrays for plotting the relative error
n = np.zeros(40); Trapez = np.zeros(4); Monte = np.zeros(4);
# find the relative error as function of integration points
for i in range(1, 3, 1):
    npts = 10**i
    n[i] = npts
    Trapez[i] = abs((trapezoid(f,a,b,N)-exact)/exact)
    Monte[i] = abs((crude_monte_carlo(Nsample)-exact)/exact)
print("Integration points=", n[0], n[1])
print("Trapezoidal relative error=", Trapez[0], Trapez[1])
print("Monte carlo relative error=", Monte[0], Monte[1])
