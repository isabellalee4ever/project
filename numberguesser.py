import random,time

def get_imput_from_user():
    s=time.time()
    guess=int(input("guess number between 1-200: "))
    e=time.time()
    return e-s, guess


mystery=random.randint(1,200)
counter=1

t,response=get_imput_from_user()


while response!=mystery:
    counter+=1
    if t>5:
        print("You took too much time to respond")
    elif response>mystery:
        print("too large")
    else:
        print("too small")
    
    t,response=get_imput_from_user()

print("You Win!")
print("you took",counter,"tries")
