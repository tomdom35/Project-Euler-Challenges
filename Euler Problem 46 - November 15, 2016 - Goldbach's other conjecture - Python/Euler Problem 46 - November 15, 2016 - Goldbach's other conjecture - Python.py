import math
def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_next_prime(n):
    num = n+1
    while not is_prime(num):
        num+=1
    return num

c = 33
found = True

while(found):
    c+=2
    found = False
    if(not is_prime(c)):
        p = 2
        s = 1
        t = p + (2 * (s*s))
        while(p < c):
            s = 1
            t = p + (2 * (s*s))
            while(t <= c):
                if(t == c):
                    found = True
                    break
                s+=1
                t = p + (2 * (s*s))
            if(found):
                break
            p = get_next_prime(p)
    else:
        found = True

print(c)

                
    
