import math
def isPrime(n):
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def findNthPrime(n):
    count = 1
    i = 2
    while(count<n):
        i+=1
        if(isPrime(i)):
            count+=1
    return(i)

print(findNthPrime(10001))
        
