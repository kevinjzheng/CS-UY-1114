
def sum_column(filename):
    sumNum = 0
    f = open(filename,"r")
    for line in f:
        sumNum += int(line)
    return sumNum

print(sum_column('lab11_q2.txt'))