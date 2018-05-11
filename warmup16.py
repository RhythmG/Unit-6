#Stephen Wang
#5/11/18
#Print all words that start with your first initial and end with your last initial

file = open('engmix.txt')


for word in file:
    word = word.strip()
    if word[0] == 's' and word[len(word)-1]  == 'w':
        print(word)
        