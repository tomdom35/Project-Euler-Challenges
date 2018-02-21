import math
import itertools
import time
from random import shuffle

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_x_num_primes(x):
    primes = [2]
    i = 3
    while len(primes) < x:
        if is_prime(i):
            primes.append(i)
        i+=2
    return primes

def check_tup(t):
    t1 = t[0]
    t2 = t[1]
    t3 = str(t1) + str(t2)
    t3 = int(t3)
    if is_prime(t3):
        t3 = str(t2) + str(t1)
        t3 = int(t3)
        return is_prime(t3)
    return False

def get_first_num_list(tupes):
    nums = []
    for t in tupes:
        nums.append(t[0])
    return sorted(list(set(nums)))


def find_set_of_n(n,tupes):
    nums = [None] * n
    for t in tupes: 
        x = t[0]
        y = t[1]
        y_nums = get_nums_in_tupe(y,tupes)
        x_nums = get_nums_in_tupe(x,tupes)
        xy_nums = sorted(list(set(y_nums).intersection(x_nums)))
        print(x)
        print(x_nums)
        print(y)
        print(y_nums)
        print(xy_nums)


def get_common_elements(master_list):
    c_list = master_list[0]
    for lst in master_list:
        if(lst == None):
            break
        c_list = sorted(list(set(c_list).intersection(lst)))
    return c_list

def find_set_of_n(tupes,num_list,master_list,set_list,n,i):
    if(i<n-1):
        for num in num_list:
            n1 = get_nums_in_tupe(num,tupes)
            master_list[i] = n1
            n2 = get_common_elements(master_list)
            if(len(n2) == 0):
                master_list[i] = None
            else:
                set_list.append(num)
                r = find_set_of_n(tupes,n2,master_list,set_list,n,i+1)
                if(r == None):
                    set_list.remove(num)
                    master_list[i] = None
                else:
                    return r
                
    else:
        set_list.append(num_list[0])
        return set_list
    
           
def get_nums_in_tupe(x,tupes):
    ts = []
    for t in tupes:
        if t[0] == x:
            ts.append(t[1])
    return ts

def find_sum(set_size):
    n = set_size
    p = 300
    start = time.time() 
    primes = get_x_num_primes(p)
    end = time.time()
    print('Time to generate',p,'primes:',end - start)
    start = time.time() 
    prime_sets = itertools.combinations(primes,2)
    tupes = []
    start = time.time() 
    for p in prime_sets:
        if(check_tup(p)):
            tupes.append(p)
    end = time.time()
    print('Time to generate tuples:',end - start)
    start = time.time() 
    nums = get_first_num_list(tupes)
    end = time.time()
    print('Time to generate list of first nums in tuples:',end - start)
    master_list = [None] * n
    start = time.time() 
    s_list = find_set_of_n(tupes,nums,master_list,[],n,0)
    end = time.time()
    print('Time to run actual logic:',end - start)
    print(s_list)
    return sum(s_list)

t_start = time.time() 
set_sum = find_sum(4)
t_end = time.time()
print(set_sum)
print('Total time:',t_end - t_start)
