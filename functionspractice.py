def max3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


print(max3(5,3894,190284720928))

def sum(liist):
    summ=0
    for i in liist:
       summ += i
    return summ  

print(sum([854,45875,4484738,484,5,4,3,2,1]))

def reverse(str):
    var=""
    for i in range(len(str)-1,-1,-1):
        var += str[i]
    return var

print(reverse("isabella"))

def fact(num):
    nums=1
    for i in range(1,num+1):
        nums *= i
    return nums

print(fact(8))
