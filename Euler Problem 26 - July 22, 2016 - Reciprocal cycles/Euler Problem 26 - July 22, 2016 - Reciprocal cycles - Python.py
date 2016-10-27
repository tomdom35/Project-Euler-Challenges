import math

def find_largest_repeating(d):
    max_dec = 1
    max_d = 3
    for i in range(4,d):
        dec = divide2(1,i,'',[])
        rep = len(dec)
        if rep > max_dec:
            max_d = i
            max_dec = rep
    return max_d

def divide(dividend,divisor,quotient,remainder_list):
    if(dividend in remainder_list):
        index = len(quotient) - remainder_list.index(dividend)
        return quotient[-index:]
    elif dividend == 0:
        return ''
    n = dividend
    d = divisor
    dec = quotient
    rl = remainder_list
    rl.append(n)
    zeros = -1
    while d > n:
        n*=10
        zeros += 1
    if zeros > 1:
        for i in range(zeros):
            dec += ('0')

    q = str(math.floor(n/d))
    n = n%d
    dec += q

    return divide(n,d,dec,rl)
    

    


def divide2(dividend,divisor,quotient,remainder_list):
    n = dividend
    d = divisor
    dec = quotient
    rl = remainder_list
    while(n not in rl and n != 0):
        rl.append(n)
        zeros = -1
        while d > n:
            n*=10
            zeros += 1
        if zeros > 1:
            for i in range(zeros):
                dec += ('0')

        q = str(math.floor(n/d))
        n = n%d
        dec += q

    if(n in rl):
        index = len(dec) - rl.index(n)
        return dec[-index:]
    elif n == 0:
        return ''



print(find_largest_repeating(3000))
