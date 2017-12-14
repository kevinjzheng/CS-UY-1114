#Problem 7b

decVal = int(input("Enter decimal number: "))
romanNum = 0
newVal = decVal

thous = newVal // 1000
newVal %= 1000
fiveHun = newVal // 500
newVal %= 500
hun = newVal // 100
newVal %= 100
fifty = newVal // 50
newVal %= 50
ten = newVal // 10
newVal %= 10
five = newVal // 5
ones = newVal % 5



romanNum = (thous * "M") + (fiveHun * "D") + (hun * "C") + (fifty * "L") + (ten *"X") + (five * "V") + (ones * "I")
print(decVal,"is",romanNum)


