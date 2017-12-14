#Problem 5

n = int(input("Please enter an integer n: "))

for i in range(1,n+1):
    evenDig = 0
    oddDig = 0
    tempNum = i
    while(tempNum > 0):
        oneDigs = tempNum % 10
        if(oneDigs % 2 == 0):
            evenDig = evenDig + 1
        else:
            oddDig = oddDig + 1
        tempNum = tempNum // 10
    if(evenDig > oddDig):
        evenDig = 0
        oddDig = 0
        print(i)


