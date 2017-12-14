#Problem 4
lst = ['2','4','6','8','10']


def create_prefix_lists(lst):
    outlst = [[]]
    inlst = []
    for i in range(len(lst)):
        inlst.append(lst[i])
        outlst.append(inlst[:]) #inlst[:] is a copy of inlst and thus removes the issue of the changing inlst
        #print(inlst,'in')
        #print(outlst,'out')
        #inlst.append(lst[i])
    print(outlst)

create_prefix_lists(lst)