#Problem 2

sumVals = 0
nInt = int(input("Please enter a positive integer for n: " ))
for i in range(nInt):
    vals = ((-1) ** i) * (i+1)
    sumVals = vals + sumVals
    #print(vals)
print("Sum is:", sumVals)

