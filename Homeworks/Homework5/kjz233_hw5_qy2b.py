#Problem 2b

string = input("Please enter a character: ")


if(string >= "a" and string <= "z"):
    type = "lower case letter"
elif(string >= "A" and string <= "Z"):
    type = "upper case letter"
elif(string >= "0" and string <= "9"):
    type = "digit"
else:
    type = "non-numerical character"

print(string,"is an",type)
