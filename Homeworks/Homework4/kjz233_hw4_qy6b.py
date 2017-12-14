#PART B

print("Please enter a non-empty sequence of positive integers, each one in a separate line. End your sequence by typing done:")
seqProd = 1
xLength = 0
status = False
seqIn = ""
while(status == False):
    seqIn = input()
    if(seqIn == 'done'):
        status = True
    else:
        seqIn_integer = int(seqIn)
        xLength = xLength + 1
        seqProd = seqProd * seqIn_integer

seqMean = seqProd ** (1/xLength)

print("The geometric mean is", seqMean)
