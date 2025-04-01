def distinctlist(listt):
    newlist=[]
    for i in listt:
        if i not in newlist:
            newlist.append(i)
    return newlist


def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True


def isperfect(num):
    sum=0
    for i in range(1,num+1):
        if num%i == 0:
            sum += i
    if sum == 2*num:
        return True
    else:
        return False
    


def findperfect(start,end):
    perfects = []
    for i in range(start,end+1):
        if isperfect(i):
            perfects.append(i)
    return perfects


def ispalindrome(word):
    word="".join(word.split()).lower()
    word2 = word[::-1]
    # for i in range(len(word)-1,-1,-1):
    #     word2+=word[i]
    return word == word2

