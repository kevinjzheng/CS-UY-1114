#Problem 5a

string = "aadccccaa"
def length_string_encoder(string):
    counter = 1
    outls = []
    subls = []
    for i in range(len(string)):
        if i == len(string)-1 or string[i] != string[i+1] :
            subls = [string[i],counter]
            outls.append(subls)
            #print(outls)
            counter = 1
        else:
            counter += 1
            #print(string[i],counter)
    print(outls)
length_string_encoder(string)

#Problem 5b

lst = [['a', 2], ['d', 1], ['c', 4], ['a', 2]]
#print(lst[0][0])
def length_string_decoder(lst):
    newString = ""
    for i in range(len(lst)):
        newString += lst[i][0] * lst[i][1]
        #print(newString)
    print(newString)

length_string_decoder(lst)
#print('aadccccaa')