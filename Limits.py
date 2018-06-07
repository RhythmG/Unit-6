#Stephen Wang
#Calculus Programming Week
#Limit calculator

from math import *

approaching = float(input('Enter a x-value to approach: '))

def f(x):
    return (x**2)/(x-2)

def limit(x):
    if f(approaching) <= 1.0E16 and f(approaching) >= -1.0E16:
        print(f(approaching))
    elif f(approaching-0.0001) - f(approaching+0.0001) <= 0.1:
            print((f(approaching-0.0001) + f(approaching+0.0001))/2)

limit(approaching)
    