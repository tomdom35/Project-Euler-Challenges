def digit_total(x):
    t = 0
    n = list(str(x))
    for i in n:
        t += int(i)
    return t

m = 0

for i in range(100):
    for j in range(100):
        x = i**j
        t = digit_total(x)
        if t > m:
            m = t

print(m)
        
        
