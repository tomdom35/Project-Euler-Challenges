import math
def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def truncate_prime_check_left(n):
    num = n
    while(is_prime(num)):
        num = str(num)[1:]
        if(num == ''):
            return True
        num = int(num)
    return False
    
def truncate_prime_check_right(n):
    num = n
    while(is_prime(num)):
        num = str(num)[:-1]
        if(num == ''):
            return True
        num = int(num)
    return False



n = 10
found = 0
total = 0
while(found<11):
    if(truncate_prime_check_left(n) and truncate_prime_check_right(n)):
        found += 1
        total += n
        print(n)
    n += 1

print(total)
