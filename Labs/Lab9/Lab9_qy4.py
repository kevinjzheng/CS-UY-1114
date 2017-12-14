
def find_max_even_index(lst):
    max = 0
    index = -1
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            if lst[i] > max:
                max = lst[i]
                index = i
    print(index)

find_max_even_index([56, 24, 58, 10, 33, 95])
find_max_even_index([3,5])