def isPalindromic(n):
    num = str(n)
    cur1 = 0
    cur2 = len(num)-1
    while(cur1<=cur2):
        if(num[cur1] != num[cur2]):
            return False
        cur1+=1
        cur2-=1
    return True
    

def findLargestPalindrome(n):
    a = 100
    b = 100
    largest = 0
    done = False
    while not done:
        if(b+1>999):
            if(a+1>999):
                done = True
            else:
                a+=1
                b=a+1
        else:
            b+=1
        c = a*b
        if(isPalindromic(c) and c>largest):
            largest = c
    return largest

print(findLargestPalindrome(3))
