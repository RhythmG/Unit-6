#Stephen Wang
#Math Modeling Project 3, Homework Question 1
import math

decimal = 1
ans = 0
digit = 0
floor = 0
remainder = -1
visitednum = []
print("Enter a fraction in the form of A/B")
numerator = int(input("Enter your numerator: "))
denominator = int(input("Enter your denominator: "))

firstTime = True
    
while remainder != 0:
    if numerator > denominator:
        print('divide')
        floor = decimal * math.floor(numerator/denominator)
        print('floor = ', floor)
        ans = ans + floor
        print('answer = ', ans)
        if not firstTime:
            digit += 1
            print('digit = ', digit)
        else:
            firstTime = False
            print('firstTime')
        remainder = numerator%denominator
        if remainder in visitednum:
            break
        visitednum.append(remainder)
        print(remainder, " saved")
        print('remainder = ', remainder)
        numerator = remainder * 10
        print('numerator = ', numerator)
        decimal = decimal * 0.1
        print('decimal =', decimal)
        
    else:
        if firstTime:
            firstTime = False
        print('inflate numerator')
        visitednum.append(numerator)
        print(numerator, " saved")
        numerator = numerator*10
        decimal = decimal * 0.1
        print('numerator = ', numerator)
        print('decimal = ',decimal)
    
if remainder != 0:
    print("Repeating digit: ", digit)
    print("The answer is: ", ans,"...")
elif remainder == 0:
    print("Non-repeating digit: ", digit)
    print("The answer is: ", ans)






