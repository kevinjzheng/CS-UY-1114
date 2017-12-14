#Problem 3

dividend = int(input("Please enter a positive integer as the dividend: "))
divisor = int(input("Please enter a positive integer as the divisor: "))
quotient = 0
difference = dividend - divisor
n = 0
while (difference >= 0):
    difference = difference - divisor
    n = n + 1
    #print(n)

print("Quotient of",dividend,"divided by", divisor, "is:",n)