def is_palindromic(x):
    cur_1 = 0
    cur_2 = len(x)-1
    while(cur_1 <= cur_2):
        if(x[cur_1] != x[cur_2]):
            return False
        cur_1 += 1
        cur_2 -= 1
    return True

total = 0

for i in range(0,500000):
    x = 2*i+1
    num = list(str(x))
    num_2 = list(bin(x))[2:]
    if(is_palindromic(num) and is_palindromic(num_2)):
        total += x

print(total)
