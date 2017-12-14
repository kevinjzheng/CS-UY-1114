#Problem 2: Price calculator with club benefits

#inputs and variables
itemA = float(input("Please enter price of item 1: "))
itemB = float(input("Please enter price of item 2: "))
clubMem = input("Are you club card member? (Y/N): ")
taxRate = float(input("Please enter a tax rate, e.g. 5.5 for 5.5% tax(%): "))
itemCheap = 0
itemExp = 0

#calculations
if(itemA < itemB):
    itemCheap = itemA
    itemExp = itemB
else:
    itemCheap = itemB
    itemExp = itemA

if(clubMem == "Y" or clubMem == "y"):
    discount = .9
else:
    discount = 1
basePrice = float(itemA + itemB)
discPrice = float( ((itemCheap/2) + itemExp) * (discount) )
totalPrice = float(discPrice * (1+(taxRate/100)))

print("The base price is:", basePrice,'\n' + "The price after discounts:", discPrice, '\n'+"The total price is:", round(totalPrice,2))

#print(itemCheap,basePrice,discPrice,round(totalPrice,2))
