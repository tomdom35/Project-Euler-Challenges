import math
def get_divisors_sum(n):
    sqrt = math.ceil(math.sqrt(n))
    divisors = [1]
    for i in range(2,sqrt+1):
        if n % i == 0:
            div = int(n/i)
            divisors.append(i)
            if div != i:
                divisors.append(div)
    return sum(divisors)

divisor_sums = [1] * 10001
amicable = []

for i in range(2,len(divisor_sums)):
    if(divisor_sums[i] != 0):
        sum_1 = get_divisors_sum(i)
        sum_2 = get_divisors_sum(sum_1)
        divisor_sums[i] = sum_1
        if i == sum_2 and i != sum_1:
            divisor_sums[sum_1] = 0
            msg = "d("+str(i)+") = d("+str(sum_1)+")"
            print(msg)
            amicable.append(i)
            amicable.append(sum_1)
        elif sum_1<len(divisor_sums):
            divisor_sums[sum_1] = sum_2

print(amicable)
print(sum(amicable))
