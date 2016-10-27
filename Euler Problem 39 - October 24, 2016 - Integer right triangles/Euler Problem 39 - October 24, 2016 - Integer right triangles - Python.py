import math

def find_max_val(dic):
    items = list(dic.items())
    item = items[0]
    for i in items:
        if i[1] > item[1]:
            item = i
    return item

perms = dict()

for a in range(2,250):
    b = a
    while True:
        c = math.sqrt((a*a)+(b*b))
        p = a+b+c
        if(p>1000):
            break
        if c.is_integer():
            if(p in perms):
                perms[p] += 1
            else:
                perms[p]=1
        b+=1

print(find_max_val(perms))
