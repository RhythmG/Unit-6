#Stephen Wang
#Math Modeling Project 3, Homework Question 1
import math

decimal = 1
ans = 0
digit = 0
floor = 0
unit = 0
remainder = -1
visitednum = []
saveddigits = []
print("Enter a fraction in the form of A/B")
numerator = int(input("Enter your numerator: "))
denominator = int(input("Enter your denominator: "))
repeatedindex = 0
numofrepeateddigits = 0

firstTime = True
    
while remainder != 0:
    if numerator > denominator:
        floor = math.floor(numerator/denominator)
        ans = ans + floor * decimal
        if not firstTime:
            saveddigits.append(floor)
            digit += 1
        else:
            firstTime = False
            unit = floor
        remainder = numerator%denominator
        if remainder in visitednum:
            repeatedindex = visitednum.index(remainder)
            numofrepeateddigits = len(visitednum) - repeatedindex
            print('Finished!')
            break
        visitednum.append(remainder)
        numerator = remainder * 10
        decimal = decimal * 0.1
        
    else:
        if firstTime:
            firstTime = False
        visitednum.append(numerator)
        if decimal < 1.0:
            saveddigits.append(0)
        numerator = numerator*10
        decimal = decimal * 0.1
    
if remainder != 0:
    print('')
    print("# of repeating digits: ", numofrepeateddigits)
    print("# of non-repeating digits: ", len(visitednum)-numofrepeateddigits)
    print("The answer is: ", unit,".", end="")
    for i in range(len(saveddigits)):
        print(saveddigits[i], end='')
    for i in range(len(saveddigits)):
        if i > repeatedindex-1:
            print(saveddigits[i], end='')
    print('...')
    
elif remainder == 0:
    print('')
    print("# of non-repeating digits: ", digit)
    print("The answer is: ", unit,".", end="")
    for i in range(len(saveddigits)):
        print(saveddigits[i], end='')
