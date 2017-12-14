#Lab 4
#Problem 1


posInt = int(input("Please enter a positive integer: "))
numDigs = int(input("Please enter the number of digits: "))
digSum = 0
for i in range(numDigs):
    eachDig = posInt // 10 ** i  % 10
    digSum = eachDig + digSum

print("Sum of the last", numDigs, "digits in", posInt, "is", digSum)
