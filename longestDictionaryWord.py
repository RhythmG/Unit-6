#Stephen Wang
#5/10/18
#Prints out the longest word in the dictionary

file = open('engmix.txt')
word = ''

for line in file:
    if len(line)> len(word):
        word = line

print(word)
            
