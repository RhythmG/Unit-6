#Stephen Wang
#Math Modeling Project 3, Homework Question 1
import math

print("Enter a fraction in the form of A/B")
numerator = int(input("Enter your numerator: "))
denominator = int(input("Enter your denominator: "))
decimal = 1
ans = 0
digit = 0
remainder = -1
visitednum = []

while remainder not in visitednum and remainder != 0:
    floor = 0
    if numerator > denominator:
        floor = decimal * math.floor(numerator/denominator)
        remainder = numerator%denominator
        visitednum.append(remainder)
        digit += 1
    else:
        numerator = numerator*10
        decimal = decimal*0.1
    ans = ans + floor

if remainder == 1:
    print("Repeating digit: ", digit)
    print("The answer is: ", ans,"...")
elif remainder == 0:
    print("Non-repeating digit: ", digit)
    print("The answer is: ", ans)






