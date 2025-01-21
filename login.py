class User:
    def __init__(self, username, age, phone, password):
        self.username = username
        self.age = age
        self.phone = phone
        self.password = password
    def __str__(self):
        return f"{self.username}({self.age})"
Users=[]
while True:    
    signup=input("Do you want to sign up or log in? ")

    if signup == "sign up":
        username=input("Create a username ")
        age=int(input("What's your age? "))
        phone=input("What's you phone number? ")
        password=input("Create a password")
        cpassword=input("Confirm your password ")
        while password != cpassword:
            print("Passwords do not match")
            password=input("Create a password")
            cpassword=input("Confirm your password ")
        Users.append(User(username, age, phone, password))
    else:
        username=input("Input your username ")
        password=input("Input your password ")
        for user in Users:
            if user.username == username:
                if user.password == password:
                    print("You have been logged in")
                else:
                    print("Your password was wrong")
                    password=input("Try again. Input your password ")

        
