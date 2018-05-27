#Stephen Wang
#Calc - 10 Essential Problems Project
#Summation calculator for select series


#Harmonic Series 

terms = int(input('Enter a number of terms for summing the harmonic series: '))
#WARNING: It is advisable to enter terms not exceeding 100000

i = 0
harmonicseries = []

for i in range(1, terms+1):
    harmonicseries.append(1/i)

print('')
print('Harmonic Series: ', sum(harmonicseries))  

#Alternating Harmonic Series

j = 0
altharmonicseries = []

for j in range(1, terms+1):
    altharmonicseries.append(((-1)**(j-1))*(1/j))

print('')
print('Alt Harmonic Series: ', sum(altharmonicseries))  
print('ln 2 = ', 0.69314718056)
print('Error(Alt Series): ', ((0.69314718056-sum(altharmonicseries))/0.69314718056)*100, '%')

#as 'terms' goes to infinity, the error will go to 0 and so the alternating harmonic series converges to ln 2
