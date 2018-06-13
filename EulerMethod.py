#Stephen and Maia
#Calculus Programming Week
#Euler's Method

from math import *

def df(x):
    return sin(x)

initialx = float(input('Enter an initial x value: '))
initialy=float(input("enter an initial y value: "))
dx=float(input("Enter a dx value: "))
finalx=float(input("Enter a final x value: "))

def euler(initialx,initialy,dx,finalx):
    x=initialx
    y=initialy
    while x<(finalx-dx):
        dy=df(x)*dx
        y+=dy
        x+=dx
        print("(",round(x,4),",",round(y,4),")")


euler(initialx,initialy,dx,finalx)