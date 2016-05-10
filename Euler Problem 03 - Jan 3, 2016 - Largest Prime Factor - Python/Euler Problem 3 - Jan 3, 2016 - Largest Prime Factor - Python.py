import math
def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def largestPrimeFact(num):
    largest = 0
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            fact = num/i
            if(isPrime(i) and i>largest):
                largest = i
            if(isPrime(fact) and fact>largest):
                largest = fact
    return largest

print(largestPrimeFact(600851475143))
