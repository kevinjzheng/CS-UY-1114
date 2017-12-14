#Problem 4

n = int(input("Please enter an integer n: "))
line = ""
for i in range (1,n+1):
    line = line + str(i)
    print( ((n-1) * " " ) + line)
    n = n - 1