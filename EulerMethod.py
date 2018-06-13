#Stephen and Maia
#Calculus Programming Week
#Euler's Method

from math import *

def f(x):
    return sin(x)

def derivative(x):
    h = 1/1000
    rise = f(x+h)-f(x) 
    run = h
    slope = rise/run 
    return slope

initialx = int(input('Enter an initial x value: '))
dx=float(input("Enter a dx value: "))
finalx=int(input("Enter a final x value: "))

def euler():
    while x!=finalx:
        y=f(initialx)
        dy=derivative(y)*dx
        y+=dy
        x+=dx
        print("(",x,",",y,")"