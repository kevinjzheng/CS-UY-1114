#Problem 5: Write a program that reads number of days, hours, minutes each of them worked, and prints the total time both of them worked together as days, hours, minutes.

#user inputs
johnDays = int(input("Please enter the number of days that John worked: "))
johnHours = int(input("Please enter the number of hours that John worked: "))
johnMins = int(input("PLease enter the number of minutes that John worked: "))
billDays = int(input("Please enter the number of days that Bill worked: "))
billHours = int(input("Please enter the number of hours that Bill worked: "))
billMins = int(input("PLease enter the number of minutes that Bill worked: "))

#conversions to all minutes
johnTotal = int((johnDays * 1440) + (johnHours * 60) + johnMins)
billTotal = int((billDays * 1440) + (billHours * 60) + billMins)

#combined values
combineTotal = johnTotal + billTotal
combineDays = int(combineTotal/1440)
leftDays = int(combineTotal % 1440)
combineHours = int(leftDays / 60)
leftHours = int(leftDays % 60)
combineMins = leftHours

#print final
print("The total time both of them worked together is:",combineDays,"days,",combineHours,"hours and",combineMins,"minutes.")