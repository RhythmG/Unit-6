from random import randint

notlookedat = 0
j= 0
k= 0
l= 0

L = [1]
n = int(input('Enter a number of birds: '))

for i in range(1, n+1):
    L.append(randint(1,2))

L.append(2)
print(L)

for i in range(1, n):
    if L[i-1] == 2 and L[i+1] == 1:
        notlookedat = notlookedat + 1
        j = j+1

if L[0] == 1 and L[1] == 1:
    notlookedat = notlookedat + 1
    k = k+1
if L[n] == 2 and L[n+1] == 2:
    notlookedat = notlookedat + 1
    l = l+1

print("Not looked at:", notlookedat)
print(j)
print(k)
print(l)


