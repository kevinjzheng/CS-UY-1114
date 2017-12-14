
lst = [1,2,3,4,5,6,7,8]

def circular_shift_list1(lst,k):
    newLst =[]
    newLst.extend(lst[-k:])
    newLst.extend(lst[:-k])
    print(newLst)

circular_shift_list1(lst,3)