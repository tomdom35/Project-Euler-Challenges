count = 0

for i in range(1,10):
    for j in range(1,22):
        x = i**j
        num_dig = len(str(x))
        if(num_dig == j):
            count += 1
            
print(count)
