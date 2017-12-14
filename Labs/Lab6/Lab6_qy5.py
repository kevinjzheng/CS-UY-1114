stringS = input("Please enter a string s: ")

max = len(stringS) // 2
counter = 1

for i in range(1,max):
    string1 = stringS [:i]
    counter = counter + 1
    for j in range(i,len(stringS),i):
        string2 = stringS[j:(j+1)]
        if(string1 == string2):
            counter = 0
        else:
            break

if (counter > 1):
    print("The Substring", string1, "is repeated", counter, "times in", stringS)
else:
    print("There are no repeating substrings in", stringS)