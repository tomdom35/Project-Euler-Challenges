import math

def fact(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def get_digits(num):
    curNum = num
    nums = []
    while(curNum/10 > 1):
        nums.append(curNum%10)
        curNum = math.floor(curNum/10)
    nums.append(curNum)
    return nums

def check_fact_sum(num):
    nums = get_digits(num)
    total = 0
    for i in nums:
        total += fact(i)
        if total > num:
            return False
    if total == num:
        return True
    else:
        return False

start = 10
end = 7*fact(9)
nums = []

for i in range(start,end):
    if check_fact_sum(i):
        nums.append(i)

print(nums)
