#Stephen Wang + Maia Reynolds
#Calculus Programming Week
#Length of a Curve

from math import *

def f(x):
    return x**3

def derivative(x):
    h = 1/1000000
    rise = f(x+h)-f(x) 
    run = h
    slope = rise/run #definition of derivative
    return slope
    
def lenf(x):
    return sqrt(1+(derivative(f(x))**2))

lower = float(input('Enter a lower bound: '))
upper = float(input('Enter an upper bound: '))
    
def rectangles(a, b, numofrectangles):
    width = (b-a)/numofrectangles
    sum = 0
    for i in range(numofrectangles):
        i0 += a
        a += 0.5
        height = lenf(i0)
        area = height*width
        sum += area
    print('')
    print('Area: ', sum*numofrectangles)
    
rectangles(lower, upper, 100000)


