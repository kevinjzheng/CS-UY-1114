#Problem 4: Determining the number of possible real solutions given a,b,c in the form of a quadratic equation.
import math

#variables
root2 = ""
root1 = ""
varA = float(input("Please enter value of a: "))
varB = float(input("Please enter value of b: "))
varC = float(input("Please enter value of c: "))

numSol = ""
discriminant = (varB ** 2 - 4 * varA * varC)

#testing for solutions
if(varA == 0 and varB == 0 and varC == 0):
    numSol = "infinite solutions"
    root2 = ""
    root1 = ""
elif(varA == 0 and varB == 0):
    numSol = "no solutions"
elif(discriminant > 0):
    numSol = "two real solutions x:"
    root1 = (-varB + (math.sqrt(discriminant))) / (2 * varA)
    root2 = (-varB - (math.sqrt(discriminant))) / (2 * varA)
elif(discriminant == 0):
    numSol = "one real solution x:"
    root1 = (-varB + (math.sqrt(discriminant))) / (2 * varA)
    root2 = (-varB - (math.sqrt(discriminant))) / (2 * varA)
elif(discriminant < 0):
    numSol = "no real solutions"

if(root1 == root2):
    root2 = ""

#print final
print("This equation has", numSol,root1,",", root2 )
