#Stephen Wang
#5/10/18
#Asks the user for the name of a file and prints the lines in reverse

ask = input("Enter the name of a file: ")
file = open(ask)

for line in file:
    lines = line.split()
    for item in lines:
        lines.reverse()
        print(item)
 

