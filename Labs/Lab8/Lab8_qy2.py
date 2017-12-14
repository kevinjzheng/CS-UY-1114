#Problem 2



'''
def compare(stringA,stringB):
    value = "True"
    newB = stringB
    for char in stringA:
        for i in range(len(stringA)) :
            if(char == newB[i]):
                newB = stringB[i:]
            else:
                value = "False"
    print(value)

'''
''' # malfunctions
def stringChecker(stringA,stringB):
    value = True
    for i in stringA:
        ind = -1
        for letter in range(len(stringB)):
            ind = i
    if ind == -1:
        value = False
    else:
        beforeIndex = stringB[:ind]
        afterIndex = stringB[ind + 1:]
        stringB = beforeIndex + afterIndex
    return value
'''
def match(a,b):
    for ch in a:
        post = b.find(ch)
        if (post == -1):
            return False
        b = b[:post] + b[post+1:]
    return True

def main():
    stringA = input("Please enter string A: ")
    stringB = input("Please enter string B: ")
    print(match(stringA,stringB))

main()

