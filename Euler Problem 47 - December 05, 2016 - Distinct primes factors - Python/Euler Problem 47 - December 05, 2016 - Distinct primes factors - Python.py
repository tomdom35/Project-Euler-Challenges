import time
import math

def get_smallest_factor(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return i
    return 1

def get_prime_factors(n,f):
    if len(f)<4:
        x = get_smallest_factor(n)
        if(x!=1):
            y = int(n/x)
            if x not in f:
                f.append(x)
            get_prime_factors(y,f)
        elif(len(f)>0 and n not in f):
            f.append(n)

f = []
n = 210
m = 4
nums = [210]
count = 1
start = time.time()
while(len(nums)<m):
    f = []
    n+=1
    get_prime_factors(n,f)
    if len(f) == m:
        nums.append(n)
    else:
        nums = []
end = time.time()
print(nums)
print(end - start)
