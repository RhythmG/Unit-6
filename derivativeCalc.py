#Stephen Wang
#Calculus 10 Essential Problems Project - Chapter 3
#Derivative Calculator

from math import *

xvalue = float(input('Enter a value of x to approximate the derivative :')) #at what value of x for the derivative?

def f(x):
    return abs(x) #This is the function used to approximate the derivative

def derivative(x):
    h = 1/1000
    rise = f(x+h)-f(x) 
    run = h
    slope = rise/run #definition of derivative
    return slope

print("The function is not differentiable at x = ", xvalue)

print('')
print('Derivative at x =', xvalue, ':', round(derivative(xvalue), 2)) #Prints out the value of the derivative
