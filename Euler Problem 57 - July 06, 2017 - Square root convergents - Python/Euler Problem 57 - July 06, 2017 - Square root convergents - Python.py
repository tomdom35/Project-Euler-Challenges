def count_digits(x):
    return len(str(x))

oldest_numer = 1
oldest_denom = 1

old_numer = 3
old_denom = 2

count = 0

for i in range(999):
    numer = old_numer*2 + oldest_numer
    denom = old_denom*2 + oldest_denom
    
    numer_digits = count_digits(numer)
    denom_digits = count_digits(denom)

    if numer_digits > denom_digits:
        count += 1

    oldest_numer = old_numer
    oldest_denom = old_denom

    old_numer = numer
    old_denom = denom

print(count)
    
    
