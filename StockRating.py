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

from math import *

def Step1(): #EV to EBITDA ratio rating
    print("Welcome to the Stock Rating System!")
    shares = float(input("Company's current shares outstanding (in billions): "))
    price = float(input("Company's current stock price: "))
    marketcap = shares * price
    print("We are done with market capitalization. Now let's get information on the company's debt.")
    stdebt = float(input("Company's total short-term debt: "))
    ltdebt = float(input("Company's total long-term debt: "))
    totaldebt = stdebt + ltdebt
    minorinter = float(input("Company's minority interest: "))
    prfereq = float(input("Company's preferred equity: "))
    cashoinv = float(input("Company's total cash and short-term investments: "))
    EV = marketcap + totaldebt + minorinter + prfereq - cashoinv
    EBITDA = float(input("Enter the current EBITDA for this stock: "))
    step1ratio = EV/EBITDA
    competratio1 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio2 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio3 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    competratio4 = float(input("Enter the EV:EBITDA ratio for the 1st competitor of the stock: "))
    compEV:EBITDA = (competratio1+competratio2+competratio3+competratio4)/4
    % diff = ((EV:EBITDA - compEV:EBITDA)/compEV:EBITDA)*100
    

Step1()
    







