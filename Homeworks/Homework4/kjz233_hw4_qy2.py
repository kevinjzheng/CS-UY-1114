#Problem 2

n = int(input("Please enter an integer n: "))
times = 0
hold = n
for i in range(n):
    times = (2*n) - 1
    n = n - 1
    print( (i * " ") + times * "*")
while(n < hold):
    n = n + 1
    times = (2*n) - 1
    print((i * " ") + times * "*")
    i = i - 1