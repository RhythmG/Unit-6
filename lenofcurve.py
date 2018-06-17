#Stephen Wang + Maia Reynolds
#Calculus Programming Week
#Length of a Curve

from math import *

nInterval = 10000

def f(x):
    return sin(x)

def derivative(x):
    h = 1.0/nInterval
    rise = (f(x+h)-f(x-h))*0.5
    run = h
    slope = rise/run #definition of derivative
    return slope
    
def lenf(x):
    df = derivative(x)
    return sqrt(1+(df*df))

lower = float(input('Enter a lower bound: '))
upper = float(input('Enter an upper bound: '))
    
def rectangles(a, b, numofrectangles):
    sum = 0
    x = a
    dx = (b-a)/numofrectangles
    while x<b:
        rate = lenf(x)
        ds = rate*dx
        sum += ds
        x += dx
    print('')
    print('Length: ', sum)
    
rectangles(lower, upper, nInterval)


