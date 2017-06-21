def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)

def combo_num(n, r):
    numerator = factorial(n)
    d1 = factorial(r)
    d2 = factorial(n-r)
    denominator = d1 * d2
    result = numerator/denominator
    return result

r = 0
count = 0

for n in range(1,101):
    for r in range(1,n):
        r = combo_num(n,r)
        if(r > 1000000):
            count += 1
        
print(count)
