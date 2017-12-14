#Problem 2a

string = input("Please enter a character: ")
if(string.isdigit()==True):
    type = "digit"
else:
    if (string.islower() == True):
        type = "lower case letter"
    elif (string.isupper() == True):
        type = "upper case letter"
    else:
        type = "non-alphanumerical character"


print(string,"is an",type)

