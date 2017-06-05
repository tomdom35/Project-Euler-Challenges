def getDigits(x):
    return sorted(list(str(x)))

x = 0
done = False

while not done:
    x += 1
    digits = getDigits(x)
    for i in range(2,6):
        done = True
        n = x*i
        n_digits = getDigits(n)
        if(n_digits != digits):
            done = False
            break;

print(x)
        
        
    
