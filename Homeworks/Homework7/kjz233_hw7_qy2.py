#Problem 2

lst = ["a", "b", "10", "bab", "a"]
val = "a"
def find_all(lst,val):
    newlst = []
    for i in range(len(lst)):
        if lst[i] == val:
            newlst.append(i)
            #newlst += [i]
    print(newlst)

(find_all(lst,val))
