#Problem 3

hamDist = 0
intA = int(input("Please enter a first integer: "))
intB = int(input("Please enter a second integer: "))
tempA = intA
tempB = intB


while(tempA > 0 and tempB > 0):
    oneA = tempA % 10
    oneB = tempB % 10
    if(oneA != oneB ):
        hamDist = hamDist + 1
    tempA = tempA // 10
    tempB = tempB // 10
print(hamDist)

