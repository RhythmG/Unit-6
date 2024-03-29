#Stephen Wang
#Calculus Programming Week
#Newton's Method

from math import * 

def f(x):
    return (x**3)-7*(x**2)+(8*x)-3

order = int(input('Enter a number of iterations to estimate the point: '))
guess = float(input('Enter an initial point: '))


def NewtonMethod(a):
    estimation = 0
    for i in range(1, (order+1)):
        estimation = (a - (f(a)/derivative(a)))
        a = estimation 
        print(estimation)

def derivative(a):
    h = 1/1000
    rise = f(a+h)-f(a) 
    run = h
    slope = rise/run
    return slope


NewtonMethod(guess)
derivative(guess)


"""
Newton's Method: x(n+1) = xn - f(xn)/f'(xn)
"""

