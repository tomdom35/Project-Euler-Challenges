def is_palindromic(x):
    p1 = 0
    p2 = (len(x) - 1)
    i = 0
    while p1 < p2:
        p1 = i
        p2 = (len(x) - 1) - i
        if x[p1] != x[p2]:
            return False
        i += 1
    return True

def is_lychrel(x):
    n = str(x)
    for i in range(50):
        x += int(''.join(list(reversed(n))))
        n = str(x)
        if is_palindromic(n):
            return False
    return True

count = 0

for i in range(10000):
    if(is_lychrel(i)):
        count += 1

print(count)
