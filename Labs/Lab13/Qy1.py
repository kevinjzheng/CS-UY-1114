

def valid_phone_number(number):
    value = True
    if len(number) != 10:
        return False
    for digit in number:
        if digit.isdigit() == True:
            value = True
        else:
            return False
    return True
# print(valid_phone_number("1234567890"))
# print(valid_phone_number("12faa11232"))
# print(valid_phone_number("123"))

def lookup(phonebook,name):
    #print(phonebook)
    if name in phonebook:
        print(phonebook[name])
    else:
        print(name+"'s phone number is not recorded in the phonebook")

def print_all(phonebook):
    for key in phonebook:
        print(key+":"+ phonebook[key])

def add_entry(phonebook,name,phonenumber):
    if valid_phone_number(phonenumber) == False:
        print(phonenumber,"is not a valid phone number")
    else:
        if name in phonebook:
            print(name,"already exist in the phone book")
        else:
            phonebook[name] = phonenumber

def main():
    openPhonebook = open('Lab 13 - phonebook.txt','r')
    yellowBook = {}
    for line in openPhonebook:
        line = line[0:-1]
        newLine = line.split(",")
        lastName = newLine[0]
        back = newLine[1].split()
        firstName = back[0]
        number = back[1]
        name = firstName + " " + lastName
        #print(name)
        #print(firstName,lastName,number)
        if valid_phone_number(number) == False:
            print(number, "is not a valid phone number")
        if name not in yellowBook:
            yellowBook[(firstName + " " + lastName)] = number
        else:
            print(name+" already exists in the phonebook")
    #print(yellowBook)
    return yellowBook

phonebook = main()
add_entry(phonebook, 'Preston Moore', '64699736000')
add_entry(phonebook, 'Preston Moore', '6469973600')
add_entry(phonebook, 'Preston Moore', '6469973600')
lookup(phonebook,'Larry Page')
lookup(phonebook, 'Linda Sellie')
print_all(phonebook)