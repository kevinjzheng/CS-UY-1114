#Problem 1

#language chooser
lang = input("Please enter a language: ")
if(lang == "en"):
    print("Hello, World!")
elif(lang == "es"):
    print(" ¡Hola mundo!")
else:
    print("Bonjour!")

#odd or even
number = int(input("Please enter a number: "))
if(number % 2 == 0):
    print("Even")
else:
    print("Odd")

#Problem 2: Given current year and graduation year you determine the year that the student is

name = input("Please enter your name: ")
gradYear = int(input("Please enter your graduation year: "))
currYear = int(input("Please enter current year: "))
collegeStatus = ""

if(gradYear - currYear == 4):
    collegeStatus = "Freshman"
elif(gradYear - currYear == 3):
    collegeStatus = "Sohpmore"
elif(gradYear - currYear == 2):
    collegeStatus = "Junior"
elif(gradYear - currYear == 1):
    collegeStatus = "Senior"
elif(gradYear > currYear):
    collegeStatus = "Graduated"
elif(gradYear - currYear > 4):
    collegeStatus = "Not yet in College"
print( name, "is a", collegeStatus)

#Problem 3:
import math
legA = float(input("Please enter the first leg: "))
legB = float(input("Please enter the second leg: "))
hypo = float(input("Please enter the hypotenuse: "))
willNot = ""
legC = float(legA**2 + legB**2)

if(math.sqrt(legC) - (hypo) < 0.001):
    willNot = "will"
else:
    willNot = "not"

print(legA,",",legB, "and", hypo, willNot,"form a right triangle.")

#Problem 4:

numA = int(input("Please enter a: "))
numB = int(input("Please enter b: "))
solution = ""

if(numA == 0):
    solution = "no solution" and print("The equation has no solution.")
elif(numA == 0 and numB == 0):
    solution = "infinite solution" and print("The equation has infinite solutions.")
else:
    solution = "one solution" and print("The equation has", solution, "and x =" , (- numB / numA))

#Problem 5:

monthInt = int(input("Please enter an integer between 1 and 12 (inclusive): "))
monthName = ""
monthDays = 0
if(monthInt == 12):
    monthName = "December"
    monthDays = 31
elif(monthInt == 11):
    monthName = "November"
    monthDays = 30
elif(monthInt == 10):
    monthName = "October"
    monthDays = 31
elif(monthInt == 9):
    monthName = "September"
    monthDays = 30
elif(monthInt == 8):
    monthName = "August"
    monthDays = 31
elif(monthInt == 7):
    monthName = "July"
    monthDays = 31
elif(monthInt == 6):
    monthName = "June"
    monthDays = 30
elif(monthInt == 5):
    monthName = "May"
    monthDays = 31
elif(monthInt == 4):
    monthName = "April"
    monthDays = 30
elif(monthInt == 3):
    monthName = "March"
    monthDays = 31
elif(monthInt == 2):
    monthName = "February"
    monthDays = 28
elif(monthInt == 1):
    monthName = "January"
    monthDays = 31

print("The entered month is", monthName, "and the number of days in",monthName, "is", monthDays)

#Problem 6
shape = ""
numSides = int(input("Enter the number of sides: "))
if(numSides == 3):
    shape = "triangle"
elif(numSides == 4):
    equalSides = input("Are the sides equal? (Y/N): ")
    angleDeg = input("Are the angle 90 degrees? (Y/N): ")
    if(equalSides == "Y" and angleDeg == "Y"):
        shape="square"
    elif(equalSides == "N" and angleDeg == "Y"):
        shape="rectangle"
    else:
        shape="quadrilateral"
else:
    shape = "pentagon"
print("The shape is", shape)

#Problem 7
time24 = int(input("Please enter time in 24 hours format: "))
hour24 = (time24 // 100)
minutes = (time24 % 100)
hour12 = 0
amPm = ""
if(hour24 == 12):
    hour12 = hour24
    amPm = "pm"
elif(hour24 > 12):
    hour12 = hour24 - 12
    amPm = "pm"
elif(hour24 == 0):
    hour12 = 12
    amPm = "am"
elif(hour24 < 12):
    hour12 = hour24
    amPm = "am"

if(minutes < 10):
    minutes = "0" + str(minutes)

print(hour24,":",minutes,"in 12 hr format is", hour12,":",minutes,amPm,)

