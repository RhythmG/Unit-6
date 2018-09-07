from random import randint

notlookedat = 0

L = [1]
n = int(input('Enter a number of birds: '))

for i in range(1, n+1):
    L.append(randint(1,2))

L.append(2)
print(L)

for i in range(1, n+1):
    if L[i-1] == 2 and L[i+1] == 1:
        notlookedat = notlookedat + 1

print(notlookedat)


