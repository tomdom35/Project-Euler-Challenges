def addDigitOfSquare(n):
    num = str(2**n)
    total = 0
    for i in num:
        total+=int(i)
    return total

print(addDigitOfSquare(1000))
    
