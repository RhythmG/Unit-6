#Stephen Wang
#Math Modeling: Stock Rating System

#marketcap = shares * price
#totaldebt = stdebt + ltdebt
#+ Minority Shares
#+ Preferred Equity
#- Cash & Short-Term Investments 
#Enter EBITDA
#Enter the ratio for 4 or 5 other competitors
#% diff EV: EBITDA to competitor average

from math import *

def Step1(): #EV to EBITDA ratio rating
    print("Welcome to the Stock Rating System!")
    shares = float(input("To start, please enter the company's current shares outstanding: (in billions) "))
    price = float(input("Next, input the stock's current price: "))
    marketcap = shares * price
    print("We are done with market capitalization. Now let's get information on the company's debt.")
    stdebt = float(input("Now, input the company's short term debt: "))
    ltdebt = float(input("Now, input the company's long term debt: "))
    totaldebt = stdebt + ltdebt
    minorinter = float(input("Now, input the company's minority interest: "))
    prfereq = float(input("Now, input the company's preferred equity: "))
    cashoinv = float(input("Now, input the company's total cash and short-term investments: "))
    EV = marketcap + totaldebt + minorinter + prfereq - cashoinv
    competratio1 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio2 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio3 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio4 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio = (competratio1+competratio2+competratio3+competratio4)
    

Step1()
print(EV)
    







