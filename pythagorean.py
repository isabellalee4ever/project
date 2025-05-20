ask = input("Type 2 if you have 2 sides or type 1 if you have 1 side and the hypotenuse ")
if ask == "2":
    a = input("What is your first side? ")
    b = input("What is your second side? ")

    a = int(a)**2
    b = int(b)**2

    sides = a + b

    c = sides ** 0.5

    print(c)

if ask == "1":
    a = input("What is your side? ")
    h = input("What is your hypotenuse? ")

    a = int(a)**2
    h = int(h)**2

    b = (h - a)**0.5

    print(b)