#Stephen Wang
#5/10/18
#Asks the user for the name of a file and prints the lines in reverse

ask = input("Enter the name of a file: ")
file = open(ask)
lines = []

for line in file:
    line = line.strip()
    lines.append(line)
lines.reverse()

for item in lines:
    print(item)
 



