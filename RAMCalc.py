#Stephen Wang
#Calculus 10 Essential Problems Project
#RAM Calculator


#Enter your function after 'return' in line 9: (use ** to denote an exponent)

print('1: Rectangles')
print('2: Trapezoid')
print("3: Simpson's Rule")

typeapprox = int(input('Enter a number corresponding to your desired approximation: '))

def f(x):
    return x**3

if typeapprox == 1:
    print('')
    lower = float(input('Enter a lower bound: '))
    upper = float(input('Enter an upper bound: '))
    intervals = int(input('Enter a number of rectangles to approximate: '))
    
    def integral(a, b, numofrectangles):
        width = (b-a)/numofrectangles
        sum = 0
        for i in range(numofrectangles):
            height = f(a + i*width)
            area = height*width
            sum += area
        print('')
        print(sum)
    
    integral(lower, upper, intervals)

if typeapprox == 2:
    print('')
    lower = float(input('Enter a lower bound: '))
    upper = float(input('Enter an upper bound: '))
    intervals = int(input('Enter a number of trapezoids to approximate: '))
    def trapezoid(a, b, numoftraps):
        width = (b-a)/numoftraps
        sum = 0
        sum += f(a) + f(b)
        for i in range(numoftraps-2):
            height = 2*f(a + i*width)
            area = height*width
            sum += area
        print('')
        print(sum)
    
    trapezoid(lower, upper, intervals)

if typeapprox == 3:
    print('')
    lower = float(input('Enter a lower bound: '))
    upper = float(input('Enter an upper bound: '))
    intervals = int(input('Enter a number of Simpson shapes to approximate: '))
    def simpson(a, b, numoftraps):
        width = (b-a)/numoftraps
        sum = 0
        for i in range(numoftraps):
            height = f(a + i*width)
            area = height*width
            sum += area
        print('')
        print(sum)
    
    simpson(lower, upper, intervals)
         
