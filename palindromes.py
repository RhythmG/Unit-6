#Stephen Wang
#5/17/18
#Prints all the palindromes in the dictionary

file = open('engmix.txt')
palindromes = []
word = []

def reverse(word):
    for word in file:
        word = word.strip()
        j = 0
        for i in range(1, 1000):
            if word[i][j] == word[i][len(word)-(j+20)]:
                j = j+1
                return True

for line in file:
    if reverse(word) == True:
        line = line.strip()
        palindromes.append(line)

for item in palindromes:
    print(item)
