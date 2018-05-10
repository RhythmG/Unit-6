#Stephen Wang
#5/10/18
#Prints out all the words in the dictionary that contain zz

file = open('engmix.txt')

for line in file:
    if 'zz' in line:
        print(line.strip())

            


