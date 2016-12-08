import math

def is_perm(x,y):
    return sorted(str(y)) == sorted(str(x))

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

x = 1000
found = False

for i in range(1488,10000):
    if found:
        break
    if(is_prime(i)):
        for j in range(1,5001):
            a = i+j
            if is_perm(i,a) and is_prime(a):
                b = a+j
                if(is_perm(i,b) and is_prime(b)):
                    print(i,a,b,j)
                    found = True

