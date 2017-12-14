#Problem 4: Write a program that takes years as input (as a integer) and prints out an estimated population (as an integer).

year = int(input("Please enter the year: "))
currentYear = 2017
currentPop = 307357870
birth = int(31536000 / 7)
death = int(31536000 / 13)
immigrants = int(31536000 / 35)
popChange = int( (year - currentYear) * ((birth + immigrants) - death) )
estPop = int(currentPop + popChange)

print("The estimated population during", str(year), "is", str(estPop) + ".")
#print(currentPop,popChange,estPop)

