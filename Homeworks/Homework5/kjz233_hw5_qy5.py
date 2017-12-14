#Problem 5

password = input("Please enter a password: ")

lowercase = 0
uppercase = 0
digits = 0
spechar = 0
validity = ""
for char in password:

    if(char.isdigit()==True):
        digits += 1
    elif (char.islower() == True):
        lowercase += 1

    elif (char.isupper() == True):
        uppercase += 1

    else:
        spechar += 1

if(uppercase >= 2 and lowercase >= 1 and digits >= 2 and spechar >= 1):
    validity = "is"
else:
    validity = "is not"

print(password,validity,"a valid password.")