def findMaxCollatz(n):
    maxLength = 1
    maxNum = 1
    for i in range(1,n):
        tempLength = collatzSequenceLength(i)
        if tempLength>maxLength:
            maxLength = tempLength
            maxNum = i
    return maxNum

def collatzSequenceLength(n):
    num = n
    i = 0
    while(num>1):
        i+=1
        if num%2 == 0:
            num = num/2
        else:
            num = 3*num + 1
    return i

print(findMaxCollatz(1000000))
