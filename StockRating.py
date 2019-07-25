from math import ceil
from scipy.stats import norm
import random
import sys

def clamp(n, minn, maxn):
  return max(min(maxn, n), minn)

price = 33.87 #Stock price
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
cptr5 = 8.75 #Competitor 5 EV:EBITDA; Source: Marketwatch
competoverall = (cptr1 + cptr2 + cptr3 + cptr4 + cptr5)/5 
step1pdiff = ((s1ratio - competoverall)/competoverall)*100
rating1 = clamp((-0.125*step1pdiff) + 5, 0.00, 10.00)
print("")

#Step 2: DCF Rating (Non-cyclical stocks only)
avgoper = 39.47 #average operating cash flow for past 4 years
print('\033[0m' "a) Consumer Cyclical, Tech, Basic Materials, Energy, Industrials", "\n", "b) Healthcare, Telecomm, Consumer Defense, Finance")
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
    disc_rate = 0.0541 #Source: https://www.stockcalc.com/wacc.aspx
    dcf = sum([avgoper/(1+disc_rate)**(i) for i in range(1,n+1)])

step2pdiff = round(((dcf-marketcap)/marketcap)*100,2)
rating2 = clamp((0.133*step2pdiff) + 6.667, 0.00, 10.00)
  
print('\033[1m' + "Step 1 Rating:", round(rating1, 2))
print('\033[1m' + "Step 2 Rating: ", round(rating2, 2))

#Step 3: Expected Shortfall Rating
time = 756 #number of days in historical data
fifth = ceil(time*0.05)
sumd = -1.2705 #sum of daily % changes up to 5th percentile 
c_var = (1/fifth)*sumd*100 #Expected shortfall, taken from the 5th %-tile of the historical % change 
rating3 = clamp(c_var + 10, 0.00, 10.00)
print('\033[1m' + "Step 3 Rating: ", round(rating3, 2),'\n')

#Step 4: Monte Carlo VaR Rating
print("\n")
price = 112.54
mean_change = 0.0019 #mean % change of historical
volatility = 0.0130 #standard deviation of historical 
walks = []
sims = []
T = 0
time = 1 #number of days for each step
trials = 60 #number of days in the future

while T < 1000:
  for i in range(1, trials+1):
    gbm = price * (1+norm.ppf(random.random(), mean_change, volatility))
    walks.append(gbm)
    price = gbm
  T += 1
  price = 112.54
  sims.append(walks[trials-1])
  walks.clear()
avgsimsprice = round(sum(sims)/len(sims),2)
print("Avg. Stock Price (after", trials, "days): ", avgsimsprice)
print("Return: ", round(((avgsimsprice-price)/price)*100,2),"%")

#Final Rating
final_rating = (rating1 + rating2 + rating3)/3
print('\033[1m' + "Final Rating: ", round(final_rating, 2))
