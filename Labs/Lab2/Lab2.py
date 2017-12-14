#Lab 2

#Problem 1
import math;
radius = int(input("Please enter an integer as the radius: "))
circum = int(2 * (math.pi) * radius)
area = ((math.pi) * (radius**2))
print("Circumference of the circle is:", circum, "and the area of the circle is", area)

#Problem 2
import turtle;
turtle.left(72);
turtle.forward(100);
turtle.left(72);
turtle.forward(100);
turtle.left(72);
turtle.forward(100);
turtle.left(72);
turtle.forward(100);
turtle.left(72);
turtle.forward(100);
turtle.done(); #holds the turtle window until you close it for the program to continue processing

#Problem 3
days = int(input("Please enter the number of days: "))
week = days // 7
daysLeft = int(days % 7)
print(days, "days is equal to", week, "week and", daysLeft, "days")

#Problem 4
decInt = int(input("Please enter a decimal integer less than 100: "))
fifty = decInt // 50
lessFifty = decInt % 50
ten = lessFifty // 10
lessTen = lessFifty % 10
five = lessTen // 5
lessFive = lessTen % 5
one = lessFive

#print(fifty,ten,five,one)
print(decInt,"in Roman Numeral is:", fifty * "L" + ten * "X" + five * "V" + one * "I")

#Problem 5a
print("Please enter in the format of yyyy/mm/dd")
dob = int(input("Please enter a date of birth: "))
todayDate = int(input("Please enter today's date: "))
day = dob % 100
month = (dob % 10000) // 100
year = (dob // 10000)
todayDay = todayDate % 100
todayMonth = (todayDate % 10000) // 100
todayYear = todayDate // 10000

#print(day, month,year)
print("Date of birth is", str(month) + "/" + str(day) + "/" + str(year), "\n" + "Today's date is", str(todayMonth) + "/" + str(todayDay) + "/" + str(todayYear) )

#Problem 5b
totDays = int(todayYear * 360 + todayMonth * 30 + todayDay)
totBdays = int(year * 360 + month * 30 + day)
totDiff = int(totDays - totBdays)
ageYears = int(totDiff // 360 )
yearsLeft = int(totDiff % 360)
ageMonths = int(yearsLeft // 30)
monthsLeft = int(yearsLeft % 30)
ageDays =int(monthsLeft)
#print(totDays,totBdays,totDiff)

print("You have been alive for", ageYears, "years", ageMonths,"months", ageDays,"days.")