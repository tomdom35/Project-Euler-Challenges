import math
import itertools
import time

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_new_num(num, digit_positions, index):
    get_increment_position(num, digit_positions, index)

def get_increment_position(num, digit_positions, start_index):
    index = start_index - 1
    while index >= 0:
        if index in digit_positions:
            index -= 1
        else:
            break
    if(index >= 0):
        increment_num(num, index, digit_positions)

def increment_num(num, index, digit_positions):
    if int(num[index]) == 9:
        num[index] = '0'
        get_increment_position(num, digit_positions, index)
    else:
        num[index] = str(int(num[index]) + 1)

def can_increment(num, digit_positions):
    exp = len(num) - len(digit_positions)
    max_num = (10**exp) - 1
    check_num = ''
    for index, n in enumerate(num):
        if index not in digit_positions:
            check_num += n
    check_num = int(check_num)
    return check_num != max_num

def generate_num(num_size):
    num = []
    for i in range(num_size):
        if i == 0:
            num.append('1')
        else:
            num.append('0')
    return num

def generate_combinations(num):
    combos = []
    size = len(num)
    for i in range(1,size):
        combos.append(list(itertools.combinations(range(size), i)))
    return combos

def generate_digit_num(num, digit, digit_positions):
    new_num = generate_num(len(num))
    for index, n in enumerate(new_num):
        if index in digit_positions:
            new_num[index] = str(digit)
    return new_num

def check_prime_set(num,digit,digit_positions):
    primes = [int(''.join(num))]
    for i in range(digit+1,10):
        if digit - len(primes) > 3:
             break
        new_num = num[:]
        for index, n in enumerate(new_num):
            if index in digit_positions:
                new_num[index] = str(i)
        new_num = int(''.join(new_num))
        if is_prime(new_num):
            primes.append(new_num)
    return len(primes) == 8

        
num_size = 2
digit_positions = [0]
num_digits = 1
done = False
combos = []
primes = []
num_digit = 0
found_prime = False

start = time.time()
while not done:
    num = generate_num(num_size)
    combos = generate_combinations(num)
    for combo in combos:
        if done:
            break
        for digit_positions in combo:
            if done:
                break
            for digit in range(3):
                if done:
                     break
                num = generate_digit_num(num,digit,digit_positions)
                valid = num[0] != '0'
                while can_increment(num, digit_positions) and valid:
                    get_new_num(num, digit_positions, len(num))
                    num_digit = int(''.join(num))
                    if is_prime(num_digit):
                        if check_prime_set(num,digit,digit_positions):
                            done = True
                            print(num_digit)
                            break
    num_size += 1
end = time.time()
print(end-start)
