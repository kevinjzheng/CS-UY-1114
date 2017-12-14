#Problem 1b: Calculating BMI given weight in lbs. and height in inches.

weightLb = float(input("Please enter a weight in pounds: "))
heightIn = float(input("Please enter a height in inches: "))

#conversions
weightKg = float(weightLb * 0.453592)
heightMe = float(heightIn * 0.0254)

#calculate BMI
bmi = weightKg / (heightMe ** 2)

#print final
print("BMI is:", bmi)
