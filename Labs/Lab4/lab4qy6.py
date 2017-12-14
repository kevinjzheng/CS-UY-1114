#Problem 6
n = int(input("Input a dimension: "))
for i in range (1, n+1):
    for j in range(1, n+1):
        if(j==i):
            print("o", end="\t")
        else:
            print("x", end ="\t")
    print()