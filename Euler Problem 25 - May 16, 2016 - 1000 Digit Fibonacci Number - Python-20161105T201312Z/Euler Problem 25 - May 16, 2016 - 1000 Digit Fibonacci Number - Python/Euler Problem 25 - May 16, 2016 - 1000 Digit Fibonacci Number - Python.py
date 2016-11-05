n1 = 1
n2 = 1
n3 = 2
index = 2
num_digits = 1

while num_digits<1000:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    index += 1
    num_digits = len(str(n3))

print(index)
