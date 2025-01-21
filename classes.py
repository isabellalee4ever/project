class Person:
    name = "Amy"
    age = 15
    favcolor = "blue"

Amy1 = Person()
print(Amy1.name)
print(Amy1.age)
print(Amy1.favcolor)

class User:
    def __init__(self, name, age, favcolor):
        self.name = name
        self.age = age
        self.favcolor = favcolor
    def __str__(self):
        return f"{self.name}({self.age})"
Johnny = User("Johnny", 10, "red")
print(Johnny.name)
print(Johnny.age)
print(Johnny.favcolor)

Danny = User("Danny", 25, "green")
print(Danny.name)
print(Danny.age)
print(Danny.favcolor)
print(Danny)