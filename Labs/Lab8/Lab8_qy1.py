#Problem 1

def alphabet(ch,num):
    string = ch
    letterNum = ord(ch)
    letter = chr(letterNum)
    #print(ord('{'))
    #print(chr(97))
    for i in range(num-1):
        if(letterNum < 122):
            letterNum += 1
            letter = chr(letterNum)
            string += letter
        else:
            letterNum -= 25
            #print(letterNum)
            letter = chr(letterNum)
            #print(letter)
            string += letter
            #print(string)

    print(string)
def main():
    ch = input("Please enter a letter: ")
    num = int(input("Please enter an integer: "))
    alphabet(ch,num)

main()




