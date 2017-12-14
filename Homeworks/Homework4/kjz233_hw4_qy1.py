#Problem 1

#PART A
n = int(input("Please enter an integer n: "))
even = 0
while(n > 0):
    even = even + 2
    n = n - 1
    print(even)

#PART B
n = int(input("Please enter an integer n: "))
num = 0
for i in range (1, n + 1):
    num = (2*i)
    print(num)