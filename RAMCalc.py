#Stephen Wang
#Calculus 10 Essential Problems Project
#RAM Calculator


#Enter your function after 'return' in line 17: (use ** to denote an exponent)

import math

print('1: Rectangles')
print('2: Trapezoid')
print("3: Simpson's Rule")
print('')
typeapprox = int(input('Enter a number corresponding to your desired approximation: '))

def f(x):
    return x**3

if typeapprox == 1:
    print('')
    lower = float(input('Enter a lower bound: '))
    upper = float(input('Enter an upper bound: '))
    intervals = int(input('Enter a number of rectangles to approximate: '))
    
    def integral(a, b, numofrectangles):
        width = (b-a)/numofrectangles
        sum = 0
        for i in range(numofrectangles):
            height = f(a + i*width)
            area = height*width
            sum += area
        print('')
        print(sum)
    
    integral(lower, upper, intervals)
    
if typeapprox == 2:
    print('')
    lower = int(input('Enter a lower bound: '))
    upper = int(input('Enter an upper bound: '))
    intervals = int(input('Enter a number of trapezoids to approximate: '))
    def trapezoid(a, b, numoftraps):
        width = (b-a)/numoftraps
        sum = 0
        sum += width*f(a) + width*f(b)
        def frange(start, stop, step):
            i = start
            while i < stop:
                yield i
                i += step
        for i in frange(a+width, upper, width): #need to fix this for decimals
            height = 2*f(a + i*width)
            area = height*width
            sum += area
        print('')
        print(sum/2) #0.25 for 0,1 10 traps
    
    trapezoid(lower, upper, intervals)

"""    
if typeapprox == 3:
    print('')
    lower = float(input('Enter a lower bound: '))
    upper = float(input('Enter an upper bound: '))
    intervals = int(input('Enter a number of Simpson shapes to approximate: This MUST be an even number '))
    def simpson(a, b, numofsimps):
        width = (b-a)/numofsimps
        sum = 0
        sum += width*f(a) + width*f(b)
        for i in range(a, b, floor(numofsimps)):
            height = f(a + i*width)
            area = height*width
            sum += area
        print('')
        print(sum/3)
    
    simpson(lower, upper, intervals)
"""
"""
else:
    print('')
    print("Error -- Please enter a number between 1-3.")
"""
        

