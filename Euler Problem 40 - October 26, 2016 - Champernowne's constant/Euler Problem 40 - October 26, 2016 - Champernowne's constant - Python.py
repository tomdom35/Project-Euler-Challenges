d = [10,100,1000,10000,100000,1000000]
num = 1
digit_count = 1
multiple = 10
digits_in_num = 1
d_num = 1
while(len(d) > 0):
    if(digit_count >= d[0]):
        i = (digit_count - d[0])+1
        temp_num = str(num)
        d_num *= int(temp_num[len(temp_num)-i])
        d.pop(0)
    num+=1
    if(num == multiple):
        digits_in_num += 1
        multiple *= 10
    digit_count += digits_in_num

print(d_num)
        
        
