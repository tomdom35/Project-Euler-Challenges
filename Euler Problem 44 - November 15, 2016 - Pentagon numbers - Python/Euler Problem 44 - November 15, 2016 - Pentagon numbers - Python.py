def calc_nth_pent_num(n):
    return (n * (3*n-1))/2

def search(l,end):
    for j in pent_nums:
        if j > end:
            return False
        if j == end:
            return True
    return False

pent_nums = [1,5]
n = 3
found = False

while(not found):
    cur = calc_nth_pent_num(n)
    for i in reversed(pent_nums):
        temp = cur - i
        if temp >= i:
            break
        if search(pent_nums,temp):
            temp_2 = i - temp
            if search(pent_nums,temp_2):
                print(i,temp,temp_2)
                found = True
    pent_nums.append(cur)
    n += 1
                

        
