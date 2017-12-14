#Problem 5
#part c
nInteger = int(input("Please enter a positive integer n: "))
cube = 0
sumCubes = 0
for i in range(nInteger):
    cube = ((i+1)**3)
    sumCubes = sumCubes + cube

print(sumCubes)