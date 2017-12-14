
def count(lst,item):
    counter = 0
    for i in range(len(lst)):
        if lst[i] == item:
            counter += 1
    print(counter)

count([0, 32, 'a', '0', '4', 15, 'q', '0'],'0')