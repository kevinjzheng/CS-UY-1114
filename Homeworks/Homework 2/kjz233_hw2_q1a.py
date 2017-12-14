#Problem 1a: Calculating BMI with weight in kg and height in m.

weight = float(input("Please enter a weight in kilograms: "))
height = float(input("Please enter a height in meters: "))

#calculate BMI
calc = weight / (height ** 2)

#print final
print("BMI is:", calc)
