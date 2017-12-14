
import random

def write_random_numbers(filename,n):
    f = open(filename, "w")
    for i in range(n):
        randNum = random.randint(1, 100)
        print(randNum ,file = f)
    f.close()

write_random_numbers('lab11_q2.txt', 5)