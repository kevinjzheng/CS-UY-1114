#Problem 1
print("Kevin")

#Problem 2
int1 = input("Please enter the first integer: ")
int2 = input("Please enter the second integer: ")
sum = int(int1) + int(int2)
diff = int(int1) - int(int2)
prod = int(int1)* int(int2)
print("Their sum is: " , str(sum) + "," , "their difference is: " , str(diff) +"," , "their product is: ", str(prod))

#Problem 3
tempF = int(input("Please enter a Fahrenheit temperature: "))
tempC = int((tempF - 32) * (5/9))
print("In Celsius it is: " , str(tempC)+ ".", "In Fahrenheit it is: " + str(tempF) + ".")

#Problem 4
weightlb = int(input("Please enter a weight in pounds: "))
weighto = int(weightlb * 16)
weightkg = int(weightlb / 0.45)
print((weightlb) , " pounds is equivalent to " , (weighto) , " and " , (weightkg) , " kilograms")

#Problem 7
feet1 = int(input("Please enter the first length's feet: "))
feet2 = int(input("Please enter the second length's feet: "))
yard1 = int(input("Please enter the first length's yard: "))
yard2 = int(input("Please enter the second length's yard: "))
feetSum = int(feet1 + feet2)
feetYard = int(feetSum/3)
yardSum = int(feetYard + yard1 + yard2)
feetLeft = int(yardSum % 3)
print ("The sum is: " + str(yardSum) + " yards and " + str(feetLeft) + " feet")

print("Finished with lab 1 :)")