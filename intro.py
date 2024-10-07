import random

name="Isabella"
age=12
color="Blue"
rain=False
characteristics= [name,age,color,rain]
print(characteristics)
print("hello "+"world")
print(11572340%34934)
flt=245254657694524565484686523333567.89656548984573735653737375345234
flt=((flt/24)**6)-7
print(flt)
x=random.uniform(0, 200)
if x<100:
    print(x, "is less than 100")
else:
    print(x, "is not less then 100")

for k in range(32):
    print(k)
lst=[random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)]

print(lst)

for i in lst:
    print(((i/24)**6)-7)

m=0
while m !=101:
    m+=2
    print(m)
    if m>101:
        break

def op(red):
    output=((red/24)**6)-7
    return output

print(op(389047038753025.2359375023572985739)*15)
