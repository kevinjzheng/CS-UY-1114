

class BankAccount:
    def __init__(self,accNum,balance):
        self.accNum = accNum
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient balance. The current balance remained as "+"$"+str(self.balance))
        else:
            self.balance -=amount
    def __repr__(self):
        money = str(self.balance)
        return ("Current balance is: $" + money)

my_account = BankAccount('BOA123', 1000)
print(my_account)
my_account.deposit(100)
print(my_account)
my_account.withdraw(500)
print(my_account)
my_account.withdraw(999999)