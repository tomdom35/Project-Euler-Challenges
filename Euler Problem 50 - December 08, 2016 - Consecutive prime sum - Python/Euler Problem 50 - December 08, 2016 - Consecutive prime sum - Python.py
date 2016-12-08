import math
import time

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def next_prime(n):
    num = n+1
    while(not is_prime(num)):
        num+=1
    return num

num = 2
count = 1
primes = []

start = time.time()
for i in range(2,1000000):
    if(is_prime(i)):
        primes.append(i)
        j = 0
        while primes[j] < i:
            if len(primes) - j < count:
                break
            t = 0
            c = 0
            k = j
            while t < i:
                t+=primes[k]
                k+=1
                c+=1
            if(t == i and c > count):
                num = i
                count = c
            j+=1
end = time.time()
print(num,count,end-start)
