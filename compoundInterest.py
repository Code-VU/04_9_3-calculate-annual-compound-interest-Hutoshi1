'''
Principle (amount): 1200
Time:               2
Rate:               5.4
Compound Interest:  133.1
---
Principle (amount): 12345
Time:               8
Rate:               6.7
Compound Interest:  8394.89
---
Principle (amount): 50
Time:               1
Rate:               1
Compound Interest:  0.5
'''

'''
A = P( 1 + R/100)^T

CI = A - P

A is Amount
P is Principal Amount
R is Interest Rate
T is Time Span in Years
CI is Compound Interest
'''

def calculateCompoundInterest():
    numOfClients = 3

    while numOfClients > 0:

        client_one_principal = float(input("Principle (amount): "))
        client_one_time =      float(input("Time:               "))
        client_one_rate =      float(input("Rate:               "))

        compoundIntCalc(client_one_principal, client_one_time, client_one_rate)
        if numOfClients > 1:
            print("---")
        numOfClients = numOfClients - 1

def compoundIntCalc(principal, time, rate) ->float:

    amount = principal*( 1 + rate/100)**time
    compoundIntTotal = round(amount - principal, 2)

    print(f"Compound Interest: {compoundIntTotal}")

 #print("Compound Interest: "+str(intrest))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
