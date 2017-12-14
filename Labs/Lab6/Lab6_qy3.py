stringS = input("Please enter a string s: ")
numK = int(input("Please enter an integer k: "))



newString = ""
start = 0
partString = ""
leftString = ""


for i in range(len(stringS) // 2):
    if(i % 2 == 0):
        newString = newString + stringS[ i*numK : i*numK+numK][::-1]

    else:
        newString = newString +stringS[ i*numK : i*numK+numK]

if(len(stringS) % 2 != 0):
    newString = newString + stringS[(i+1) * numK:]


print(newString)