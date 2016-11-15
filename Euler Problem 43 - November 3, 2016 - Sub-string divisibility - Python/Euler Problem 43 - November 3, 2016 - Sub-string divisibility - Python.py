import itertools

num = ['9','8','7','6','5','4','3','2','1','0']
num_list = list(itertools.permutations(num))
primes = [0,2,3,5,7,11,13,17]
nums = []

for num in num_list:
    for i in range(1,8):
        x = True
        index = (10-(i+3))
        if(index != 0):
            index *= -1
            new_num = num[i:index]
        else:
            new_num = num[i:]
        new_num = int(''.join(new_num))
        if new_num % primes[i] != 0:
            x = False
            break
    if x:
        n = int(''.join(num))
        nums.append(n)

print(sum(nums))
