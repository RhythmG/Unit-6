#Stephen Wang
#Math Modeling: Stock Rating System

#NOTE: Anything with an input statement only serves as a placeholder for data retrieval
#Have the following information at hand before running this program (part 1):
#Stock's industry 
#Current shares outstanding and stock price
#Short-Term and Long-Term Debt
#Minority Shares
#Preferred Equity
#Cash & Short-Term Investments 
#EBITDA
#EV:EBITDA ratio for 5 other competitors

from math import exp, sqrt, log, floor, ceil
import random

price = 121.46 #Stock price
shares = 0.911 #Shares outstanding
marketcap = shares * price
stdebt = 4.16 #Short-term debt
ltdebt = 35.99 #Long-term debt 
totdebt = stdebt + ltdebt
minoi = 0.134 #Minority interest
prfeq = 0 #Preferred equity 
cashinv = 14.66 #Cash and investments 

print("Welcome to the Stock Rating System!")
print("Step 1: Evaluates the stock in relation to its competitors.")
print("Step 2: Performs DCF analysis on non-cyclical stocks.")
print("Step 3: Looks at the future risk of the stock.")
  
#Step 1: EV-to-EBITDA Rating 
EV = marketcap + totdebt + minoi + prfeq - cashinv
EBITDA = 16.79 
s1ratio = EV/EBITDA
cptr1 = 7.68 #Competitor 1 EV:EBITDA
cptr2 = 10.80 #Competitor 2 EV:EBITDA
cptr3 = 15.22 #Competitor 3 EV:EBITDA
cptr4 = 11.29 #Competitor 4 EV:EBITDA
cptr5 = 12.37 #Competitor 5 EV:EBITDA
competoverall = (cptr1 + cptr2 + cptr3 + cptr4 + cptr5)/5 #Competitor Average
step1pdiff = ((s1ratio - competoverall)/competoverall)*100 # % diff w/ competitors
print("")
rating1 = (-0.125*step1pdiff) + 5 

#Have the following information at hand before running part 2:
#Operating cash flow for the past 4 years

#Step 2: DCF Rating (Non-cyclical stocks only)
marketcap = 33.24972
avgoper = 3.77275 #average operating cash flow for past four years
print('\033[0m' "a) Consumer Cyclical, Tech, Basic Materials, Energy, Industrials", "\n", "b) Healthcare, Telecomm, Consumer Defense", "\n", "c) Finance")
sector = str(input("Please indicate the letter containing the sector in which your stock falls into."))
print('\n')
n = 20
if sector == "a":
    print("Because your stock is cyclical, we will skip to the last step.")
    Step3()
elif sector == "b":
    dcf = sum([avgoper/(1+0.06)**(i) for i in range(1,n+1)])
    print("DCF: ", dcf)
elif sector == "c":
    dcf = sum([avgoper/(1+0.12)**(i) for i in range(1,n+1)])
step2pdiff = round(((dcf-marketcap)/marketcap)*100,2)
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
