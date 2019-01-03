#Stephen Wang
#Math Modeling: Stock Rating System

#Have the following information at hand before running this program:
#Current shares outstanding and stock price
#Short-Term and Long-Term Debt
#Minority Shares
#Preferred Equity
#Cash & Short-Term Investments 
#EBITDA
#EV:EBITDA ratio for 4 other competitors

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
    EBITDA = float(input("Enter the EV:EBITDA ratio for this stock: "))
    EV:EBITDA = EV/EBITDA
    competratio1 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio2 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio3 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio4 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    compEV:EBITDA = (competratio1+competratio2+competratio3+competratio4)/4
    % diff = (
    

Step1()
    







