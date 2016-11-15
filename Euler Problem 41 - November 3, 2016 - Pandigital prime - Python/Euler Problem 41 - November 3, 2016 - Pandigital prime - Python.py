import math
import itertools

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

num = ['9','8','7','6','5','4','3','2','1']
num_list = list(itertools.permutations(num))
max_prime = 0

while(max_prime == 0):
    for i in num_list:
        n = int(''.join(i))
        if n > max_prime:
            if is_prime(n):
                max_prime = n
    num = num[-(len(num)-1):]
    num_list = list(itertools.permutations(num))

print(max_prime)
