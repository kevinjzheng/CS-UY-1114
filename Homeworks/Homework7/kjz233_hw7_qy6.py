#Problem 6


def reverse_to_new_list(lst):
    revlst = lst[::-1]
    return (revlst)

def reverse_in_place(lst):
    start = 0
    end = len(lst)-1
    for i in range(len(lst) // 2):
        lst[start],lst[end] = lst[end],lst[start]
        start += 1
        end -= 1

def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse_to_new_list(lst1)
    print("After reverse_to_new_list, lst1 is", lst1, "and the returned list is", rev_lst1)
    lst2 = [1, 2, 3, 4, 5, 6]
    print("Before reverse_in_place, lst2 is", lst2)
    reverse_in_place(lst2)
    print("After reverse_in_place, lst2 is", lst2)

main()