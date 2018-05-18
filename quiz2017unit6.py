#Stephen Wang
#5/18/18
#Quiz from last year

file = open('engmix.txt')
rwords = 0

"""
for line in file:
    line = line.strip()
    if line.count('c') == 3 and line.count('p') == 2:
        print(line)
"""

"""        
for line in file:
    if len(line) > 0 and 'r' == line[0]:
        rwords += 1
print(rwords)
"""

num = int(input('Enter a number: '))

for line in file:
    if len(line) == num+1:
        print(line)
        break
