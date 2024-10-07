import random

mystery=random.randint(1,200)

guess=int(input("guess number between 1-200: "))

while guess!=mystery:

    if guess>mystery:
        print("too large")
    else:
        print("too small")
    

    guess=int(input("guess number between 1-200: "))

print("You Win!")
