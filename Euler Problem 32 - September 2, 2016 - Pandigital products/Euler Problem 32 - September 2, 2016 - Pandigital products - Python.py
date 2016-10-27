def num_repeats_or_zeros(x):
    new_x = list(str(x))
    count = 0
    for i in new_x:
        count = 0
        if i == '0':
            return True
        for j in new_x:
            if i == j:
                count+=1
        if count > 1:
            return True
    return False

def num_contains(x,y):
    new_y = list(str(y))
    for i in new_y:
        if i in str(x):
            return True
    return False

n = 4987
total = []

for i in range(2,98):
    if not num_repeats_or_zeros(i):
        for j in range(i+1,n):
            if not (num_contains(j,i) or num_repeats_or_zeros(j)):
                prod = i*j
                if not(num_contains(prod,j) or num_contains(prod,i) or num_repeats_or_zeros(prod) or prod in total) and len(str(prod)+str(i)+str(j)) == 9:
                    total.append(prod)
print(sum(total))
