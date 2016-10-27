import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


v = 1000
a = -v
b = -v
max_n = 0
max_a = 0
max_b = 0

while(b < v):
    while(a < v):
        n = 0
        x = n*n + n*a + b
        while(x>0 and is_prime(x)):
            n+=1
            x = n*n + n*a + b
        if n > max_n:
            max_n = n
            max_a = a
            max_b = b
        a+=1
    b+=1
    a = -v

print('a =',max_a)
print('b =',max_b)
print('n =',max_n)
print('a X b =',max_a*max_b)
