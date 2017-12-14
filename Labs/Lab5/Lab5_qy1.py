#Problem 1

n = int(input("Please enter an integer n: "))
line = ""
for i in range (1,n+1):
    line = line + str(i)
    print(line)
    n = n - 1