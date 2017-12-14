#Problem 5
#part b
nInteger = int(input("Please enter a positive integer n: "))
n = 1
cube = (n**3)
while(cube < nInteger):
    print(cube)
    n = n + 1
    cube = (n**3)
