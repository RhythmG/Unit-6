#Stephen Wang
#Calculus 10 Essential Problems Project - Chapter 3
#Derivative Calculator

from math import *
import sys

xvalue = float(input('Enter a value of x to approximate the derivative :')) #at what value of x for the derivative?

def f(x):
    return abs(x) #This is the function used to approximate the derivative

def checksides(x): #This is to check if the one-sided derivatives are equal
    h = 1/1000
    rise = f(x+h)-f(x) 
    run = h
    slope = rise/run 
    if rise - (f(x-h)-f(x)) <= h:
        print("The function is not differentiable at this point.")

def derivative(x):
    h = 1/1000
    rise = f(x+h)-f(x) 
    run = h
    slope = rise/run #definition of derivative
    return slope



print('')
checksides(xvalue)
print('Derivative at x =', xvalue, ':', round(derivative(xvalue), 2)) #Prints out the value of the derivative
