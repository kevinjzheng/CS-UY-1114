stringA = input("Please enter a string a: ")
stringB = input("Please enter a string b: ")

if(len(stringA) < len(stringB)):
    first = stringA
    second = stringB
else:
    first = stringB
    second = stringA

print(first + second + first)