import math
def isPrime(n):
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def sumPrimes(n):
    total = 2
    i = 2
    while(i<n):
        if(isPrime(i)):
            total+=i
        i+=1
    return total

print(sumPrimes(2000000))
