def num_digits(n):
    return len(str(n))

def has_no_repeats(n):
    num = list(str(n))
    for i in num:
        if num.count(i) > 1:
            return False
    return True

def is_pandigital(n):
    num = list(str(n))
    num.sort()
    return num == ['1','2','3','4','5','6','7','8','9']

pandigital_nums = []

for i in range(1,10000):
    m = 1
    num = i*m
    while has_no_repeats(num):
        m += 1
        digits = num_digits(num)
        if(digits > 9):
            break
        elif(digits == 9 and is_pandigital(num)):
            pandigital_nums.append(num)
            break
        num = int(str(num) + str(i * m))

print(max(pandigital_nums))
        
