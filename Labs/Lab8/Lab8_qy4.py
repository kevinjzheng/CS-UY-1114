#Problem 4

def int_to_bin(num):
    quo = 0
    rem = 0
    bin = ""
    while(num != 0):
        quo = num // 2
        rem = num % 2
        bin += str(rem)
        num = quo
    return (bin[::-1])

def flipper(num):
    newString = ""
    newDeci = 0
    x = 0
    for char in int_to_bin(num):
        if(char == "1"):
            newString += "0"
        else:
            newString += "1"
    #print(newString)
    for i in range(-1,-len(newString),-1):
        #print(newDeci)
        newDeci = 2**x
        x += 1

    print(newDeci)



def main():
    num = int(input("Please enter a decical number: "))
    flipper(num)

main()

