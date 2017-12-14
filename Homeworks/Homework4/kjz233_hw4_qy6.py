#Problem 6

#PART A
seqLeng = int(input("Please enter the length of the sequence: "))

seqSum = 1

for i in range(seqLeng):
    seqNum = int(input("Please enter your sequence: "))
    seqSum = seqNum * seqSum


print("The geometric mean is:", (seqSum ** (1/seqLeng)))

