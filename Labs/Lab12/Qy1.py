people = []

def createPerson(name, age):
    people.append([name,age,[]])
    #print(people)

class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.hobbies = []
    def addHobby(self,newHobby):
        name = input("Who is receiving a new hobby? ")
        newHobby = input("What is this person's new hobby? ")
        for block in people:
            hobbyList = block[2]
            if name == block[0]:
                hobbyList.append(newHobby)

    def deleteHobby(self,oldHobby):
        name = input("Who is losing a hobby? ")
        oldHobby = input("What hobby are you deleting? ")
        for block in people:
            hobbyList = block[2]
            if name == block[0]:
                if oldHobby in hobbyList:
                    hobbyList.pop()

    def birthday(self):
        name = input("Who is having a birthday? ")
        print()
        print("Happy Birthday, "+name +"!")
        for block in people:
            if name == block[0]:
                block[1] += 1

    def __repr__(self):
        for block in people:
            hobbyList = ""
            self.name = block[0]
            self.age = block[1]
            self.hobbies = block[2]
            for item in self.hobbies:
                hobbyList += "\n" + item
            if hobbyList == "":
                hobbyList += "\n" + "None"
            print()
            print("Name:",self.name)
            print("Age:",self.age)
            print("Hobbies:",hobbyList)
            print()
            print()

def main():
    person = Person()
    while True:
        print()
        print("Select one of the following options:")
        print("========================================")
        print("1. Create a new Person")
        print("2. Add to an existing person's hobbies")
        print("3. Delete an existing person's hobby")
        print("4. Someone has a birthday")
        print("5. See a list of people")
        print("6. Exit")
        print()
        answer = input("What would you like to do? ")
        if answer == "1":
            name = input("Please enter the name: ")
            age = int(input("Please enter the age: "))
            createPerson(name,age)
        elif answer == "2":
            newHobby = ""
            person.addHobby(newHobby)
        elif answer == "3":
            oldHobby = ""
            person.deleteHobby(oldHobby)
        elif answer == "4":
            person.birthday()
        elif answer == "5":
            person.__repr__()
        elif answer == "6":
            print("Goodbye!")
            return False
main()