#Problem 8

line = input("Please enter a line of text: ")
ch = input("Please enter the character you want to remove: ")
newLine = ""
for char in line:
    if(char != ch):
        newLine += char
print(newLine)
