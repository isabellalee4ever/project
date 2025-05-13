bottle = 99
beer = " bottles of beer"
one = " bottle of beer"
wall = " on the wall"
no = "No more"

while bottle > 0:
    if bottle == 1:
        print(str(bottle) + one + wall)
        print(str(bottle) + one)
    else:
        print(str(bottle) + beer + wall)
        print(str(bottle) + beer)
    print("Take one down, pass it around")
    bottle = bottle - 1
    if bottle == 1:
        print(str(bottle) + one + wall)
    else:
        print(str(bottle) + beer + wall)
    print("\n")

print(no + beer + wall)
print(no + beer)
print("Go to the store and buy some more")
print("99" + beer + wall)

