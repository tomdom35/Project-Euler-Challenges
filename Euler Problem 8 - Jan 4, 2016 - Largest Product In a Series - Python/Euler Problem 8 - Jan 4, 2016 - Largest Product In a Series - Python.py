num = ''
with open('input.txt') as file:
    for line in file:
        num+=line.rstrip()

def findAdjacentProduct(n,num):
    index = 0
    total = 0
    while(n+index<len(num)):
        curTotal = 1
        for i in range(index,n+index):
            curTotal*=int(num[i])
        if curTotal>total:
            total=curTotal
        index+=1
    return total

print(findAdjacentProduct(13,num))
