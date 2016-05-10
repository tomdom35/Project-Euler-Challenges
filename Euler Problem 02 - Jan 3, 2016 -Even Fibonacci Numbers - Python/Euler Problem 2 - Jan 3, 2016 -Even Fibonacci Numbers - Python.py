def findEvenFibNumsSum(n):
    total = 2
    a = 1
    b = 2
    c = 3
    while(c<n):
        if(c%2==0):
            total+=c
        a = b
        b = c
        c = a + b
    return total

print(findEvenFibNumsSum(4000000))
