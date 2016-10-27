def check_frac(x,y):
    ret_val = False
    _x = list(str(x))
    _y = list(str(y))
    c1 = 0
    c2 = 0
    for i in _x:
        c2 = 0
        for j in _y:
            if i == j:
                if c1 == 0:
                    cx = int(_x[1])
                else:
                    cx = int(_x[0])
                    
                if c2 == 0:
                    cy = int(_y[1])
                else:
                    cy = int(_y[0])

                if (not cy == 0) and (not x % 10 == 0) and (not y % 10 == 0) and cx/cy == x/y:
                    ret_val = True
            c2+=1
        c1+=1
    return ret_val

def factor(x):
    num = x[0]
    den = x[1]
    for i in range(num):
        num_val = num-i
        if(num%num_val == 0 and den%num_val == 0):
            return [num/num_val,den/num_val]

frac = [1,1]
for i in range(10,100):
    for j in range(i+1,100):
        if check_frac(i,j):
            frac[0]*=i
            frac[1]*=j

print(frac[0],'/',frac[1])
frac = factor(frac)
print(frac[0],'/',frac[1])
