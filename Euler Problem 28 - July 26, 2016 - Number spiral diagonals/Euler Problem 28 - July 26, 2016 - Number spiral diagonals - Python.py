c_nums = [1]
num = 1
gap = 1
size = int(1000/2)
for i in range(size):
    for i in range(4):
        num += (gap+1)
        c_nums.append(num)
    gap+=2

print(sum(c_nums))
