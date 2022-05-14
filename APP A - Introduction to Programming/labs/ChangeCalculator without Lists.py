# Include Additional Modules
from decimal import Decimal

# Declare Variables
AmountOwedEntry = None
AmountOwed = None
AmountTenderedEntry = None
AmountTendered = None
dollars100 = 0
dollars50 = 0
dollars20 = 0
dollars10 = 0
dollars5 = 0
dollars1 = 0
coins25 = 0
coins10 = 0
coins5 = 0
coins1 = 0

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
        dollars100 = dollars100 + 1
        AmountCalculated -= 100
    elif AmountCalculated >= 50:
        dollars50 = dollars50 + 1
        AmountCalculated -= 50
    elif AmountCalculated >= 20:
        dollars20 = dollars20 + 1
        AmountCalculated -= 20
    elif AmountCalculated >= 10:
        dollars10 = dollars10 + 1
        AmountCalculated -= 10
    elif AmountCalculated >= 5:
        dollars5 = dollars5 + 1
        AmountCalculated -= 5
    elif AmountCalculated >= 1:
        dollars1 = dollars1 + 1
        AmountCalculated -= 1
    elif AmountCalculated >= 0.25:
        coins25 = coins25 + 1
        AmountCalculated -= 0.25
    elif AmountCalculated >= 0.10:
        coins10 = coins10 + 1
        AmountCalculated -= 0.10
    elif AmountCalculated >= 0.05:
        coins5 = coins5 + 1
        AmountCalculated -= 0.05
    elif AmountCalculated >= 0.01:
        coins1 = coins1 + 1
        AmountCalculated -= 0.01
    else:
        AmountCalculated = 0

# Print out the response
print("Please give the customer the following currencies: ")
print("$100's: " + str(dollars100))
print("$50's: " + str(dollars50))
print("$20's: " + str(dollars20))
print("$10's: " + str(dollars10))
print("$5's: " + str(dollars5))
print("$1's: " + str(dollars1))
print("Quarters: " + str(coins25))
print("Dimes: " + str(coins10))
print("Nickels: " + str(coins5))
print("Pennies: " + str(coins1))