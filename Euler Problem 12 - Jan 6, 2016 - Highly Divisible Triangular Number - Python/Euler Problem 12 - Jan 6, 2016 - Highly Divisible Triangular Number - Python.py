import math
def findTriNum(x):
    factors = 0
    n = 0
    num = 0
    while(factors<x):
        n+=1
        num+=n
        factors = 0
        for i in range(0,int(math.sqrt(num))):
            if(num%(i+1)==0):
                factors+=2
    return num

print(findTriNum(500))
