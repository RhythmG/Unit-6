#Stephen Wang
#Math Modeling: Stock Rating System

#NOTE: Anything below that is a hardwired constant requires data extraction. 
#These pieces of information also have comments attached beside them. 


from math import exp, sqrt, log, floor, ceil
import random
import sys

price = 30.89 #Stock price
shares = 7.28 #Shares outstanding
marketcap = shares * price
stdebt = 0.002 #Short-term debt
ltdebt = 168.51 #Long-term debt 
totdebt = stdebt + ltdebt
minoi = 1.12 #Minority interest
prfeq = 0 #Preferred equity 
cashinv = 8.76 #Cash and investments 

print("Welcome to the Stock Rating System!")
print("Step 1: Evaluates the stock in relation to its competitors.")
print("Step 2: Performs DCF analysis on non-cyclical stocks.")
print("Step 3: Looks at the future risk of the stock.")
  
#Step 1: EV-to-EBITDA Rating 
EV = marketcap + totdebt + minoi + prfeq - cashinv
EBITDA = 50.62
s1ratio = EV/EBITDA
cptr1 = 8.38 #Competitor 1 EV:EBITDA
cptr2 = 8.1 #Competitor 2 EV:EBITDA
cptr3 = 5.24 #Competitor 3 EV:EBITDA
cptr4 = 8.85 #Competitor 4 EV:EBITDA
cptr5 = 8.75 #Competitor 5 EV:EBITDA
competoverall = (cptr1 + cptr2 + cptr3 + cptr4 + cptr5)/5 
step1pdiff = ((s1ratio - competoverall)/competoverall)*100

if step1pdiff <= -40:
  rating1 == 10 
elif step1pdiff >= 40:
  rating1 == 0
else:
  rating1 = (-0.125*step1pdiff) + 5 
  
print("")

#Step 2: DCF Rating (Non-cyclical stocks only)
avgoper = 39.47 #average operating cash flow for past 4 years
print('\033[0m' "a) Consumer Cyclical, Tech, Basic Materials, Energy, Industrials", "\n", "b) Healthcare, Telecomm, Consumer Defense", "\n", "c) Finance")
sector = str(input("Please indicate the letter containing the sector in which your stock falls into."))
print('\n')
n = 20
if sector == "a":
  time = 756 #number of days in historical data
  fifth = ceil(time*0.05)
  sum = -1.2705 #sum of daily % changes up to 5th percentile 
  c_var = (1/fifth)*sum*100 #Expected shortfall, taken from the 5th %-tile of the historical % change 
  rating3 = c_var + 10
  print('\033[1m' + "Step 1 Rating:", round(rating1, 2))
  print('\033[1m' + "Step 2 Rating: ", "Skipped")
  print('\033[1m' + "Step 3 Rating: ", round(rating3, 2),'\n')
  final_rating = (rating1 + rating3)/2
  print('\033[1m' + "Final Rating: ", round(final_rating, 2))
  sys.exit()
elif sector == "b":
    dcf = sum([avgoper/(1+0.066)**(i) for i in range(1,n+1)])
    print(dcf)
elif sector == "c":
    dcf = sum([avgoper/(1+0.12)**(i) for i in range(1,n+1)])

step2pdiff = round(((dcf-marketcap)/marketcap)*100,2)

if step2pdiff >= 25:
  rating2 == 10 
elif step2pdiff <= -50:
  rating2 == 0
else:
  rating2 = (0.133*step2pdiff) + 6.667

print('\033[1m' + "Step 1 Rating:", round(rating1, 2))
print('\033[1m' + "Step 2 Rating: ", round(rating2, 2))

#Step 3: Expected Shortfall Rating
time = 756 #number of days in historical data
fifth = ceil(time*0.05)
sum = -1.2705 #sum of daily % changes up to 5th percentile 
c_var = (1/fifth)*sum*100 #Expected shortfall, taken from the 5th %-tile of the historical % change 
rating3 = c_var + 10
print('\033[1m' + "Step 3 Rating: ", round(rating3, 2),'\n')
    
final_rating = (rating1 + rating2 + rating3)/3
print('\033[1m' + "Final Rating: ", round(final_rating, 2))
