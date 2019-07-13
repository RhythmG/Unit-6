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

from math import exp, sqrt, log
import random



 
"""def Step1(): #EV:EBITDA Rating 
    priprice = float(input("Company's current stock price: "))nt("Welcome to the Stock Rating System!" + "\n" + "In the first step, the program will evaluate the stock in relation to its competitors" + "\n" + "Please enter all the following stock information in billions.")
    price = float(input("Company's current stock price: "))
    shares = float(input("Company's current shares outstanding: "))
    marketcap = shares * price
    stdebt = float(input("Company's total short-term debt: "))
    ltdebt = float(input("Company's total long-term debt: "))
    totdebt = stdebt + ltdebt
    minoi = float(input("Company's minority interest: "))
    prfeq = float(input("Company's preferred equity: "))
    cashinv = float(input("Company's total cash and short-term investments: "))
    EV = marketcap + totdebt + minoi + prfeq - cashinv
    EBITDA = float(input("Enter the current EBITDA for this stock: "))
    s1ratio = EV/EBITDA
    cptr1 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    cptr2 = float(input("Enter the EV:EBITDA ratio for the 2nd competitor of the stock: "))
    cptr3 = float(input("Enter the EV:EBITDA ratio for the 3rd competitor of the stock: "))
    cptr4 = float(input("Enter the EV:EBITDA ratio for the 4th competitor of the stock: "))
    cptr5 = float(input("Enter the EV:EBITDA ratio for the 5th competitor of the stock: "))
    competoverall = (cptr1 + cptr2 + cptr3 + cptr4 + cptr5)/5
    step1pdiff = ((s1ratio - competoverall)/competoverall)*100
    rating1 = (-0.125*step1pdiff) + 5
    print("")
    print(round(step1pdiff, 2), "%")
    print("")
    print("Step 1 Rating:", round(rating1, 2))

#Have the following information at hand before running part 2:
#Operating cash flow for the past 4 years
   
def Step2(): #DCF Rating (Non-cyclical stocks only)
    print("In the second step, the program will perform DCF analysis on non-cyclical stocks.", "\n", "a) Consumer Cyclical, Tech, Basic Materials, Energy, Industrials", "\n", "b) Healthcare, Telecomm, Consumer Defense", "\n", "c) Finance")
    sector = float(input("Please indicate the letter containing the sector in which your stock falls into."))
    if sector == "a":
        print("Because your stock is cyclical, we will skip to the last step.")  
        Step3()
    elif sector == "b":
        avgoper = float(input("Enter the company's average operating cash flow for the past four years"))
        n = 20
        dcf = sum([avgoper/(1+0.06)**(i) for i in range(1,n+1)])
        print(dcf)
    elif sector == "c":
        avgoper = float(input("Enter the company's average operating cash flow for the past four years")"""
        

def Step3(): #VaR Rating
    print("In the last step, the program will evaluate how risky your stock is. Please enter the following.", "\n")
    price = 120.47
    drift = 0.05/365
    walks = []
    sims = []
    meanchange = 4.8048
    stdchange = 0.08
    T = 0
    time = 1
    trials = 65
   
    """meanchange = float(input("Mean % change in stock price: "))
    stdchange = float(input("Standard deviation % change in stock price: "))
    time = float(input("Specify a time frame to forecast this stock (in days, short-term recommended): "))
    trials = int(input("Specify a number of trials to run this simulation: "))"""
    
    while T < 50:
        for i in range(1, trials + 1):
            gbm = price * exp(stdchange*sqrt(time)*random.uniform(-0.5,0.5) + drift*time)
            walks.append(gbm)
            price = gbm
        sims.append(walks[trials-1])
        walks.clear()
        price = 120.47
        T += 1
    print(sims)
    lower = round(sims[(trials*0.05)-1],3) #What if not divisble by 5?
    upper = round(sims[(trials*0.95)-1],3)
    loglower = (sum(sims)/trials) 
    logupper = (sum(sims)/trials) + ((stdchange)**(2)/2) + upper * sqrt(((stdchange)**(2)/trials) + ((stdchange)**(4)/(2*(trials-1))))
    print("(", loglower,",", logupper,")")

    
'''Step1()'''
'''Step2()'''
Step3()
    







