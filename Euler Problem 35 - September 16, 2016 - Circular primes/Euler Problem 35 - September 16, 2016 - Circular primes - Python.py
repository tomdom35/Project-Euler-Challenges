import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def rotate(num):
    new_num = num[:]
    n = new_num.pop()
    new_num.insert(0,n)
    return new_num

count = 1

for i in range(1,500000):
    num = i*2+1
    prime = is_prime(num)
    if(prime):
        num = list(str(num))
        new_num = rotate(num)
        prime = is_prime(int(''.join(new_num)))
        while(prime):
            if(new_num == num):
                count+=1
                break;
            new_num = rotate(new_num)
            prime = is_prime(int(''.join(new_num)))

print(count)

        
        
