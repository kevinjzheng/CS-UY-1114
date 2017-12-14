#Problem 1a
import random

def create_permutation(n):
    ls = []
    while len(ls) != n:
        randInt = random.randint(0, n - 1)
        if randInt not in ls:
            ls.append(randInt)
    return ls

#print(create_permutation(6))

#Problem 1b
def scramble_word(word):
    newWord = ""
    scramIndex = create_permutation(len(word))
    for i in range(len(word)):
        newWord += word[scramIndex[i]]
    return newWord

#print(scramble_word('pokemon'))

#Problem 1c
def choose_random(filename):
    f = open(filename,"r")
    lines = f.readlines()
    #print(lines)
    randNum = random.randint(0,len(lines)-1)
    randWord = (lines[randNum][0:-1])
    #print(randWord)
    return randWord

def sep_scramble_word(word):
    wordScram = word
    wordUnscram = ""
    for letter in wordScram:
        wordUnscram += letter + " "
    return wordUnscram

#(choose_random("word_bank.txt"))

def main():
    filename = "word_bank.txt"
    randWord = choose_random(filename)
    mixed_word = scramble_word(randWord)
    spaced_word = sep_scramble_word(mixed_word)
    #print(randWord)
    print("Unscramble the word:", spaced_word)
    numGuess = 1
    guess = input("Try #" + str(numGuess) + ": ")
    while numGuess < 3 and guess != randWord:
        numGuess += 1
        print("Wrong!")
        guess = input(("Try #" + str(numGuess) + ": "))
    if numGuess == 3 and guess != randWord:
        print("Wrong! Out of guesses!")
        print("Correct Word is:",randWord)
    if guess == randWord:
        print("Yay you got it!")

main()