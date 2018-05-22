#Stephen Wang
#5/22/18
#Unit 6 Quiz

dictionary = open('engmix.txt')

"""
letter = input('Enter a letter: ')
for line in dictionary:
    if line.count('r') == 4:
        print(line.strip())
"""

"""
for line in dictionary:
    if len(line) >= 9 and line[0] == line[4] == line[8]:
        print(line)
        break
"""

"""
number = int(input('Enter a number: '))
letter = input('Enter a letter: ')
for line in dictionary:
    line.strip()
    if len(line) == number and line[0] == letter:
        print(line.strip())
"""

"""
longwords = []
for line in dictionary:
    line.strip()
    if len(line) >= 10:
        longwords.append(line)
print(longwords[7999])
"""        

"""
word = []
for line in dictionary:
    line.strip()
    if (line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')) > (word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')):
        word = line

print(word)
"""
    
