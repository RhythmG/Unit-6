#Stephen and Maia
#Calculus Programming Week
#Euler's Method

from math import *

def df(x):
    return e**(x**2)

initialx = float(input('Enter an initial x value: '))
initialy=float(input("enter an initial y value: "))
dx=float(input("Enter a dx value: "))
finalx=float(input("Enter a final x value: "))

def euler(initialx,initialy,dx,finalx):
    x=initialx
    y=initialy
    while x!=finalx:
        dy=df(x)*dx
        y+=dy
        x+=dx
        print("(",x,",",y,")")
    print("(",x,",",y,")")


euler(initialx,initialy,dx,finalx)