#Problem 2

n = int(input("Please enter an integer n: "))
line = ""

for i in range (1,n+1):
    tempHold = i
    n = n - 1
    line = (i * str(tempHold))
    print((n * ".") + line)
