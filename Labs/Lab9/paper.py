str_list = ['hi','mom','dad']
num_list = [1, 57, 15]
num_list[2] = 25
print(str_list + num_list) #Line1
print([str_list[0], num_list[2]]) # Line 2
print(str_list.append(num_list)) # Line 3
print(str_list) # Line 4

mylist = []
for i in range(3, 6):
    for k in range(4):
        mylist.append(i + k)
print(i)
print(k)
print(mylist)