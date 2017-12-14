#Problem 5

import random
num = random.randint(1,100)
print("I thought of a number between 1 and 100! Try to guess it.")

val = 0

while(val != num):
    val = int(input("Try to guess what it is: "))
    if(val<num):
        low = val
        print("Wrong! My number is larger.")
    elif(val>num):
        high = val
        print("Wrong! My number is smaller.")

print("Congrats! You guessed my number!")



