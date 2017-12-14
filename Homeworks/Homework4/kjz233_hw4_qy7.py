#Problem 7

import random
num = random.randint(1,100)
print("I thought of a number between 1 and 100! Try to guess it.")

guessCount = 5
high = 100
low = 1


for i in range (guessCount):
    print("Range: [" + str(low) + "," + str(high) + "], Number of guesses left:", guessCount)
    guessCount = guessCount - 1
    val = int(input("What is your guess? "))
    if(val != num):
        if((val != num) and (guessCount == 0)):
            print("Out of guesses! My number is", num)
        elif(val<num):
            low = val + 1
            print("Wrong! My number is larger.")
        elif(val>num):
            high = val - 1
            print("Wrong! My number is smaller.")
    elif(val == num):
        print("Congrats! You guessed my number in", i + 1,"guesses.")
        break



