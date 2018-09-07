from random import randint

L = [1]
n = int(input('Enter a number of birds: '))

for i in range(1, n+1):
    L.append(randint(1,2))

L.append(2)
print(L)



