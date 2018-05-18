#Stephen Wang
#5/18/18
#Quiz from last year

file = open('engmix.txt')
words = []

for line in file:
    line = line.strip()
    if line.count('c') == 3 and line.count('p') == 2:
        print(line)

