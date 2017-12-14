#Problem 1

string = input("Please enter an odd length string: ")
fullString = len(string)
firstHalf = ((fullString - 1) // 2)
middle = firstHalf + 1
stringA = string[:firstHalf]
stringB = string[firstHalf]
stringC = string[middle:]
#print(string,fullString,firstHalf,stringA, stringB, stringC)

print("Middle Character:",stringB,"\nFirst Half:", stringA,"\nSecond Half:",stringC)