
lst = [2, 3, 5, 1, -4, 8, 0, -1]

def avg(lst):
    avg = 0
    sum = 0
    for element in lst:
        sum += element
    avg = sum / len(lst)
    return avg

def remove_below_avg(lst):
    newLst = []
    for element in (lst):
        if element > avg(lst):
            newLst.append(element)
    print(newLst)

remove_below_avg(lst)