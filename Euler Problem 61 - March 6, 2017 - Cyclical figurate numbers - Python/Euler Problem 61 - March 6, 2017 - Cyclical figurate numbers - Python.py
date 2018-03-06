import math
import time

def get_size(lst):
    size = 0
    for i in lst:
        size += len(i)
    return size

def check_start(p_list, num, index):
    dig = num[-2:]
    found = False
    for i,p in enumerate(p_list):
        if(i != index):
            for n in p:
                if(n[:2] == dig):
                    found = True
                    break
        if found:
            break
    if not found:
        p_list[index].remove(num)

def remove_items(p_list):
    size = get_size(p_list)
    s = 0
    while size != s:
        for i,p in enumerate(p_list):
            for num in p:
                check_start(p_list, num, i)
        s = size
        size = get_size(p_list)

def find_cyclic_list(p_list, num, indices, s):
    dig = num[-2:]
    found = False
    for i,p in enumerate(p_list):
        if(i not in indices):
            for n in p:
                if(n[:2] == dig):
                    found = True
                    s.append(n)
                    indices.append(i)
                    find_cyclic_list(p_list, n, indices, s)
    if not found and len(s) < 6:
        s.pop()

def get_sum(s):
    total = 0
    for i in s:
        total += int(i)
    return total
                   
def p3(n):
    return math.floor(n*(n+1)/2)

def p4(n):
    return math.floor(n*n)

def p5(n):
    return math.floor(n*((3*n)-1)/2)

def p6(n):
    return math.floor(n*(2*n-1))

def p7(n):
    return math.floor(n*(5*n-3)/2)

def p8(n):
    return math.floor(n*(3*n-2))


def get_p_list(p_func):
    p = 0
    n = 0
    p_list = []
    while p < 10000:
        if p > 999 and p%10 != 0:
            p_list.append(str(p))
        n += 1
        p = p_func(n)
    return p_list

start = time.time()

p_list = []
p_list.append(get_p_list(p3))
p_list.append(get_p_list(p4))
p_list.append(get_p_list(p5))
p_list.append(get_p_list(p6))
p_list.append(get_p_list(p7))
p_list.append(get_p_list(p8))

remove_items(p_list)

for i,p in enumerate(p_list):
    for num in p:
        s = [num]
        indices = [i]
        find_cyclic_list(p_list, num, indices, s)
        if len(s) == 6:
            if s[0][:2] == s[5][-2:]:
                end = time.time()
                print(s)
                print(get_sum(s))
                print(end - start)
                

