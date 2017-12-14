#Problem 1

import math
lst = [-19,-3,20,-1,0,-25]

def max_abs_val(lst):
    max = 0
    for i in range(len(lst)-1):
        pre = math.fabs(lst[i])
        pro = math.fabs(lst[i + 1])
        if pre < pro:
            max = pro
    print(max)

(max_abs_val(lst))