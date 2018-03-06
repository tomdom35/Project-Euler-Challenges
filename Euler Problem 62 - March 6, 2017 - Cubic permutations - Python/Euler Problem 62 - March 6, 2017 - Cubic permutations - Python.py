import itertools
import time

def get_cube(n):
    return n**3

def get_first_n_cubes(n):
    cubes = []
    for i in range(1, n+1):
        cubes.append(get_cube(i))
    return cubes

def find_perms(n, cubes):
    nums = sorted(list(str(n)))
    perms = []
    for i in cubes:
        i_nums = sorted(list(str(i)))
        if i_nums == nums:
            perms.append(i)
    return perms

start = time.time()
x = 10000
cubes = get_first_n_cubes(x)
checked_cubes = []
max_cube = 1
perms = []
n = 5
for c in cubes:
    if c > max_cube:
        checked_cubes = []
    if c not in checked_cubes:
        perms = find_perms(c,cubes)
        m = max(perms)
        if m > max_cube:
            max_cube = m
        checked_cubes.extend(perms)
        if len(perms) == n:
            break
    
end = time.time()
if len(perms) == n:
    print(perms)
else:
    print('Not found... Try increasing x')
print(end - start)


