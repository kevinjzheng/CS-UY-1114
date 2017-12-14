#Problem 3

def user_input():
    lst = []
    print("Please enter a val, type done to finish: ")
    val = 0
    while val != 'done':
        val = input()
        lst.append(val)
        #print(lst)
    lst.pop()
    return lst

def len_list(lst1,lst2):
    return len(lst1) == len(lst2)

def add_list(lst1,lst2):
    newlst = ""
    for i in range(len(lst1)):
        sumVal = int(lst1[i]) + int(lst2[i])
        newlst = newlst + "\n" + str(sumVal)
    return newlst

def main():
    lst1 = user_input()
    lst2 = user_input()
    if len_list(lst1,lst2) == True:
        print(add_list(lst1,lst2))
    else:
        print("Lists are different lengths.")

main()