from decimal import Decimal

# Declare Variables
AmountOwedEntry = None
AmountOwed = None
AmountTenderedEntry = None
AmountTendered = None
CurrencyTypes = ["$100's", "$50's", "$20's", "$10's", "$5's", "$1's", "Quarters", "Dimes", "Nickels", "Pennies"]
CurrencyCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
AmountChange = None
AmountCalculated = None

# Get the amount owed.
AmountOwedEntry = input("Please enter the total purchase amount: $")
AmountOwed = Decimal(AmountOwedEntry)

# Get the amount tendered.
AmountTenderedEntry = input("Please enter the amount tendered: $")
AmountTendered = Decimal(AmountTenderedEntry)

# Calculate the change.
AmountChange = AmountTendered - AmountOwed
print("The change amount is: $"+str(AmountChange))

# Figure out the Change Currency
AmountCalculated = (int(AmountChange*100)) / 100
while AmountCalculated > 0:
    if AmountCalculated >= 100:
        CurrencyCounts[0] = CurrencyCounts[0] + 1
        AmountCalculated -= 100
    elif AmountCalculated >= 50:
        CurrencyCounts[1] = CurrencyCounts[1] + 1
        AmountCalculated -= 50
    elif AmountCalculated >= 20:
        CurrencyCounts[2] = CurrencyCounts[2] + 1
        AmountCalculated -= 20
    elif AmountCalculated >= 10:
        CurrencyCounts[3] = CurrencyCounts[3] + 1
        AmountCalculated -= 10
    elif AmountCalculated >= 5:
        CurrencyCounts[4] = CurrencyCounts[4] + 1
        AmountCalculated -= 5
    elif AmountCalculated >= 1:
        CurrencyCounts[5] = CurrencyCounts[5] + 1
        AmountCalculated -= 1
    elif AmountCalculated >= 0.25:
        CurrencyCounts[6] = CurrencyCounts[6] + 1
        AmountCalculated -= 0.25
    elif AmountCalculated >= 0.10:
        CurrencyCounts[7] = CurrencyCounts[7] + 1
        AmountCalculated -= 0.10
    elif AmountCalculated >= 0.05:
        CurrencyCounts[8] = CurrencyCounts[8] + 1
        AmountCalculated -= 0.05
    elif AmountCalculated >= 0.01:
        CurrencyCounts[9] = CurrencyCounts[9] + 1
        AmountCalculated -= 0.01
    else:
        print(AmountCalculated)
        AmountCalculated = 0

# Print out the response
indexPosition = 0
print("Please give the customer the following currencies: ")
for each in CurrencyTypes:
    if CurrencyCounts[indexPosition] != 0:
        print(each + ": " + str(CurrencyCounts[indexPosition]))
    indexPosition += 1