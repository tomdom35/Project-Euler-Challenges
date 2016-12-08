def t_num(n):
    return (n*(n+1))/2

def p_num(n):
    return (n*(3*n-1))/2

def h_num(n):
    return n*(2*n-1)

t = 40755
p = 40755
h = 40755

cur_t = 286
cur_p = 166
cur_h = 144

found = False

while(not found):
    t = t_num(cur_t)
    cur_t += 1
    if(t > p):
        p = p_num(cur_p)
        cur_p += 1
    if(t > h):
        h = h_num(cur_h)
        cur_h += 1
    if(t == p and t == h):
        found = True

print(t)
