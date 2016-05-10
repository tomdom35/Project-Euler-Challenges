def sumOfSquares(n):
    total = 0
    for i in range(1,n+1):
        total+=i*i
    return total

def squareOfSum(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total*total

print(squareOfSum(100) - sumOfSquares(100))
