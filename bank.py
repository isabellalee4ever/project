class BankAccount:
    globelaccount = 0
    def __init__(self, name:str, email:str, balance:int):
        BankAccount.globelaccount += 1
        self.name = name
        self.email = email
        self.accountnumber = BankAccount.globelaccount
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
    
    def save(self, name, email, accountnumber, balance):
        File = open(name, "w")
        File.write(name)
        File.write("\n")
        File.write(email)
        File.write("\n")
        File.write(accountnumber)
        File.write("\n")
        File.write(str(balance))
        File.write("\n")

    def save(self):
        File = open("People/" + self.name, "w")
        File.write(self.name)
        File.write("\n")
        File.write(self.email)
        File.write("\n")
        File.write(str(self.accountnumber))
        File.write("\n")
        File.write(str(self.balance))
        File.write("\n")

    def findaccount():
        File = open("People" +  "r")
        for i in File:
            print(i)



    #findaccount()
def money(self):
    money = input("Do you want to withdraw or desposit money from your account? Type withdraw if you want to withdraw. Type deposit if you want to deposit.")
    if money == "withdraw":
        withdraw = input("How much money do you want to withdraw?")
        self.balance = self.balance - int(withdraw)
        print("Your new balance is" , self.balance)
    if money == "deposit":
        deposit = input("How much money do you want to deposit?")
        self.balance = self.balance + int(deposit)
        print("Your new balance is" , self.balance)
#User_account = BankAccount("Isabella", "imtesting@gmail.com", 10)
#User_account = BankAccount("Isabella", "imtesting@gmail.com", 10)
#User_account.seedetails()

#User_account.deposit(money = 10)
#User_account.seedetails()
#User_account.save()
login = input("Do you want to log into your account or sign up? If you want to log in type log in. If you want to sign up type sign up.")
if login == "log in":
    name=input("What is your name?")
    email=input("What is your email?")
    User_account = BankAccount(name, email, 0)
    User_account.seedetails()

if login == "sign up":
    name=input("What is your name?")
    email=input("What is your email?")
    User_account = BankAccount(name, email, 0)
    User_account.save()
    User_account.seedetails()
    money(User_account)

