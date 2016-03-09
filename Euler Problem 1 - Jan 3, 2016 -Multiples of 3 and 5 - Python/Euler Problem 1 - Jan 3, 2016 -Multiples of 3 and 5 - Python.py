def sumOfMultiples(n):
    total = 0
    for i in range(1,n):
        if(i%5==0 or i%3==0):
            total+=i
    return total

print(sumOfMultiples(1000))
