import math

def is_abundant(n):
    sqrt = math.floor(math.sqrt(n))
    divisors = [1]
    for i in range(2,sqrt+1):
        if n % i == 0:
            div = int(n/i)
            divisors.append(i)
            if div != i:
                divisors.append(div)
    return sum(divisors)> n

abundant_nums = []
limit = 28124
nums = [False] * limit
total = 0

for i in range(12,limit):
    if is_abundant(i):
        abundant_nums.append(i)

for i in abundant_nums:
    for j in abundant_nums:
        abundant_sum = i+j
        if abundant_sum > limit-1:
            break
        else:
            nums[abundant_sum] = True

for index, i in enumerate(nums):
    if not i:
        total += index
      
print(total)
