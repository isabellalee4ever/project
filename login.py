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
        userfound = False
        for user in Users:
            if user.username == username:
                userfound = True
        while userfound == True:
            print("That username already exists")
            username=input("Create a username ")
            userfound = False
            for user in Users:
                if user.username == username:
                    userfound = True
        age=int(input("What's your age? "))
        if age < 13:
            print("You must be over 13 to use this website")
            continue
        phone=input("What's your phone number? ")
        phonefound = False
        for user in Users:
            if user.phone == phone:
                phonefound = True
        if phonefound == True:
            print("A user already has this phone number. Try logging in")
            continue
        password=input("Create a password")
        while len(password) < 10:
            print("Password must be at least 10 characters")
            password=input("Create a password")
        cpassword=input("Confirm your password ")
        while password != cpassword:
            print("Passwords do not match")
            password=input("Create a password")
            while len(password) < 10:
                print("Password must be at least 10 characters")
                password=input("Create a password")
            cpassword=input("Confirm your password ")
        Users.append(User(username, age, phone, password))
    elif signup == "log in":
        username=input("Input your username ")
        password=input("Input your password ")
        userfound = False
        for user in Users:
            if user.username == username:
                userfound = True
                # if user.password == password:
                #     print("You have been logged in")
                # else:
                #     print("Your password was wrong")
                #     password=input("Try again. Input your password ")
                while user.password != password:
                    print("Your password was wrong")
                    password=input("Try again. Input your password ")
                print("You have been logged in")
        if userfound == False:
            print("There is no user by that username. Maybe try signing up.")
    else:
        break
        
        