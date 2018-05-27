#Stephen Wang
#Calc - 10 Essential Problems Project
#Summation calculator for select series


#Harmonic Series 

terms = int(input('Enter a number of terms for summing the harmonic series: '))
#WARNING: It is advisable to enter terms to be at most 100000

i = 0
harmonicseries = []

for i in range(1, terms+1):
    harmonicseries.append(1/i)

print('')
print('Harmonic Series: ', sum(harmonicseries))  

#Alternating Harmonic Series

j = 0
altharmonicseries = []

for j in range(1, terms):
    altharmonicseries.append(((-1)**(j+1))*(1/j))

print('')
print('Alt Harmonic Series: ', sum(altharmonicseries))  
print('')
print('Difference: ', sum(harmonicseries)-sum(altharmonicseries))
