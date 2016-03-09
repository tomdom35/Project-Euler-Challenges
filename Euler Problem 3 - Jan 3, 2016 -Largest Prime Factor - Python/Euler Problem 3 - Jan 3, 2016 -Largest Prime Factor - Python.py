import math
def isPrime(n):
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def largestPrimeFactor(n):
    for i in range(0,n+1):
        x = n-i
        if(n%x==0):
            if(isPrime(x)):
                return x

print(largestPrimeFactor(3761))
