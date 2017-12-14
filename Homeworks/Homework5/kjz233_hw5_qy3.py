#Problem 3

mathExp = input("Please enter a mathematical expression: ")

oprand1 = 0
op = ""
oprand2 = 0
answer = 0
for i in range(len(mathExp)):
    if(mathExp[i] == " "):
        oprand1 = mathExp[:i-1]
        op = mathExp[i-1]
        oprand2 = mathExp[i+1:]

if(op == "+"):
    answer = int(oprand1) + int(oprand2)
elif(op == "*"):
    answer = int(oprand1) * int(oprand2)
elif(op == "/"):
    answer = int(oprand1) // int(oprand2)
elif(op == "-"):
    answer = int(oprand1) - int(oprand2)

print(str(oprand1) + str(op),oprand2,"=", answer)

#print(oprand1)
#print(op)
#print(oprand2)
#print(answer)


'''
new = mathExp.split(" ")
#print(new)
oprand1 = new[0]
op = new[1]
oprand2 = new[2]
answer = 0
'''