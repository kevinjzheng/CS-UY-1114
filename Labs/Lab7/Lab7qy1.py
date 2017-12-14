#Problem 1

import random
n = int(input("Please enter a number n: "))



for i in range(n):

    for j in range(n-i):

        print(str(random.randint(0,9)), end=" ")

    print()

for k in range(n):
    for l in range(k+1):
        print(str(random.randint(0,9)), end=" ")

    print()
