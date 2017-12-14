



sentence = ""
stringS = input("Please enter a string s: ")
piece = ""


for char in stringS:
    if (char == " "):
        sentence = sentence + piece[::-1] + " "
        print(sentence, "2")
        piece = ""
    else:
        piece = piece + char
        print(piece, "1")
sentence = sentence + piece[::-1]

print("Result is:", sentence)
