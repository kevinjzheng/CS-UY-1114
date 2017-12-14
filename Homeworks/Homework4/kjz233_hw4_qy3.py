#Problem 3

n = 10
for i in range (1, (n//2) + 1):
    for j in range(1, n+1):
        print(j**i, end="\t")
    print()
