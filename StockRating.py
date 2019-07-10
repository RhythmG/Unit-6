#Stephen Wang
#Math Modeling: Stock Rating System

#Have the following information at hand before running this program:
#Stock's industry 
#Current shares outstanding and stock price
#Short-Term and Long-Term Debt
#Minority Shares
#Preferred Equity
#Cash & Short-Term Investments 
#EBITDA
#EV:EBITDA ratio for 5 other competitors

from math import *

def Step1(): #EV to EBITDA ratio rating
    print("Welcome to the Stock Rating System!")
    print("Please enter all the following information in billions.")
    shares = float(input("Company's current shares outstanding: "))
    price = float(input("Company's current stock price: "))
    marketcap = shares * price
    stdebt = float(input("Company's total short-term debt: "))
    ltdebt = float(input("Company's total long-term debt: "))
    totaldebt = stdebt + ltdebt
    minorinter = float(input("Company's minority interest: "))
    prfereq = float(input("Company's preferred equity: "))
    cashoinv = float(input("Company's total cash and short-term investments: "))
    EV = marketcap + totaldebt + minorinter + prfereq - cashoinv
    EBITDA = float(input("Enter the current EBITDA for this stock: "))
    step1ratio = EV/EBITDA
    cptratio1 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    cptratio2 = float(input("Enter the EV:EBITDA ratio for the 2nd competitor of the stock: "))
    cptratio3 = float(input("Enter the EV:EBITDA ratio for the 3rd competitor of the stock: "))
    cptratio4 = float(input("Enter the EV:EBITDA ratio for the 4th competitor of the stock: "))
    cptratio5 = float(input("Enter the EV:EBITDA ratio for the 5th competitor of the stock: "))
    competoverall = (cptratio1 + cptratio2 + cptratio3 + cptratio4 + cptratio5)/5
    step1pdiff = ((step1ratio - competoverall)/competoverall)*100
    rating1 = (-0.125*step1pdiff) + 5
    print(round(step1pdiff, 2), "%")
    print("")
    print("Step 1 Rating:", rating1)
    
#def Step2(): #DCF Rating (Non-cyclical stocks only)

#def Step3(): #VaR Rating

    

Step1()
    







