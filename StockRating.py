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

def Step1(): #EV to EBITDA ratio rating
    print("Welcome to the Stock Rating System!")
    shares = print(input("To start, please enter the company's current shares outstanding: "))
    price = print(input("Next, input the stock's current price: "))
    marketcap = shares * price
    print("We are done with market capitalization. Now let's get information on the company's debt.")
    stdebt = print(input("Now, input the company's short term debt: "))
    ltdebt = print(input("Now, input the company's long term debt: "))
    totaldebt = stdebt + ltdebt







