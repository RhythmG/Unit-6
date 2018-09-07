#Math Modeling Proj #1
#Problem 5: Birds on a Wire
#Looking direction: 1 = Right, 2 = Left

from random import randint

n = int(input('Enter a number of birds: ')) #number of birds on wire
t = int(input('How many times do you want to run the simulation? ')) #repeat simulation t times
#average number of birds not looked at
print('')
nlaavg = []

def birds():
    notlookedat = 0 #how many not looked at?
    L = [1] #first bird always looks right
    for i in range(1, n+1):
        L.append(randint(1,2))
    
    L.append(2) #last bird always looks left
    print(L)
    
    for i in range(1, n): #Cases where bird is not looked at 11, 22, 221, 211
        if L[i-1] == 2 and L[i+1] == 1:
            notlookedat = notlookedat + 1
    if L[0] == 1 and L[1] == 1:
        notlookedat = notlookedat + 1
    if L[n] == 2 and L[n+1] == 2:
        notlookedat = notlookedat + 1
    nlaavg.append(notlookedat)
    print(notlookedat)
    print('')

for i in range(1, t+1):
    birds()
    
print('Avg. Not looked at: ', sum(nlaavg)/t)
    


