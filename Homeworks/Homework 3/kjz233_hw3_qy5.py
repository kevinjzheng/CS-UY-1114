#Problem 5: Defining triangles given the side lengths
import math

#variables
sideA = float(input("Please enter length of first side: "))
sideB = float(input("Please enter length of second side: "))
sideC = float(input("Please enter length of third side: "))
triType = ""
diffAB = abs(sideA - sideB)
diffBC = abs(sideB - sideC)
diffCA = abs(sideC - sideA)
calcA = (math.degrees(math.acos( (sideB**2 + sideC**2 - sideA**2) / (2*sideB*sideC) )))
calcB = (math.degrees(math.acos( (sideA**2 + sideC**2 - sideB**2) / (2*sideA*sideC) )))
calcC = (math.degrees(math.acos( (sideB**2 + sideA**2 - sideC**2) / (2*sideA*sideB) )))
angleA = round(calcA,2)
angleB = round(calcB,2)
angleC = round(calcC,2)

#testing for triangle type
if(diffAB <= 0.00001 and diffBC <= 0.00001 and diffCA <= 0.00001):
    triType = "equilateral"
elif((diffAB <= 0.00001) or (diffBC <= 0.00001) or (diffCA <= 0.00001)):
    if(angleA == 90.0 or angleB == 90.0 or angleC == 90.0):
        triType = "isosceles right"
    else:
        triType = "isosceles"
else:
    triType = "scalene"

#print(angleA,angleB,angleC)

#print final
print(sideA, "," , sideB,",", sideC,",", "form an", triType, "triangle.")