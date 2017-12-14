s = input("Please enter a string: ")
lenOfString = len(s)
#print(lenOfString)
maxLen = lenOfString // 2
#print(maxLen)
numRepeat=0

for length in range(1, maxLen):
    subString = s[:length]
    #print(subString)

    for index in range[0,len(s), length]:
        segment = s[index: index + length]

        if subString != segment:
            numRepeat = 0
            break
        else:
            numRepeat