#Stephen Wang
#5/10/18
#Asks the user for the name of a file and prints the lines in reverse

ask = input("Enter the name of a file: ")
file = open(ask)

for line in file:
    words = line.split()
    for i in range(len(line), -1):
        print(words[i])
