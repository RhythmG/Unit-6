#Stephen Wang
#Math Modeling: Stock Rating System

#NOTE: Anything with an input statement only serves as a placeholder for automated data retrieval
#Have the following information at hand before running this program (part 1):
#Stock's industry 
#Current shares outstanding and stock price
#Short-Term and Long-Term Debt
#Minority Shares
#Preferred Equity
#Cash & Short-Term Investments 
#EBITDA
#EV:EBITDA ratio for 5 other competitors


def Step1(): #EV to EBITDA ratio rating
    print("Welcome to the Stock Rating System!")
    print("In the first step, the program will evaluate the stock in relation to its competitors")
    print("Please enter all the following stock information in billions.")
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
    print("")
    print(round(step1pdiff, 2), "%")
    print("")
    print("Step 1 Rating:", round(rating1, 2))

#Have the following information at hand before running part 2:
#Operating cash flow for the past 4 years
#

def Step2(): #DCF Rating (Non-cyclical stocks only)
    print("In the second step, the program will perform DCF analysis on non-cyclical stocks. If your interested stock is cyclical, then this skip is unnecessary.")
    print("a) Consumer Cyclical, Tech, Basic Materials, Energy, Industrials")
    print("b) Healthcare, Telecomm, and Consumer Defense")) 
    print("c) Finance")
    sector = float(input("Please indicate the letter containing the sector in which your stock falls into."))
    if sector == "a":
        print("Because your stock is cyclical, we will skip to the last step.")  
        Step3()
    elif sector == "b":
        avgoperation = float(input("Enter the company's average operating cash flow for the past four years")
        total = 0
        for i in range(1, 20):
            i = i + 1
            dcf = sum(avgoperation / (1 + 0.06)**(i))
            total = total + dcf
        print(dcf)
    
    elif sector == "c":
        avgoperation = float(input("Enter the company's average operating cash flow for the past four years")
        
    else:
        print("
        
    
def Step3(): #VaR Rating
    print("In the last step, the program will evaluate how risky your stock is")
    

Step1()
Step2()
    






