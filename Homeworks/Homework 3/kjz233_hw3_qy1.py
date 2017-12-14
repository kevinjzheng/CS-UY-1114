#Problem 1: Letting the user know their weight status based on their bmi

weightLb = float(input("Please enter a weight in pounds: "))
heightIn = float(input("Please enter a height in inches: "))

#conversions
weightKg = float(weightLb * 0.453592)
heightMe = float(heightIn * 0.0254)

#calculate BMI
bmi = weightKg / (heightMe ** 2)

#print final
status = ""
if(bmi < 18.5):
    status = "Underweight"
elif(bmi >= 18.5 and bmi <= 24.9):
    status = "Normal"
elif(bmi >= 25.0 and bmi <= 29.9):
    status = "Overweight"
elif(bmi >= 30.0):
    status = "Obese"
print("BMI is:", bmi, "and you are", status,)

