#Stephen Wang + Maia Reynolds
#Calculus Programming Week
#Length of a Curve

from math import *

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


