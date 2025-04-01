class BankAccount:
    def __init__(self, name, email, accountnumber, balance):
        self.name = name
        self.email = email
        self.accountnumber = accountnumber
        self.balance = balance
    def deposit(self, money):
        if money > 0:
            self.balance += money
            print("deposited")
        else:
            print("You must deposit an amount of money greater than 0")
    def withdraw(self, money):
        if money<=0:
           print("You must withdraw an amount of money greater than 0")
        elif money <= self.balance:
            self.balance -= money
            print("withdrawn")
        else:
            print("The amount of money you are trying to withdraw is greater than your balance, you have withdrawn the entirety of your balance")
            self.balance = 0

    def seebalance(self):
        print("Balance: $",self.balance)
    def seedetails(self):
        print("Name: ",self.name)
        print("Email: ",self.email)
        print("Account Number: ",self.accountnumber)
        print("Balance: $",self.balance)
