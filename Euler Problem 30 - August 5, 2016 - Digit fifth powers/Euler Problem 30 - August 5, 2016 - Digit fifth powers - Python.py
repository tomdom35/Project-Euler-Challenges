import math

def get_nums(n):
    num = n
    nums = []
    while num >= 10:
        nums.append(num%10)
        num = math.floor(num/10)
    nums.append(num)
    return nums

def sum_powers(nums,power):
    total = 0
    for num in nums:
        total += num**power
    return total

power = 5
final_sum = 0

for i in range(2,1000000):
    nums = get_nums(i)
    total = sum_powers(nums,power)
    if total == i:
        final_sum += i

print(final_sum)



