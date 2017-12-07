import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

side_length = 1
num = 1

diagonals = [1]
prime_diagonals = []
percent = 1

while percent > 0.1:
    for i in range(1,5):
        d = num + (side_length * i) + i
        diagonals.append(d)
        if is_prime(d):
            prime_diagonals.append(d)

    num = num + side_length*4 + 4
    side_length += 2
    
    percent = len(prime_diagonals)/len(diagonals)

print(side_length)