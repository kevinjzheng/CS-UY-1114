#Problem 3

n = input("Please enter an Ascii Number: ")


def convertASCIIToText(number):
    newString = ""
    for i in range(len(number)//2):

        newString += chr(int(number[i*2:2+(i*2)]))

    return newString

print(convertASCIIToText(n))

