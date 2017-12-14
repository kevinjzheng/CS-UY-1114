#Problem 7a

romanNum = input("Enter number in the simplified Roman system: ")
decVal = 0
for char in romanNum:
    if(char == "M"):
        decVal += 1000
    elif (char == "D"):
        decVal += 500
    elif (char == "C"):
        decVal += 100
    elif (char == "L"):
        decVal += 50
    elif (char == "X"):
        decVal += 10
    elif (char == "V"):
        decVal += 5
    elif (char == "I"):
        decVal += 1

print(romanNum,"is",decVal)