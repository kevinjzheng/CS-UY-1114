#Problem 5: Write a program that asks the user to enter a number of quarters, dimes, nickels and pennies
# and then outputs the monetary value of the coins in the format of dollars and remaining cents.

quarters = int(input("Please enter the # of quarters: "))
dimes = int(input("Please enter the # of dimes: "))
nickels = int(input("Please enter the # of nickels: "))
pennies = int(input("Please enter the # of pennies: "))
quartersTot = int(quarters * 25)
dimesTot = int(dimes * 10)
nickelsTot = int(nickels * 5)
totalCents = int((quartersTot + dimesTot + nickelsTot + pennies))
totalDollars = int(totalCents / 100)
remCents = (totalCents % 100)

print("The total is",totalDollars, "dollars and", remCents, "cents.")
#print(quartersTot,nickelsTot,dimesTot,pennies,totalCents)
