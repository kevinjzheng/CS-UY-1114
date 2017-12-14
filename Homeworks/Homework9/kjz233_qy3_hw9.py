
class BinaryPositiveInteger:
    def __init__(self, num=0):
        self.num = num
        quo = 0
        rem = 0
        binString = ""
        while (self.num != 0):
            quo = self.num // 2
            rem = self.num % 2
            binString += str(rem)
            self.num = quo
        binString = binString[::-1]
        self.num = binString
        #print(self.num)
        ''' Initializes a BinaryPositiveInteger object
        representing the value given in the integer num'''
    def __add__(self, other):
        if len(self.num) < len(other.num):
            self.num = "0"*(len(other.num)-len(self.num)) + self.num

        elif len(self.num > len(other.num)):
            other.num = "0"*(len(self.num) - len(other.num)) + other.num
        self.num="0"+self.num
        other.num="0"+other.num

        self.num = self.num[::-1]
        other.num = other.num[::-1]
        newNumber = ""
        carry = 0
        for i in range(len(self.num)):
            if carry == 1:
                #if other.num[i] == "0" and self.num[i] == "0":
                #    carry = 0
                #    newNumber += "1"
                if other.num[i] == "1" and self.num[i] == "1":
                    carry = 1
                    newNumber += "1"
                elif other.num[i] == "0" and self.num[i] == "0":
                    carry = 0
                    newNumber += "1"
                else:
                    carry = 1
                    newNumber += "0"
            else:
                if other.num[i] == "1" and self.num[i] == "1":
                    carry = 1
                    newNumber += "0"
                elif other.num[i] == "0" and self.num[i] == "0":
                    carry = 0
                    newNumber += "0"
                else:
                    carry = 0
                    newNumber += "1"
        if newNumber[0] == "0":
            newNumber = newNumber[1:]
        #print(self.num)
        #print(other.num)
        newNumber = "0b"+newNumber[::-1]
        #print(newNumber)
        return newNumber
        ''' Creates and returns a BinaryPositiveInteger object
    that represent the sum of self and other (also of
    type BinaryPositiveInteger)'''
        #BinaryPositiveInteger().num = final
    def __lt__(self, other):
        ''' returns True if self is less than other, or False
    otherwise'''
        if len(self.num) < len(other.num):
            return True
        elif len(other.num) < len(self.num):
            return False
        elif len(other.num) == len(self.num):
            for digitA in self.num:
                digitA = digitA
            for digitB in other:
                digitB = digitB
            if digitA < digitB:
                return True
    def is_power_of_2(self):
        ''' returns True if self is a power of 2, or False
    otherwise'''
        number = self.num[2:]
        #print(number)
        while number[0] == '1':
            for i in range(len(number)):
                if number[i+1] == "0":
                    return True
                else:
                    return False

    def largest_power_of_2(self):
        ''' returns the largest power of 2 that is less than or
    equal to self'''
        largestPower = "1"
        zeros = len(self.num)-3
        largestPower = largestPower + (zeros)*"0"
        #print(largestPower)
        integer = 2**(zeros)
        return integer
    def __repr__(self):
        ''' Creates and returns the string representation
    of self. The string representation starts with 0b,
    followed by a sequence of 0s and 1s'''
        self.num = "0b"+self.num
        return self.num

n1 = BinaryPositiveInteger(13)
print(n1)
n2 = BinaryPositiveInteger(25)
print(n2)
#n3 = BinaryPositiveInteger(256)
#print(n3)
print(n1.is_power_of_2())
#print(n3.is_power_of_2())
print(n1.largest_power_of_2())
print(n1 < n2)
print(n1 + n2)