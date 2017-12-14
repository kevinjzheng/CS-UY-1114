#Problem 6


lowerString = input("Please enter a string of lowercase letters: ")
condition = "increasing."
for i in range(len(lowerString)-1):
    if(ord(lowerString[i]) > ord(lowerString[i+1])):
        condition = "not increasing."
print(lowerString,"is",condition)
