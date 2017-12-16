import random

def create_acc_num():
    accNum = ""
    for i in range(5):
        digit = str(random.randint(0,9))
        accNum += digit
    return (accNum)
#create_acc_num()

class Library:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.patrons = []
        self.bookList = []
    def add_book(self,book):
        self.bookList.append(book)
    def add_patron(self,patron):
        accNum = create_acc_num()
        patron.library_account_number = accNum
        self.patrons.append(patron)
    def lend(self,patron,bookName):
        if patron in self.patrons:
            if bookName in self.bookList:
                patron.borrowedBooks.append(bookName)
                index = self.bookList.index(bookName)
                self.bookList.pop(index)
            else:
                print(bookName,"is not available")
        else:
            print(patron.name,"is not a patron of the",self.name)
    def __repr__(self):
        bookList = ""
        back = ""
        #print(self.patrons)
        for book in self.bookList:
            bookList += book +'\n'
        for patron in self.patrons:
            back += "\nLibrary Patron Information: " + "\nName: "+ patron.name + "\nLibrary Account Number: " + patron.library_account_number +'\n'
            books = "\nBorrow Books:\n"+"\n".join(patron.borrowedBooks)
            back += books
        front = "Name: "+self.name+"\nLocation: "+self.location +"\nAvailable Books:\n"+bookList

        return front + back

class Patron:
    def __init__(self,name):
        self.name = name
        self.library_account_number = None
        self.borrowedBooks = []


bk_library = Library("Brooklyn Public Library", "6 Metrotech Center")
bk_library.add_book("Ender's Game")
bk_library.add_book("Ender's Shadow")
bk_library.add_book("Shadow of the Hegemon")
bk_library.add_book("Ready Player One")
bk_library.add_book("The Outsiders")
bk_library.add_book("Flowers for Algernon")
bob = Patron('Bob')
print(bob.library_account_number)
bk_library.add_patron(bob)
print(bob.library_account_number)
print(bk_library)
shuyu = Patron('Shuyu')
bk_library.lend(shuyu, "Flowers for Algernon")
bk_library.add_patron(shuyu)
bk_library.lend(shuyu, "Old Man’s War")
bk_library.lend(shuyu, "Ender's Shadow")
bk_library.lend(bob, "Ender's Shadow")
print(bk_library)