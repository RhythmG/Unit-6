from math import ceil
from scipy.stats import norm
import random

rating1 = 5.00
rating2 = 5.00
rating3 = 5.00
rating4 = 5.00

def clamp(n, minn, maxn): #Ratings capped from 0.00 to 10.00
  return max(min(maxn, n), minn)

#Stock: United Technologies ; Ticker: UTX
sector = "Industrials" #Sector

#Step 1 Inputs 
price = 130.50 #Stock price
shares = 0.86291 #Shares outstanding
stdebt =    #Short-term debt
ltdebt =   #Long-term debt 
minoi = 0 #Minority interest
prfeq = 0 #Preferred equity 
cashinv =  #Cash and investments 
EBITDA = 9.50  #EBITDA
cptr1 = 10.24 #Competitor 1 EV:EBITDA 
cptr2 = 10.24 #Competitor 2 EV:EBITDA
cptr3 = 10.24 #Competitor 3 EV:EBITDA
cptr4 = 10.24 #Competitor 4 EV:EBITDA
cptr5 = 10.24 #Competitor 5 EV:EBITDA; Source: Marketwatch

#Step 2 Inputs 
avgoper = 29.843 #Net operating cash flow for past 4 years
disc_rate = 0.0571 #Source: https://www.stockcalc.com/wacc.aspx

#Step 3 Inputs
sumd = -1.1887  #sum of daily % changes up to 5th percentile 

#Step 4 Inputs
mean_change = 0.001262  #mean % change of historical
volatility = 0.01350 #standard deviation of historical 

if sector == "Consumer Cyclical" or "Tech" or "Basic Materials" or "Energy" or "Industrials":
  #Step 1: EV-to-EBITDA Rating 
  marketcap = shares * price 
  totdebt = stdebt + ltdebt
  EV = marketcap + totdebt + minoi + prfeq - cashinv
  s1ratio = EV/EBITDA
  competoverall = (cptr1 + cptr2 + cptr3 + cptr4 + cptr5)/5 
  step1pdiff = ((s1ratio - competoverall)/competoverall)*100
  rating1 = clamp((-0.125*step1pdiff) + 5, 0.00, 10.00)
  print(s1ratio)
  print("")
  
#Step 3: Expected Shortfall Rating
  time = 756 #number of days in historical data
  fifth = ceil(time*0.05)
  c_var = (1/fifth)*sumd*100 #Expected shortfall, taken from the 5th %-tile of the historical % change 
  rating3 = clamp(c_var + 10, 0.00, 10.00)

#Step 4: Monte Carlo VaR Rating
  print("\n")
  price = 45.60 #Stock price
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
    price = 45.60 #Stock price
    sims.append(walks[trials-1])
    walks.clear()
  avgsimsprice = round(sum(sims)/len(sims),2)
  step4pdiff = round(((avgsimsprice-price)/price)*100,2)
  if step4pdiff <= 8.00:
    rating4 = clamp(0.8*step4pdiff, 0.00, 10.00)
  else:
    rating4 = clamp(0.2*step4pdiff + 6, 0.00, 10.00)
  print("Return: ", step4pdiff,"%")
  print('\033[1m' + "Step 1 Rating:", round(rating1, 2))
  print('\033[1m' + "Step 2 Rating: ", "Skipped")
  print('\033[1m' + "Step 3 Rating: ", round(rating3, 2))
  print('\033[1m' + "Step 4 Rating: ", round(rating4, 2),'\n')
  final_rating = (rating1 + rating3 + rating4)/3
  print('\033[1m' + "Final Rating: ", round(final_rating, 2))
else:
#Step 1: EV-to-EBITDA Rating 
  marketcap = shares * price 
  totdebt = stdebt + ltdebt
  EV = marketcap + totdebt + minoi + prfeq - cashinv
  s1ratio = EV/EBITDA
  competoverall = (cptr1 + cptr2 + cptr3 + cptr4 + cptr5)/5 
  step1pdiff = ((s1ratio - competoverall)/competoverall)*100
  rating1 = clamp((-0.125*step1pdiff) + 5, 0.00, 10.00)
  print("")

#Step 2: DCF Rating (Non-cyclical stocks only)
  print('\n')
  n = 20
  dcf = sum([avgoper/(1+disc_rate)**(i) for i in range(1,n+1)])
  step2pdiff = round(((dcf-marketcap)/marketcap)*100,2)
  rating2 = clamp((0.133*step2pdiff) + 6.667, 0.00, 10.00)

#Step 3: Expected Shortfall Rating
  time = 756 #number of days in historical data
  fifth = ceil(time*0.05)
  c_var = (1/fifth)*sumd*100 #Expected shortfall, taken from the 5th %-tile of the historical % change 
  rating3 = clamp(c_var + 10, 0.00, 10.00)

#Step 4: Monte Carlo VaR Rating
  print("\n")
  price = 45.60 #Stock price
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
    price = 45.60 #Stock price
    sims.append(walks[trials-1])
    walks.clear()
  avgsimsprice = round(sum(sims)/len(sims),2)
  step4pdiff = round(((avgsimsprice-price)/price)*100,2)
  if step4pdiff <= 8.00:
    rating4 = clamp(0.8*step4pdiff, 0.00, 10.00)
  else:
    rating4 = clamp(0.2*step4pdiff + 6, 0.00, 10.00)
  print("Return: ", step4pdiff,"%")
  print('\033[1m' + "Step 1 Rating:", round(rating1, 2))
  print('\033[1m' + "Step 2 Rating: ", "Skipped")
  print('\033[1m' + "Step 3 Rating: ", round(rating3, 2))
  print('\033[1m' + "Step 4 Rating: ", round(rating4, 2),'\n')
  final_rating = (rating1 + rating3 + rating4)/3
  print('\033[1m' + "Final Rating: ", round(final_rating, 2))

#str(input("Please indicate the letter containing the sector in which your stock falls into."))
#print('\033[0m' "a) Consumer Cyclical, Tech, Basic Materials, Energy, Industrials", "\n", "b) Healthcare, Telecomm, Consumer Defense, Finance")
