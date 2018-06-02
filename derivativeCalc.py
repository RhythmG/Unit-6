#Stephen Wang
#Calculus 10 Essential Problems Project - Chapter 3
#Derivative Calculator

xvalue = float(input('Enter a value of x to approximate the derivative :'))

def f(x):
    return ((x-2)**2)*(x-4) #This is the function used to approximate the derivative

def derivative(x):
    h = 1/1000
    rise = f(x+h)-f(x)
    run = h
    slope = rise/run
    return slope

print('')
print('Derivative at x =', xvalue, ':', derivative(3))
