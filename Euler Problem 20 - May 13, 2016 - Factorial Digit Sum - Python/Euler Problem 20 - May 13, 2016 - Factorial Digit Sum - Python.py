def factorialSum(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
    fact = str(fact)
    fact_sum = 0
    for i in fact:
        fact_sum += int(i)
    return fact_sum

print(factorialSum(100))

