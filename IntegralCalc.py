#Stephen Wang
#Calculus 10 Essential Problems Project
#RAM Calculator

#Enter your function after 'return' in line 27: (use ** to denote an exponent)

from math import *

def inputValid(a,a0,a1):
    if a <= a1 and a >= a0:
        return True
    else:
        print('Invalid input')
        return False
            
print('1: Rectangles')
print('2: Trapezoid')
print("3: Simpson's Rule")
print('')
getInput = False
while getInput == False:
    typeapprox = int(input('Enter a number corresponding to your desired approximation: '))
    getInput = inputValid(typeapprox, 1, 3)


def f(x):
    return sin(x)
            
if typeapprox == 1:
    print('')
    print('1: LRAM')
    print('2: RRAM')
    print("3: MRAM")
    getInput = False
    while getInput == False:
        ramselect = int(input('Enter a number corresponding to your desired RAM approximation: '))
        getInput = inputValid(ramselect, 1, 3)
    
    if ramselect == 1:
        print('LRAM Selected')
    
    elif ramselect == 2:
        print('RRAM Selected')

    elif ramselect == 3:
        print('MRAM Selected')

    lower = float(input('Enter a lower bound: '))
    upper = float(input('Enter an upper bound: '))
    intervals = int(input('Enter a number of rectangles to approximate: '))
    inputValid(intervals, 1, 1.0E16)
    
    def rectangles(a, b, numofrectangles):
        width = (b-a)/numofrectangles
        sum = 0
        for i in range(numofrectangles):
            if ramselect == 1:
                i0 = i
            elif ramselect == 2:
                i0 = i+1
            elif ramselect == 3:
                i0 = i+0.5
            else:
                print("Error -- input is not in range")
            height = f(a + i0*width)
            area = height*width
            sum += area
        print('')
        print('Area: ', sum)
    
    rectangles(lower, upper, intervals)
    
elif typeapprox == 2:
    print('')
    print('Trapezoids Selected')
    lower = int(input('Enter a lower bound: '))
    upper = int(input('Enter an upper bound: '))
    
    getInput = False
    while getInput == False:
        intervals = int(input('Enter a number of trapezoids to approximate: '))
        getInput = inputValid(intervals, 1, 1.0E16)
    def trapezoid(a, b, numoftraps):
        width = float(b-a)/numoftraps
        sum = 0
        sum += f(a) + f(b)
        for i in range(1, numoftraps): #need to fix this for decimals
            sum += 2*f(a + i*width)
        print('')
        print('Area: ',(sum*width)/2) #0.25 for 0,1 10 traps
    
    trapezoid(lower, upper, intervals)

   
elif typeapprox == 3:
    print('')
    print("Simpson's Rule Selected")
    lower = float(input('Enter a lower bound: '))
    upper = float(input('Enter an upper bound: '))
    getInput = False
    while getInput == False:
        intervals = int(input('Enter a number of elements to approximate: '))
        getInput = inputValid(intervals, 1, 1.0E16)
    def simpson(a, b, numofsimps):
        width = float(b-a)/numofsimps
        sum = 0
        sum += f(a) + f(b)
        for i in range(1, numofsimps, 2):
            sum += 4*f(a + i*width)
        for i in range(2, numofsimps-1, 2):
            sum += 2*f(a + i*width)
        print('')
        print('Area: ',(sum*width)/3)
    
    simpson(lower, upper, intervals)
    

        

