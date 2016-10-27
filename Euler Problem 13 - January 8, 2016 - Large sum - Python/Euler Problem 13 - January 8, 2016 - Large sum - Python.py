nums = []
with open('input.txt') as file:
    for line in file:
        num = list(line.rstrip())
        for i in range(0,len(num)):
            num[i] = int(num[i])
        nums.append(num)


num1 = [1,2,3,4,5,6,7,8,9]
num2 = [2,4,6,8,1,3,5,7,9]

num3 = [1,2,3,4,5,6]
num4 = [9,3,6]

num5 = [1,0]
num6 = []


def add(x,y):
    num1 = x
    num2 = y
    num1.reverse()
    num2.reverse()
    total = []
    for i in range(0,max(len(num1),len(num2))):
        if(i<len(num1) and i<len(num2)):
            val = num1[i] + num2[i]
        elif(i<len(num1)):
             val = num1[i]
        else:
             val = num2[i]
        total.append(val%10)
        if(val>=10):
            if(i<len(num1)-1):
                num1[i+1] = num1[i+1] + 1
            elif(i<len(num2)-1):
                num2[i+1] = num2[i+1] + 1
            else:
                total.append(1)
    total.reverse()
    return total

def totalSum(nums):
    total = []
    for num in nums:
        total = add(total,num)
    return total

print(totalSum(nums))


