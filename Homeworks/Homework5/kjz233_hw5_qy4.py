#Problem 4

vowel = 0
consonant = 0
word = input("Please enter a word: ")

'''
for i in range(len(word)):
    if(word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u"):
        vowel += 1
    elif (word[i] == "A" or word[i] == "E" or word[i] == "I" or word[i] == "O" or word[i] == "U"):
        vowel += 1
    else:
        consonant += 1

'''
for char in word:
    c = char.lower()
    if c == "a" or c == "i" or c == "e" or c == "o" or c == "u":
        vowel += 1
    else:
        consonant += 1

print(word,"has",vowel,"vowels and",consonant,"consonants.")