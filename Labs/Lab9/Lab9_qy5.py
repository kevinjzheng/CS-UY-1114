
lst1 =  [ 2, 'S', 3.13, 3.13, 'python']
lst2 = ['pythy', 2, 12, 'hello', 3.13 ]

def get_common_element(lst1,lst2):
    newLst = []
    for element in lst1:
        if element in lst2:
            if element not in newLst:
                newLst.append(element)

    print(newLst)

get_common_element(lst1,lst2)
