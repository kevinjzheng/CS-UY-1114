#Problem 6: Write a program that asks the user to enter an amount of money in the format of dollars and remaining cents.
# The program should calculate and print the minimum number of coins (quarters, dimes, nickels and pennies)
# that are equivalent to the given amount.

dollars = int(input("Please enter the # of dollars: "))
cents = int(input("Please enter the # of remaining cents: "))
dollarCents = int(dollars * 100)
totalCents = int(dollarCents + cents)
quarters = int(totalCents / 25)
leftQuarters = int(totalCents % 25)
dimes = int(leftQuarters / 10)
leftDimes = int(leftQuarters % 10)
nickels = int(leftDimes / 5)
leftNickels = int(leftDimes % 5)
pennies = int(leftNickels)

print(dollars, "dollars and", cents, "cents are:", quarters, "quarters,", dimes , "dimes,", nickels, "nickels and", pennies, "pennies.")
#print(quarters,leftQuarters,dimes,leftDimes,nickels,leftNickels,pennies,totalCents)
