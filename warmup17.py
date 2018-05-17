#Stephen Wang
#5/17/18
#Find all words that contain every letter of last name

file = open('engmix.txt')

for line in file:
    if 'w' in line and 'a' in line and 'n' in line and 'g' in line:
         print(line.strip())
