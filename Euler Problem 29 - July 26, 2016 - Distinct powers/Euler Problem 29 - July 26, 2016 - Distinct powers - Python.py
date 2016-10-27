terms = []
x = 100
count=0
for a in range(2,x+1):
    for b in range(2,x+1):
        num = a**b
        if num not in terms:
            terms.append(num)

print(len(terms))
