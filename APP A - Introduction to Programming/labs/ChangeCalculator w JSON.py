# Declare Variables
AmountOwedEntry = 0
AmountOwed = 0
AmountTenderedEntry = 0
AmountTendered = 0
entrySuccess = False
pesos = {"Pesetas":{"qty":0,"value":10000},"Quintos":{"qty":0,"value":1000},"Tostons":{"qty":0,"value":25},"Pesos":{"qty":0,"value":1}}
usd = {"$100's":{"qty":0,"value":10000},"$50's":{"qty":0,"value":5000},"$20's":{"qty":0,"value":2000},"$10's":{"qty":0,"value":1000},"$5's":{"qty":0,"value":500},"$1's":{"qty":0,"value":100},"Quarters":{"qty":0,"value":25},"Dimes":{"qty":0,"value":10},"Nickels":{"qty":0,"value":5},"Pennies":{"qty":0,"value":1}}
currencies = pesos
AmountChange = 0
AmountCalculated = 0
indexPosition = 0

# Manager doesn't want us to use bills over $20
#del usd["$100's"]
#del usd["$50's"]

# Get the amount owed.
while entrySuccess == False:
    AmountOwedEntry = input("Please enter the total purchase amount: $")
    try:
        AmountOwed = int(float(AmountOwedEntry)*100)
        entrySuccess = True
    except:
        print(AmountOwedEntry + " is not a valid currency amount. Please try again.")

# Get the amount tendered.
entrySuccess = False
while entrySuccess == False:
    AmountTenderedEntry = input("Please enter the amount tendered: $")
    try:
        AmountTendered = int(float(AmountTenderedEntry)*100)
        if AmountTendered >= AmountOwed:
            entrySuccess = True
        else:
            print("$" + AmountTenderedEntry + " is less than the amount owed ($" + AmountOwedEntry+"). Please try again.")
    except:
        print(AmountTenderedEntry + " is not a valid currency amount. Please try again.")

# Calculate the change.
AmountChange = AmountTendered - AmountOwed
AmountCalculated = AmountChange
while AmountCalculated != 0:
    for each in currencies:
        foundMatch = False
        if AmountCalculated >= currencies[each]['value']:
            currencies[each]['qty'] = currencies[each]['qty'] + 1
            AmountCalculated = AmountCalculated - currencies[each]['value']
            foundMatch = True
        if foundMatch == True:
            break
AmountChangeDisplayed = AmountChange/100

# Tell them what to do
print("Change: ${:.2f}".format(AmountChangeDisplayed))
print("Please hand the customer: ")
for each in currencies:
    if currencies[each]['qty'] > 0:
        rowString = str(currencies[each]['qty']) + " x " + each
        print(rowString)