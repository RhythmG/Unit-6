#Stephen Wang
#Calculus 10 Essential Problems Project
#RAM Calculator


#Enter your function after 'return' in line 9: (use ** to denote an exponent)

def f(x):
    return x**3

  
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

    
