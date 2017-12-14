string=input("Please enter a string: ")
for letter in string:
    if (letter.isupper()==True):
        print(letter.lower(),end="")
    elif (letter.islower()==True):
        print(letter.upper(), end="")
    else:
        print(" ",end="")